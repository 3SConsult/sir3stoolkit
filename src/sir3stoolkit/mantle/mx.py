# -*- coding: utf-8 -*-
"""
Internal: reading calculation results directly from the SIR 3S result files - .MX1 (channel metadata,
XML), .MX2 (object lists) and .MXS (results, one fixed-size record per snapshot) - instead of one
GetResultfortimestamp() call per value. Only used through generate_element_results_dataframe(bulk=True);
nothing in here is meant to be called directly.

Values are decoded with numpy directly from the file's bytes (file-native float32/int32), reading only
the byte ranges of the requested channels, records and tks, in bounded chunks. Nothing is memory-mapped
and no result data is kept after a request, so SirCalc can overwrite the .MXS between reads. Only the
file metadata (channels, tk lists, record index) is reused while the .MXS file is unchanged.

AI assistant: see sir3stoolkit/__init__.py for orientation (architecture, API/property reference,
known gotchas) before writing code against this module.

@author: Jablonski
"""
from __future__ import annotations

import ctypes
import os
import re
import shutil
import struct
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from decimal import Decimal, Context, ROUND_HALF_UP
from enum import Enum
from typing import Dict, List, Optional, Sequence, Tuple, Union

from sir3stoolkit.dependency_check import require_packages
require_packages(__name__, "numpy", "pandas")

import numpy as np
import pandas as pd

from sir3stoolkit.core.wrapper import SIR3S_Model
from sir3stoolkit.logging_utils import get_logger
from sir3stoolkit.mantle.advanced_operations import mapping_for_groups

logger = get_logger(__name__)


class SIR3S_Model_MX(SIR3S_Model):
    """
    Internal mixin: reads results straight from the .MX1/.MX2/.MXS result files for
    generate_element_results_dataframe(bulk=True). All members are private.
    """

    _MX_KNOWN_DATATYPES = {"CHAR", "INT4", "REAL", "RVEC"}
    _MX_NUMERIC_DTYPES = {"INT4": np.dtype("<i4"), "REAL": np.dtype("<f4"), "RVEC": np.dtype("<f4")}
    # Numeric results are returned as float32: the precision the result files store (and the SIR 3S
    # Toolkit API reads), so every value is kept exactly at half the memory of float64.
    _MX_RESULT_DTYPE = np.dtype("float32")
    _MX_VEC_FORMATS = ("str", "multiindex")
    _MX_MAX_CHUNK_BYTES = 512 * 1024**2
    # Byte ranges (channels, or the items of selected tks within a channel) closer together than this
    # are fetched with one read per record instead of one read each. Measured on a local NVMe: one
    # extra read costs ~0.1 ms, about as long as transferring ~100 KiB, so skipping less than that
    # doesn't pay off; 256 KiB leaves headroom for storage where a read call costs more (HDD, network).
    _MX_SPAN_MERGE_GAP_BYTES = 256 * 1024
    # Reads of at least this size log their progress.
    _MX_PROGRESS_LOG_MIN_BYTES = 64 * 1024**2
    # Refuse to build a result DataFrame estimated to need more than this share of the available memory.
    _MX_MAX_RESULT_SHARE_OF_AVAILABLE = 0.5
    # SIR 3S formats result values as 7-significant-digit, upper-case-E strings, with ties rounded
    # away from zero (Python's default rounds ties to even) - this context reproduces that.
    _MX_FLOAT_FORMAT_CTX = Context(prec=7, rounding=ROUND_HALF_UP)

    # --- data containers ------------------------------------------------------------------------

    class _MxFileChangedError(RuntimeError):
        """The .MXS file changed (e.g. a new calculation started) while it was being read."""

    @dataclass(frozen=True)
    class _MxChannel:
        """One .MX1 channel: a fixed byte range inside every .MXS record."""
        sir3s_id: str
        objtype: str
        name1: str
        name2: str
        objtype_pk: str
        attrtype: str
        datatype: str
        offset: int
        length: int
        item_length: int

        @property
        def n_items(self) -> int:
            return self.length // self.item_length

        @property
        def is_element_type_channel(self) -> bool:
            """One value per instance of the element type (listed in .MX2), not a single-object channel."""
            return self.name1 == "*" and self.name2 == "*" and self.objtype_pk == "*"

        @property
        def dtype(self) -> np.dtype:
            """numpy dtype of the decoded array: file-native float32/int32, raw bytes (uint8) for CHAR."""
            return SIR3S_Model_MX._MX_NUMERIC_DTYPES.get(self.datatype, np.dtype("u1"))

        @property
        def row_shape(self) -> Tuple[int]:
            return (self.length,) if self.datatype == "CHAR" else (self.n_items,)

    @dataclass
    class _MxLayout:
        """How one element type (MX OBJTYPE) is laid out in the result files."""
        objtype: str
        tks: List[str]
        scalar_channels: Dict[str, "SIR3S_Model_MX._MxChannel"] = field(default_factory=dict)
        vector_channels: Dict[str, "SIR3S_Model_MX._MxChannel"] = field(default_factory=dict)
        unresolvable_vector_props: List[str] = field(default_factory=list)
        skipped_props: List[str] = field(default_factory=list)
        segment_offsets: Optional[np.ndarray] = None
        # Properties written only for individual objects (channel OBJTYPE~NAME1~NAME2~tk~ATTRTYPE, e.g.
        # selected for a time curve), not for the whole element type: {property: {tk: channel}}.
        single_channels: Dict[str, Dict[str, "SIR3S_Model_MX._MxChannel"]] = field(default_factory=dict)

        @property
        def readable_props(self) -> List[str]:
            return list(self.scalar_channels) + list(self.vector_channels) + list(self.single_channels)

        def channel_ids(self, props: Sequence[str]) -> List[str]:
            ids = []
            for prop in props:
                if prop in self.scalar_channels:
                    ids.append(self.scalar_channels[prop].sir3s_id)
                elif prop in self.vector_channels:
                    ids.append(self.vector_channels[prop].sir3s_id)
                elif prop in self.single_channels:
                    ids.extend(c.sir3s_id for c in self.single_channels[prop].values())
            return ids

    @dataclass
    class _MxFile:
        """Metadata of one calculation's result files (no result values)."""
        mx1_path: str
        mx2_path: str
        mxs_path: str
        mx1_df: pd.DataFrame
        record_length: int
        channels: Dict[str, "SIR3S_Model_MX._MxChannel"]
        signature: Tuple[float, int]
        n_records: int
        version: str = ""
        records: Optional[pd.DataFrame] = None
        mx2_df: Optional[pd.DataFrame] = None
        layouts: Dict[str, "SIR3S_Model_MX._MxLayout"] = field(default_factory=dict)

    @dataclass
    class _MxFramePlan:
        """Which file values go to which DataFrame column, worked out once per request."""
        layout: "SIR3S_Model_MX._MxLayout"
        place_holder_value: float
        groups: list
        items: Dict[str, Optional[np.ndarray]]
        dest: np.ndarray
        n_float: int
        n_obj: int
        columns: pd.MultiIndex
        float_columns: Optional[pd.MultiIndex] = None
        obj_columns: Optional[pd.MultiIndex] = None
        restore: Optional[np.ndarray] = None

    class _MxProgress:
        """Logs the progress of a long loop at every 20 %."""

        def __init__(self, log, label: str, total: int, unit: str, enabled: bool = True):
            self.log, self.label, self.total, self.unit = log, label, total, unit
            self.enabled = enabled and total > 0
            self.done = 0
            self.next_pct = 20
            self.t0 = time.perf_counter()

        def update(self, n: int = 1) -> None:
            if not self.enabled:
                return
            self.done += n
            pct = self.done * 100 // self.total
            if pct >= self.next_pct:
                self.log.info(f"{self.label}: {min(pct, 100)} % ({self.done:,}/{self.total:,} {self.unit}, "
                              f"{time.perf_counter() - self.t0:.1f} s)")
                while self.next_pct <= pct:
                    self.next_pct += 20

    # --- small utilities ------------------------------------------------------------------------

    @staticmethod
    def _mx_format_float(value: float) -> str:
        """Format a float the way SIR 3S formats result values: 7 significant digits, upper-case
        scientific notation for very small/large magnitudes, ties rounded away from zero."""
        if value == 0.0:
            return "0"
        rounded = SIR3S_Model_MX._MX_FLOAT_FORMAT_CTX.create_decimal(Decimal(value))
        return "{:.7G}".format(float(rounded))

    @staticmethod
    def _mx_format_floats(values: np.ndarray) -> np.ndarray:
        """
        _mx_format_float() for a whole array, with identical results but much faster on real results:
        each distinct value is formatted once, and the slow exact (Decimal) rounding is only used where a
        tie is possible - everywhere else "{:.7G}" gives the same digits, since it only rounds
        differently (ties to even) on an exact tie at the 7th significant digit.
        """
        values = np.asarray(values)
        if values.size == 0:
            return np.empty(values.shape, dtype=object)
        unique, inverse = np.unique(values, return_inverse=True)
        formatted = []
        for v in unique.astype(np.float64).tolist():
            # An exact tie at the 7th significant digit means the 8th digit is exactly 5 - only those
            # candidates need the exact check ("%.7E" has 8 significant digits, the 8th right before "E").
            eight = "%.7E" % v
            if eight[eight.find("E") - 1] == "5" or v == 0.0:
                formatted.append(SIR3S_Model_MX._mx_format_float(v))
            else:
                formatted.append("{:.7G}".format(v))
        return np.array(formatted, dtype=object)[inverse.reshape(-1)].reshape(values.shape)

    @staticmethod
    def _mx_physical_memory() -> Tuple[int, int]:
        """(total, available) physical memory in bytes; (8 GiB, 4 GiB) if it can't be determined."""
        try:
            if sys.platform == "win32":
                class _MemoryStatusEx(ctypes.Structure):
                    _fields_ = [
                        ("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                        ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                        ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                    ]
                status = _MemoryStatusEx()
                status.dwLength = ctypes.sizeof(_MemoryStatusEx)
                if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
                    return int(status.ullTotalPhys), int(status.ullAvailPhys)
            else:
                page = os.sysconf("SC_PAGE_SIZE")
                return page * os.sysconf("SC_PHYS_PAGES"), page * os.sysconf("SC_AVPHYS_PAGES")
        except Exception as e:
            logger.warning(f"[mx] Could not determine physical memory ({e}); assuming 8 GiB total / 4 GiB available.")
        return 8 * 1024**3, 4 * 1024**3

    @staticmethod
    def _mx_as_indexer(positions: np.ndarray) -> Union[slice, np.ndarray]:
        """A slice (basic, fast indexing) if positions form an arithmetic progression, else the array."""
        n = len(positions)
        if n == 0:
            return positions
        if n == 1:
            return slice(int(positions[0]), int(positions[0]) + 1)
        step = int(positions[1] - positions[0])
        if step > 0 and np.all(np.diff(positions) == step):
            return slice(int(positions[0]), int(positions[-1]) + 1, step)
        return positions

    @staticmethod
    def _mx_order_columns(df: pd.DataFrame, tks: Sequence[str], props: Sequence[str]) -> pd.DataFrame:
        """Reorder result columns tk-major / property-minor (then interior point), following tks and
        props; columns whose tk or property isn't listed go last, in their current order."""
        if df.shape[1] == 0:
            return df
        tk_rank = {tk: i for i, tk in enumerate(tks)}
        prop_rank = {p: i for i, p in enumerate(props)}
        tk_keys = np.array([tk_rank.get(tk, len(tk_rank)) for tk in df.columns.get_level_values(0)])
        prop_keys = np.array([prop_rank.get(p, len(prop_rank)) for p in df.columns.get_level_values(1)])
        point_keys = (np.asarray(df.columns.get_level_values(2), dtype=np.int64)
                      if df.columns.nlevels > 2 else np.zeros(df.shape[1], dtype=np.int64))
        order = np.lexsort((np.arange(df.shape[1]), point_keys, prop_keys, tk_keys))
        if np.array_equal(order, np.arange(df.shape[1])):
            return df
        return df.iloc[:, order]

    # --- model / file paths ---------------------------------------------------------------------

    def _mx_result_directory(self) -> str:
        """Directory of the open model's result files: <working_directory>\\B<b>\\V<v>\\BZ<bz> (from self.Mid)."""
        if not self.Mid:
            raise ValueError("[mx] No model is open (self.Mid is not set). Call OpenModel() first.")
        parts = self.Mid.split("-")
        if len(parts) != 4 or parts[0] != "M":
            raise ValueError(f"[mx] Unexpected Mid format: {self.Mid!r}. Expected 'M-<b>-<v>-<bz>'.")
        _, b, v, bz = parts
        working_directory = self.GetWorkingDirectory()
        if not working_directory:
            raise ValueError("[mx] GetWorkingDirectory() returned no working directory.")
        return os.path.join(working_directory, f"B{b}", f"V{v}", f"BZ{bz}")

    def _mx_current_mx1_filepath(self, dot_resolution: Optional[int] = None) -> str:
        """
        Absolute path to the .MX1 file of the currently open model (existence isn't checked), e.g.
        "<working_directory>\\B1\\V0\\BZ1\\M-1-0-1.<dot_resolution>.MX1" - the format with an output
        factor in the name (for the format without one and which file is read by default, see
        _mx_resolve_mx1()).

        The dot resolution is an output factor of the model (TIMD.DTFAK_KLEIN / DTFAK_GROSS). With equal
        factors SirCalc writes one result file set, ".<factor>". With different factors it writes two:
        ".<DTFAK_KLEIN>" with just the time-curve channels at the finer interval, and ".<DTFAK_GROSS>" with
        all channels (all element types) at the coarser interval - the one GetTimeStamps() refers to.
        Default: None, i.e. the DTFAK_GROSS file of the most recent calculation (see _mx_output_factors()).
        """
        if dot_resolution is None:
            dot_resolution = self._mx_output_factors()[1]
        return os.path.join(self._mx_result_directory(), f"{self.Mid}.{dot_resolution}.MX1")

    def _mx_resolve_mx1(self, output_factor: Optional[int] = None) -> str:
        """
        The .MX1 file to read for the open model. Result files come in two formats: without an output
        factor in the name ("M-1-0-1.MX1") or with one ("M-1-0-1.<factor>.MX1", see
        _mx_current_mx1_filepath()).

        output_factor=None: the file without an output factor if it exists, otherwise the DTFAK_GROSS
        file of the most recent calculation. output_factor given: the file of that factor (any factor
        with result files, also from an earlier calculation), also when a file without an output factor
        exists.
        """
        if output_factor is None:
            plain = os.path.join(self._mx_result_directory(), f"{self.Mid}.MX1")
            if os.path.exists(plain):
                return plain
        return self._mx_current_mx1_filepath(self._mx_resolve_output_factor(output_factor))

    def _mx_describe_file(self, mx1_filepath: str, output_factor: Optional[int] = None) -> str:
        """For logging: the result file and its output factor, e.g. "M-1-0-1.4.MX1 (output factor 4 =
        DTFAK_GROSS of the most recent calculation, default)"."""
        name = os.path.basename(mx1_filepath)
        how = "default" if output_factor is None else "output_factor parameter"
        factor = os.path.splitext(os.path.splitext(name)[0])[1].lstrip(".")
        if not factor.isdigit():
            return f"{name} (no output factor in the file name, {how})"
        factor = int(factor)
        try:
            all_factors, recent = self._mx_result_factors()
        except FileNotFoundError:
            return f"{name} (output factor {factor}, {how})"
        if factor not in recent:
            role = "from an earlier calculation"
        elif recent[0] == recent[-1]:
            role = "DTFAK_KLEIN = DTFAK_GROSS of the most recent calculation"
        elif factor == recent[-1]:
            role = "DTFAK_GROSS of the most recent calculation"
        else:
            role = "DTFAK_KLEIN of the most recent calculation"
        return f"{name} (output factor {factor} = {role}, {how})"

    def _mx_resolve_output_factor(self, output_factor: Optional[int]) -> int:
        """The output factor to read: output_factor if result files exist for it (from the most recent
        calculation or an earlier one), DTFAK_GROSS of the most recent calculation if None."""
        if output_factor is None:
            return self._mx_output_factors()[1]
        all_factors, recent = self._mx_result_factors()
        if output_factor not in all_factors:
            described = ", ".join(f"{f} ({'most recent calculation' if f in recent else 'earlier calculation'})"
                                  for f in all_factors)
            raise ValueError(
                f"[mx] output_factor={output_factor!r} has no result files for this model; available: {described}. "
                f"In the most recent calculation, the smallest factor (DTFAK_KLEIN) holds only the time-curve "
                f"channels at the finer interval, the largest (DTFAK_GROSS, the default) all channels."
            )
        return int(output_factor)

    def _mx_file_timestamps(self, mx_file: "SIR3S_Model_MX._MxFile",
                            timestamps: Optional[Sequence[Union[str, int]]]) -> Tuple[List[str], List[int]]:
        """
        Timestamps and record numbers from a result file's own timeline (for the DTFAK_KLEIN file finer
        than GetTimeStamps()). timestamps: None (all), indices into the file's timeline, or timestamp
        strings (matched by instant). Labels are formatted like GetTimeStamps() strings
        ("2023-02-13 00:00:00.000 +01:00") from the local time and offset the file stores, so no
        (slow, for big result files) GetTimeStamps() call is needed.
        """
        timeline = self._mx_timeline_records(mx_file)
        instants = list(mx_file.records.loc[timeline, "timestamp"])
        if timestamps is None:
            selected = list(range(len(timeline)))
        elif timestamps and isinstance(timestamps[0], int):
            selected = []
            for i in timestamps:
                if -len(timeline) <= i < len(timeline):
                    selected.append(i % len(timeline))
                else:
                    logger.warning(f"[mx] Index {i} out of bounds for the {len(timeline)} timestamps of "
                                   f"{os.path.basename(mx_file.mx1_path)}. It will be excluded.")
        else:
            position = {ts: i for i, ts in enumerate(instants)}
            selected = []
            for label, ts in zip(timestamps, pd.to_datetime(list(timestamps), utc=True)):
                if ts in position:
                    selected.append(position[ts])
                else:
                    logger.warning(f"[mx] Timestamp {label} is not in {os.path.basename(mx_file.mx1_path)}. It will be excluded.")

        labels = list(mx_file.records.loc[timeline[selected], "label"]) if selected else []
        records = [int(timeline[i]) for i in selected]
        return labels, records

    def _mx_result_factors(self) -> Tuple[List[int], List[int]]:
        """
        Output factors with result files ("M-1-0-1.<factor>.MX1" plus .MXS) in the open model's result
        directory: (all of them, those from the most recent calculation), both sorted. SirCalc rewrites the
        .MX2 in every calculation (after the .MX1, before the .MXS), so files whose .MXS is older than the
        .MX2 are from an earlier calculation, e.g. left over from other output factors.
        """
        directory = self._mx_result_directory()
        mx2 = os.path.join(directory, f"{self.Mid}.MX2")
        if not os.path.exists(mx2):
            raise FileNotFoundError(f"[mx] No result files (.MX2) for {self.Mid} in {directory}; calculate the model first.")
        mx2_mtime = os.path.getmtime(mx2)
        all_factors, recent = [], []
        prefix = f"{self.Mid}.".lower()
        for name in os.listdir(directory):
            stem, ext = os.path.splitext(name)
            if ext.upper() != ".MX1" or not stem.lower().startswith(prefix):
                continue
            factor = stem[len(prefix):]
            mxs = os.path.join(directory, f"{stem}.MXS")
            if factor.isdigit() and os.path.exists(mxs):
                all_factors.append(int(factor))
                if os.path.getmtime(mxs) >= mx2_mtime:
                    recent.append(int(factor))
        if not all_factors:
            raise FileNotFoundError(f"[mx] No result files with an output factor (\"{self.Mid}.<factor>.MX1\") "
                                    f"in {directory}.")
        return sorted(all_factors), sorted(recent)

    def _mx_output_factors(self) -> Tuple[int, int]:
        """
        (DTFAK_KLEIN, DTFAK_GROSS) of the open model's most recent calculation, taken from its result
        files (see _mx_result_factors()): the smallest and the largest factor of the files from the most
        recent calculation (the same factor if there is only one). If no file is from the most recent
        calculation, all files are used (reading one then logs a warning, see _mx_open_file()).

        TODO: _discover_output_factors() reads the factors from the model itself instead, but is not used
        for now: it needs a GetTimeStamps() call to undo a side effect of WriteSirCalcXmlFile() on the
        API, which takes ~20 s for large result files. Switch back once that side effect is fixed.
        """
        all_factors, recent = self._mx_result_factors()
        factors = recent or all_factors
        return factors[0], factors[-1]

    def _discover_output_factors(self) -> Tuple[int, int]:
        """
        Discover the currently configured MX result-output factors (SIR 3S: TIMD.DTFAK_KLEIN /
        TIMD.DTFAK_GROSS) of the currently open model: the time-curve and the numeric-display output
        intervals, which end up as dot-resolution numbers in the result file names (e.g. "M-1-0-1.1.MX1").
        Implemented by exporting a throwaway SirCalc XML file into a temporary directory.

        Side effect of WriteSirCalcXmlFile() (SIR 3S Toolkit 90-15-26): GetResultfortimestamp() returns
        empty strings afterwards until GetTimeStamps() is called again, which reloads the results - so
        that's done here right after the export. NOT USED for now (that call takes ~20 s for large result
        files); _mx_output_factors() takes the factors from the result files instead.

        :return: (output_factor_small, output_factor_large)
        :rtype: Tuple[int, int]
        """
        if not self.Mid:
            raise ValueError("[_discover_output_factors] No model is open (self.Mid is not set). Call OpenModel() first.")

        tmp_dir = tempfile.mkdtemp(prefix="sir3s_output_factors_")
        try:
            xml_path = self.WriteSirCalcXmlFile(saveItInThisDirectory=tmp_dir)
            if not xml_path:
                raise ValueError("[_discover_output_factors] WriteSirCalcXmlFile() failed (returned no path).")
            with open(xml_path, encoding="Windows-1252") as f:
                content = f.read()
            timd_match = re.search(r"<TIMD\b[^>]*/>", content)
            if not timd_match:
                raise ValueError(f"[_discover_output_factors] No <TIMD> element found in {xml_path}.")
            timd_tag = timd_match.group(0)
            small_match = re.search(r'\bDTFAK_KLEIN="(\d+)"', timd_tag)
            large_match = re.search(r'\bDTFAK_GROSS="(\d+)"', timd_tag)
            if not small_match or not large_match:
                raise ValueError(f"[_discover_output_factors] DTFAK_KLEIN/DTFAK_GROSS not found in: {timd_tag}")
            output_factor_small = int(small_match.group(1))
            output_factor_large = int(large_match.group(1))
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            try:
                self.GetTimeStamps()  # reload the results for the API, see docstring
            except Exception:
                pass  # no results yet (model never calculated)

        logger.info(f"[_discover_output_factors] output_factor_small={output_factor_small}, "
                    f"output_factor_large={output_factor_large}.")
        return output_factor_small, output_factor_large

    @staticmethod
    def _mx_objtype(element_type: Union[Enum, str]) -> str:
        """MX OBJTYPE code (e.g. "ROHR") of an element type given as ObjectTypes member or OBJTYPE code."""
        if isinstance(element_type, Enum):
            code = mapping_for_groups.get(element_type.name)
            if not code or code == -1:
                raise ValueError(
                    f"[mx] No MX OBJTYPE code known for element type '{element_type.name}'; its results "
                    "can't be read from the result files (use bulk=False)."
                )
            return code
        return str(element_type)

    # --- .MX1 / .MX2 parsing --------------------------------------------------------------------

    @staticmethod
    def _mx_parse_mx1(mx1_filepath: str) -> pd.DataFrame:
        """One row per .MX1 channel, all attributes, plus Sir3sID (OBJTYPE~NAME1~NAME2~OBJTYPE_PK~ATTRTYPE)."""
        root = ET.parse(mx1_filepath).getroot()
        df = pd.DataFrame([dict(ch.attrib) for ch in root.findall("XL1")])
        if df.empty:
            raise ValueError(f"[mx] .MX1 file contains no channels: {mx1_filepath}")
        for col in ["DATALENGTH", "DATATYPELENGTH", "DATAOFFSET", "FLAGS"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="raise").astype("int64")
        df["Sir3sID"] = (df["OBJTYPE"].astype(str) + "~" + df["NAME1"].astype(str) + "~" + df["NAME2"].astype(str)
                         + "~" + df["OBJTYPE_PK"].astype(str) + "~" + df["ATTRTYPE"].astype(str))
        df["NOfItems"] = df["DATALENGTH"] // df["DATATYPELENGTH"]
        return df

    @staticmethod
    def _mx_parse_mx2(mx2_filepath: str) -> pd.DataFrame:
        """One row per .MX2 block (ObjType, AttrType, DataType, ..., Data: tuple of values; CHAR decoded
        and right-stripped, REAL skipped) - e.g. the tk list and N_OF_POINTS per element type."""
        if not os.path.exists(mx2_filepath):
            raise FileNotFoundError(f"[mx] .MX2 file does not exist: {mx2_filepath}")
        rows = []
        with open(mx2_filepath, "rb") as f:
            next_header = 0
            while True:
                header = f.read(64)
                if len(header) != 64:
                    if header:
                        logger.warning(f"[mx] Unexpected trailing .MX2 bytes: {len(header)}")
                    break
                obj_type, attr_type, data_type, type_length, data_length = struct.unpack("12s12s4si28xi", header)
                obj_type = obj_type.decode("utf-8").rstrip()
                attr_type = attr_type.decode("utf-8").rstrip()
                data_type = data_type.decode("utf-8").rstrip()
                n_items = int(data_length // type_length)
                data_bytes = f.read(data_length)
                if data_type == "CHAR":
                    data = tuple(item.decode("utf-8").rstrip()
                                 for item in struct.unpack(f"{type_length}s" * n_items, data_bytes))
                elif data_type == "INT4":
                    data = struct.unpack("i" * n_items, data_bytes)
                else:
                    data = ()
                rows.append({"ObjType": obj_type, "AttrType": attr_type, "DataType": data_type,
                             "DataTypeLength": int(type_length), "DataLength": int(data_length),
                             "NOfItems": n_items, "Data": data})
                next_header += 64 + data_length
                if f.tell() != next_header:
                    f.seek(next_header)
        return pd.DataFrame(rows)

    # --- result file metadata -------------------------------------------------------------------

    def _mx_get_file(self, mx1_filepath: Optional[str] = None) -> "SIR3S_Model_MX._MxFile":
        """Metadata of mx1_filepath's result files (default: the open model's current .MX1), reused
        while the .MXS file is unchanged."""
        if mx1_filepath is None:
            mx1_filepath = self._mx_resolve_mx1()
        key = os.path.normcase(os.path.abspath(mx1_filepath))
        mx_file = getattr(self, "_mx_file", None)
        if mx_file is not None and getattr(self, "_mx_file_key", None) == key:
            try:
                self._mx_check_unchanged(mx_file)
                return mx_file
            except (OSError, RuntimeError):
                logger.info("[mx] Result file changed since it was last read; reloading.")
        self._mx_file = self._mx_open_file(mx1_filepath)
        self._mx_file_key = key
        return self._mx_file

    def _mx_open_file(self, mx1_filepath: str) -> "SIR3S_Model_MX._MxFile":
        """Parse the .MX1, check the files belong together and read the record index."""
        if not os.path.exists(mx1_filepath):
            raise FileNotFoundError(f"[mx] .MX1 file does not exist: {mx1_filepath}")
        work_dir, file_name = os.path.split(mx1_filepath)
        base, dot_resolution = os.path.splitext(os.path.splitext(file_name)[0])
        mx2 = os.path.join(work_dir, f"{base}.MX2")
        mxs = os.path.join(work_dir, f"{base}{dot_resolution}.MXS")

        mx1_df = self._mx_parse_mx1(mx1_filepath)
        unknown = mx1_df[~mx1_df["DATATYPE"].isin(self._MX_KNOWN_DATATYPES)]
        if not unknown.empty:
            logger.warning(f"[mx] Skipping {len(unknown)} channel(s) with unrecognized DATATYPE(s) "
                           f"{sorted(set(unknown['DATATYPE']))}: {list(unknown['Sir3sID'])}")
        # Same check as PT3S.Mx: numeric items are 4-byte float32/int32.
        bad_length = mx1_df[mx1_df["DATATYPE"].isin(list(self._MX_NUMERIC_DTYPES)) & (mx1_df["DATATYPELENGTH"] != 4)]
        if not bad_length.empty:
            logger.warning(f"[mx] Skipping {len(bad_length)} numeric channel(s) with DATATYPELENGTH != 4: "
                           f"{list(bad_length['Sir3sID'])}")
        usable = mx1_df["DATATYPE"].isin(self._MX_KNOWN_DATATYPES) & ~mx1_df.index.isin(bad_length.index)
        channels = {}
        for row in mx1_df[usable].sort_values("DATAOFFSET").itertuples():
            channels[row.Sir3sID] = self._MxChannel(
                sir3s_id=row.Sir3sID, objtype=row.OBJTYPE, name1=row.NAME1, name2=row.NAME2,
                objtype_pk=row.OBJTYPE_PK, attrtype=row.ATTRTYPE, datatype=row.DATATYPE,
                offset=int(row.DATAOFFSET), length=int(row.DATALENGTH), item_length=int(row.DATATYPELENGTH),
            )

        if not os.path.exists(mxs):
            raise FileNotFoundError(f"[mx] .MXS file does not exist: {mxs}")
        stat = os.stat(mxs)
        # Same consistency check as PT3S.Mx: SirCalc writes the .MX1 before the .MXS, so an older .MXS
        # belongs to a previous run (e.g. the last calculation was aborted before writing results).
        if stat.st_mtime < os.path.getmtime(mx1_filepath):
            raise ValueError(f"[mx] {mxs} is older than {mx1_filepath}; the result files belong to different "
                             "calculation runs. Recalculate the model.")
        # SirCalc rewrites the .MX2 in every calculation (after the .MX1, before the .MXS): an .MXS older
        # than it is from an earlier calculation, e.g. left over from other output factors.
        if os.path.exists(mx2) and stat.st_mtime < os.path.getmtime(mx2):
            logger.warning(
                f"[mx] {os.path.basename(mxs)} is older than the most recent calculation ({os.path.basename(mx2)}); "
                "its results are from an earlier calculation. The element lists (.MX2) are from the most recent "
                "one - if the network changed in between, values can be assigned to the wrong elements."
            )
        record_length = int((mx1_df["DATAOFFSET"] + mx1_df["DATALENGTH"]).max())
        n_records, trailing = divmod(stat.st_size, record_length)
        if trailing:
            logger.warning(f"[mx] .MXS size is not a multiple of the record length; ignoring {trailing} trailing byte(s).")

        mx_file = self._MxFile(mx1_path=mx1_filepath, mx2_path=mx2, mxs_path=mxs, mx1_df=mx1_df,
                               record_length=record_length, channels=channels,
                               signature=(stat.st_mtime, stat.st_size), n_records=n_records)
        self._mx_read_record_index(mx_file)
        logger.info(f"[mx] {os.path.basename(mxs)}: {len(channels)} channels, {n_records} records of "
                    f"{record_length:,} bytes ({stat.st_size / 1024**3:.2f} GiB).")
        return mx_file

    def _mx_check_unchanged(self, mx_file: "SIR3S_Model_MX._MxFile") -> None:
        stat = os.stat(mx_file.mxs_path)
        if (stat.st_mtime, stat.st_size) != mx_file.signature:
            raise self._MxFileChangedError(
                f"[mx] {mx_file.mxs_path} changed since it was opened (e.g. a new calculation was started). "
                "Results from before and after the change can't be combined; read again."
            )

    @staticmethod
    def _mx_timestamp_label(raw: str, utc: pd.Timestamp) -> str:
        """
        GetTimeStamps()-style label of a record timestamp. The files store local time with UTC offset
        ("2023-02-13 00:00:00.000000+01:00"); the API shows it as "2023-02-13 00:00:00.000 +01:00".
        Without an offset in the file, the UTC time is labelled with "+00:00".
        """
        match = re.match(r"^(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})(?:\.(\d+))?\s*([+-]\d{2}:\d{2})$", raw)
        if match:
            return f"{match.group(1).replace('T', ' ')}.{(match.group(2) or '0').ljust(3, '0')[:3]} {match.group(3)}"
        if pd.isna(utc):
            return raw
        return f"{utc:%Y-%m-%d %H:%M:%S}.{utc.microsecond // 1000:03d} +00:00"

    def _mx_read_record_index(self, mx_file: "SIR3S_Model_MX._MxFile") -> None:
        """Snapshot type (STAT, TIME, TMIN, TMAX), UTC timestamp and GetTimeStamps()-style label of every
        record, plus the SIR 3S version."""
        allg = {c.attrtype: c for c in mx_file.channels.values() if c.objtype == "ALLG"}
        if "TIMESTAMP" not in allg or "SNAPSHOTTYPE" not in allg:
            raise ValueError("[mx] .MX1 has no ALLG TIMESTAMP/SNAPSHOTTYPE channel.")
        ts_id, st_id = allg["TIMESTAMP"].sir3s_id, allg["SNAPSHOTTYPE"].sir3s_id
        arrays = self._mx_read(mx_file, [ts_id, st_id])
        decode = lambda row: bytes(row).decode("utf-8", errors="replace").strip("\x00 ")
        raw = [decode(row) for row in arrays[ts_id]]
        timestamps = pd.to_datetime(raw, utc=True, errors="coerce")
        mx_file.records = pd.DataFrame({"snapshot_type": [decode(row) for row in arrays[st_id]], "timestamp": timestamps,
                                        "label": [self._mx_timestamp_label(r, t) for r, t in zip(raw, timestamps)]})
        mx_file.records.index.name = "record"
        if "CVERSO" in allg and mx_file.n_records:
            cid = allg["CVERSO"].sir3s_id
            mx_file.version = decode(self._mx_read(mx_file, [cid], records=[0])[cid][0])

    @staticmethod
    def _mx_timeline_records(mx_file: "SIR3S_Model_MX._MxFile") -> np.ndarray:
        """
        Record numbers of the simulation timeline, one per distinct TIMESTAMP in file order. As in
        PT3S.Mx, the first record of a TIMESTAMP wins: the STAT record for the first TIMESTAMP (SIR 3S
        writes STAT and TIME there), the TIME record for the last one (TIME, TMIN, TMAX there). A
        stationary calculation has just its STAT record.
        """
        valid = mx_file.records[mx_file.records["timestamp"].notna()]
        return valid.index[~valid["timestamp"].duplicated(keep="first")].to_numpy()

    def _mx_object_layout(self, mx_file: "SIR3S_Model_MX._MxFile", objtype: str) -> "SIR3S_Model_MX._MxLayout":
        """
        How one element type is laid out: its tk list (.MX2), which properties can be read as scalar
        per-tk values, which interior-point (VEC) properties can be split per tk (needs a matching
        N_OF_POINTS list in .MX2), which only exist for single objects, and which can't be read.
        """
        if objtype in mx_file.layouts:
            return mx_file.layouts[objtype]

        channels = {c.attrtype: c for c in mx_file.channels.values()
                    if c.objtype == objtype and c.is_element_type_channel}
        if channels and mx_file.mx2_df is None:
            mx_file.mx2_df = self._mx_parse_mx2(mx_file.mx2_path)
        mx2 = mx_file.mx2_df if channels else None
        rows = mx2[mx2["ObjType"] == objtype] if mx2 is not None and not mx2.empty else None
        tk_rows = rows[rows["AttrType"].isin(["tk", "pk"])] if rows is not None else None
        tks = [str(tk) for tk in tk_rows.iloc[0]["Data"]] if tk_rows is not None and not tk_rows.empty else []
        if channels and not tks:
            logger.warning(f"[mx] No .MX2 tk list found for OBJTYPE '{objtype}'.")

        layout = self._MxLayout(objtype=objtype, tks=tks)
        len_rows = rows[rows["AttrType"] == "N_OF_POINTS"] if rows is not None else None
        if len_rows is not None and not len_rows.empty and len(len_rows.iloc[0]["Data"]) == len(tks):
            layout.segment_offsets = np.concatenate([[0], np.cumsum(np.asarray(len_rows.iloc[0]["Data"], dtype=np.int64))])

        for prop, channel in channels.items():
            if "VEC" in prop:
                if layout.segment_offsets is not None and channel.n_items == layout.segment_offsets[-1]:
                    layout.vector_channels[prop] = channel
                else:
                    layout.unresolvable_vector_props.append(prop)
            elif tks and channel.n_items == len(tks):
                layout.scalar_channels[prop] = channel
            else:
                logger.warning(f"[mx] Channel '{channel.sir3s_id}' has {channel.n_items} value(s) per record but "
                               f".MX2 lists {len(tks)} '{objtype}' tk(s); skipping this property.")
                layout.skipped_props.append(prop)

        # Like PT3S.Mx, which reads every channel: properties written only for individual objects
        # (OBJTYPE_PK = the object's tk) are read from those channels. Element-type channels take
        # precedence where both exist.
        for channel in mx_file.channels.values():
            if channel.objtype == objtype and not channel.is_element_type_channel and channel.attrtype not in channels:
                if "VEC" not in channel.attrtype and channel.n_items != 1:
                    continue
                layout.single_channels.setdefault(channel.attrtype, {})[channel.objtype_pk] = channel

        mx_file.layouts[objtype] = layout
        return layout

    # --- reading values -------------------------------------------------------------------------

    def _mx_read_plan(self, channels: Sequence["SIR3S_Model_MX._MxChannel"], items: Dict[str, np.ndarray]) -> list:
        """
        Byte spans to read per record and how to copy them into the output arrays. A channel with
        selected items contributes one piece per run of items; pieces (of any channels) closer than
        _MX_SPAN_MERGE_GAP_BYTES are read together, so densely selected items end up as one read of the
        whole block.
        """
        gap = self._MX_SPAN_MERGE_GAP_BYTES
        pieces = []  # (start, end, channel, selection) - selection: None or (dest_from, dest_to, idx)
        for channel in channels:
            sel = items.get(channel.sir3s_id)
            size = channel.item_length
            if sel is None:
                pieces.append((channel.offset, channel.offset + channel.length, channel, None))
                continue
            if len(sel) == 0:
                continue
            breaks = np.flatnonzero(np.diff(sel) * size - size > gap) + 1
            for run in np.split(np.arange(len(sel)), breaks):
                first, last = int(sel[run[0]]), int(sel[run[-1]])
                pieces.append((channel.offset + first * size, channel.offset + (last + 1) * size, channel,
                               (int(run[0]), int(run[-1]) + 1, sel[run] - first)))
        pieces.sort(key=lambda p: p[0])
        spans = []
        for piece in pieces:
            if spans and piece[0] - spans[-1][1] <= gap:
                spans[-1][1] = max(spans[-1][1], piece[1])
                spans[-1][2].append(piece)
            else:
                spans.append([piece[0], piece[1], [piece]])
        return spans

    def _mx_bytes_per_record(self, mx_file: "SIR3S_Model_MX._MxFile", channel_ids: Sequence[str],
                             items: Optional[Dict[str, np.ndarray]] = None) -> int:
        total = 0
        for cid in channel_ids:
            channel = mx_file.channels[cid]
            sel = None if items is None else items.get(cid)
            total += channel.length if sel is None else len(sel) * channel.item_length
        return total

    def _mx_read(
        self,
        mx_file: "SIR3S_Model_MX._MxFile",
        channel_ids: Sequence[str],
        records: Optional[Sequence[int]] = None,
        items: Optional[Dict[str, Optional[np.ndarray]]] = None,
        progress: Optional["SIR3S_Model_MX._MxProgress"] = None,
    ) -> Dict[str, np.ndarray]:
        """
        Read channels for a set of records (default: all), optionally only some items (e.g. tk
        positions) of a channel: {Sir3sID: sorted unique item positions, or None for all}.

        :return: {Sir3sID: array (n_records, n_items or len(items))} - float32/int32 as stored, raw bytes
                 (uint8, item_length bytes per item) for CHAR channels (see _mx_decode_char()).
        """
        missing = [cid for cid in channel_ids if cid not in mx_file.channels]
        if missing:
            raise KeyError(f"[mx] Unknown channel(s): {missing}")
        channels = [mx_file.channels[cid] for cid in channel_ids]
        recs = (np.arange(mx_file.n_records, dtype=np.int64) if records is None
                else np.asarray(records, dtype=np.int64))
        if recs.size and (recs.min() < 0 or recs.max() >= mx_file.n_records):
            raise IndexError(f"[mx] Record numbers must be within 0..{mx_file.n_records - 1}.")
        selected = {}
        for channel in channels:
            sel = None if items is None else items.get(channel.sir3s_id)
            if sel is None:
                continue
            sel = np.asarray(sel, dtype=np.int64)
            if sel.size and (sel.min() < 0 or sel.max() >= channel.n_items or np.any(np.diff(sel) <= 0)):
                raise ValueError(f"[mx] Items of '{channel.sir3s_id}' must be sorted, unique and within "
                                 f"0..{channel.n_items - 1}.")
            selected[channel.sir3s_id] = sel

        out = {}
        for c in channels:
            sel = selected.get(c.sir3s_id)
            if sel is None:
                shape = (len(recs),) + c.row_shape
            else:
                shape = (len(recs), len(sel) * c.item_length) if c.datatype == "CHAR" else (len(recs), len(sel))
            out[c.sir3s_id] = np.empty(shape, dtype=c.dtype)
        if not len(recs) or not channels:
            return out

        spans = self._mx_read_plan(channels, selected)
        buffers = [bytearray(end - start) for start, end, _ in spans]
        with open(mx_file.mxs_path, "rb", buffering=0) as f:
            for i, record in enumerate(recs):
                base = int(record) * mx_file.record_length
                for (start, _end, pieces), buffer in zip(spans, buffers):
                    f.seek(base + start)
                    if f.readinto(buffer) != len(buffer):
                        raise self._MxFileChangedError(
                            f"[mx] Unexpected end of {mx_file.mxs_path} while reading record {record}.")
                    view = memoryview(buffer)
                    for p_start, p_end, channel, selection in pieces:
                        block = np.frombuffer(view[p_start - start:p_end - start], dtype=channel.dtype)
                        target = out[channel.sir3s_id]
                        if selection is None:
                            target[i] = block
                        else:
                            d_from, d_to, idx = selection
                            if channel.datatype == "CHAR":
                                size = channel.item_length
                                target[i, d_from * size:d_to * size] = block.reshape(-1, size)[idx].reshape(-1)
                            else:
                                target[i, d_from:d_to] = block[idx]
                if progress is not None:
                    progress.update()
        self._mx_check_unchanged(mx_file)
        return out

    @staticmethod
    def _mx_decode_char(raw: np.ndarray, channel: "SIR3S_Model_MX._MxChannel",
                        items: Optional[Sequence[int]] = None) -> np.ndarray:
        """Decode CHAR raw bytes into strings, one per item, verbatim (fixed-width padding and null bytes
        are kept - that matches what the SIR 3S Toolkit API returns for the same value)."""
        width = channel.item_length
        positions = range(raw.shape[1] // width) if items is None else items
        out = np.empty((raw.shape[0], len(positions)), dtype=object)
        for r in range(raw.shape[0]):
            row = raw[r].tobytes()
            out[r] = [row[p * width:(p + 1) * width].decode("utf-8", errors="replace") for p in positions]
        return out

    # --- result frames --------------------------------------------------------------------------

    def _mx_frame_bytes_estimate(self, layout: "SIR3S_Model_MX._MxLayout", n_tks: int, props: Sequence[str],
                                 n_rows: int, vec_format: str = "str") -> int:
        """Rough memory estimate of a result frame, for the size check and chunk sizing."""
        item = self._MX_RESULT_DTYPE.itemsize
        per_row = item * n_tks * sum(1 for p in props if p in layout.single_channels)
        avg_points = 0.0
        if layout.segment_offsets is not None and len(layout.tks):
            avg_points = float(layout.segment_offsets[-1]) / len(layout.tks)
        for prop in props:
            if prop in layout.vector_channels:
                per_row += n_tks * (item * avg_points if vec_format == "multiindex" else 8 + 49 + 10 * avg_points)
            elif prop in layout.scalar_channels and layout.scalar_channels[prop].datatype == "CHAR":
                per_row += n_tks * (8 + 49 + layout.scalar_channels[prop].item_length)
            else:
                per_row += n_tks * item
        return int(per_row * n_rows)

    def _mx_check_result_size(self, estimate: int, what: str) -> None:
        available = self._mx_physical_memory()[1]
        if estimate > self._MX_MAX_RESULT_SHARE_OF_AVAILABLE * available:
            raise MemoryError(
                f"[mx] {what} would need about {estimate / 1024**3:,.1f} GiB of memory, but only "
                f"{available / 1024**3:,.1f} GiB are available. Request fewer tks/properties/timestamps or "
                "use vec_format='multiindex' for interior-point properties."
            )

    def _mx_frame_plan(self, layout: "SIR3S_Model_MX._MxLayout", tks: Sequence[str], props: Sequence[str],
                       place_holder_value: float = 99999.0, vec_format: str = "str") -> "SIR3S_Model_MX._MxFramePlan":
        """
        Work out once which file values go to which column of the result frames (one column per
        (tk, property[, interior point]), ordered tk-major / property-minor) and which items of each
        channel the requested tks need, so building each chunk only costs copying values. Only
        properties in layout.readable_props are included.

        vec_format: "str" - interior-point (VEC) values as one tab-separated string per (tk, timestamp),
        formatted like the SIR 3S Toolkit API does; "multiindex" - one float column per interior point,
        with an additional column level "interior points" (scalar properties get -1 there).
        """
        if vec_format not in self._MX_VEC_FORMATS:
            raise ValueError(f"[mx] vec_format must be one of {self._MX_VEC_FORMATS}, got {vec_format!r}.")
        multi = vec_format == "multiindex"
        tks = [str(tk) for tk in tks]
        position = {tk: i for i, tk in enumerate(layout.tks)}
        tk_pos = np.array([position.get(tk, -1) for tk in tks], dtype=np.int64)
        present = tk_pos >= 0
        n_tks = len(tks)
        all_tk_idx = np.arange(n_tks, dtype=np.int64)

        # Items the requested tks need from the element-type channels; the frames are built from arrays
        # holding just these (read with _mx_read(..., items=plan.items)). None = all items.
        present_pos = np.unique(tk_pos[present])
        scalar_items = None if len(present_pos) == len(layout.tks) else present_pos
        tk_pos_r = tk_pos.copy()
        if scalar_items is not None:
            tk_pos_r[present] = np.searchsorted(scalar_items, tk_pos[present])
        vector_items = seg_start_r = seg_len = None
        if layout.segment_offsets is not None:
            offsets = layout.segment_offsets
            safe = np.where(present, tk_pos, 0)
            seg_start, seg_len = offsets[safe], np.where(present, offsets[safe + 1] - offsets[safe], 0)
            if scalar_items is not None:
                starts_u = offsets[present_pos]
                lens_u = offsets[present_pos + 1] - starts_u
                vector_items = (np.repeat(starts_u - np.cumsum(lens_u) + lens_u, lens_u)
                                + np.arange(int(lens_u.sum()), dtype=np.int64))
                seg_start_r = np.where(present, np.searchsorted(vector_items, seg_start), 0)
            else:
                seg_start_r = seg_start

        # One group per property: which values go to which (property-major) column.
        groups, items = [], {}
        col_tk, col_prop, col_point, col_obj = [], [], [], []

        def add_group(kind, prop_idx, tk_idx, points, is_obj, **info):
            groups.append(dict(kind=kind, start=sum(len(a) for a in col_tk), n=len(tk_idx), is_obj=is_obj, **info))
            col_tk.append(np.asarray(tk_idx, dtype=np.int64))
            col_prop.append(np.full(len(tk_idx), prop_idx, dtype=np.int64))
            col_point.append(np.asarray(points, dtype=np.int64))
            col_obj.append(np.full(len(tk_idx), is_obj, dtype=bool))

        scalar_point = np.full(n_tks, -1, dtype=np.int64)
        for prop_idx, prop in enumerate(props):
            if prop in layout.scalar_channels:
                channel = layout.scalar_channels[prop]
                identity = bool(present.all()) and np.array_equal(tk_pos, np.arange(len(layout.tks)))
                items[channel.sir3s_id] = scalar_items
                add_group("scalar", prop_idx, all_tk_idx, scalar_point, channel.datatype == "CHAR",
                          channel=channel, tk_pos=tk_pos_r, present=present, identity=identity)

            elif prop in layout.vector_channels:
                channel = layout.vector_channels[prop]
                items[channel.sir3s_id] = vector_items
                if multi:
                    counts = np.where(present, seg_len, 1)
                    tk_idx = np.repeat(all_tk_idx, counts)
                    points = np.arange(len(tk_idx), dtype=np.int64) - np.repeat(np.cumsum(counts) - counts, counts)
                    first = np.repeat(np.where(present, seg_start_r, -1), counts)
                    gather = np.where(first >= 0, first + points, -1)
                    add_group("vector_multi", prop_idx, tk_idx, points, False, channel=channel, gather=gather)
                else:
                    add_group("vector_str", prop_idx, all_tk_idx, scalar_point, True, channel=channel,
                              present=present, seg_start=seg_start_r, seg_end=seg_start_r + seg_len)

            elif prop in layout.single_channels:
                by_tk = layout.single_channels[prop]
                channels = [by_tk.get(tk) for tk in tks]
                if "VEC" in prop and multi:
                    counts = np.array([c.n_items if c is not None else 1 for c in channels], dtype=np.int64)
                    tk_idx = np.repeat(all_tk_idx, counts)
                    points = np.arange(len(tk_idx), dtype=np.int64) - np.repeat(np.cumsum(counts) - counts, counts)
                    add_group("single_vector_multi", prop_idx, tk_idx, points, False, channels=channels, counts=counts)
                elif "VEC" in prop:
                    add_group("single_vector_str", prop_idx, all_tk_idx, scalar_point, True, channels=channels)
                else:
                    is_char = any(c is not None and c.datatype == "CHAR" for c in channels)
                    add_group("single_scalar", prop_idx, all_tk_idx, scalar_point, is_char, channels=channels)

        cat = lambda parts, dtype: np.concatenate(parts) if parts else np.array([], dtype=dtype)
        col_tk, col_prop = cat(col_tk, np.int64), cat(col_prop, np.int64)
        col_point, col_obj = cat(col_point, np.int64), cat(col_obj, bool)
        n_cols = len(col_tk)

        # Final (tk-major) column order. Numeric and object columns are filled into two arrays (each in
        # final order); dest is the column of each property-major column within its array.
        order = np.lexsort((col_point, col_prop, col_tk))
        final_pos = np.empty(n_cols, dtype=np.int64)
        final_pos[order] = np.arange(n_cols, dtype=np.int64)
        obj_final = col_obj[order]
        rank_in_kind = np.empty(n_cols, dtype=np.int64)
        rank_in_kind[~obj_final] = np.arange(int((~obj_final).sum()))
        rank_in_kind[obj_final] = np.arange(int(obj_final.sum()))

        tk_level = pd.Index(tks).unique()
        prop_level = pd.Index(list(props)).unique()
        empty = np.array([], dtype=np.int64)
        tk_codes = tk_level.get_indexer(np.array(tks, dtype=object))[col_tk[order]] if n_cols else empty
        prop_codes = prop_level.get_indexer(np.array(list(props), dtype=object))[col_prop[order]] if n_cols else empty
        if multi:
            point_level = np.unique(col_point) if n_cols else empty
            columns = pd.MultiIndex(levels=[tk_level, prop_level, pd.Index(point_level)],
                                    codes=[tk_codes, prop_codes, np.searchsorted(point_level, col_point[order])],
                                    names=["tk", "property", "interior points"], verify_integrity=False)
        else:
            columns = pd.MultiIndex(levels=[tk_level, prop_level], codes=[tk_codes, prop_codes],
                                    names=["tk", "property"], verify_integrity=False)

        plan = self._MxFramePlan(layout=layout, place_holder_value=place_holder_value, groups=groups, items=items,
                                 dest=rank_in_kind[final_pos], n_float=int((~obj_final).sum()),
                                 n_obj=int(obj_final.sum()), columns=columns)
        if plan.n_obj:
            plan.float_columns = columns[~obj_final]
            plan.obj_columns = columns[obj_final]
            # position in [numeric columns..., object columns...] of each final column
            plan.restore = np.where(obj_final, plan.n_float + rank_in_kind, rank_in_kind)
        return plan

    def _mx_fill_frame(self, plan: "SIR3S_Model_MX._MxFramePlan", arrays: Dict[str, np.ndarray],
                       num: np.ndarray, obj: Optional[np.ndarray]) -> None:
        """Write arrays read with _mx_read(..., items=plan.items) into num/obj (one row per array row,
        columns as in plan). Numeric values as float32, CHAR values and VEC strings (vec_format="str") as str."""
        ph = plan.place_holder_value
        as_indexer = self._mx_as_indexer

        for g in plan.groups:
            dest = plan.dest[g["start"]:g["start"] + g["n"]]
            kind = g["kind"]
            if kind == "scalar":
                channel, present, tk_pos = g["channel"], g["present"], g["tk_pos"]
                if channel.datatype == "CHAR":
                    obj[:, dest] = ph
                    if present.any():
                        obj[:, dest[present]] = self._mx_decode_char(arrays[channel.sir3s_id], channel, tk_pos[present])
                else:
                    values = arrays[channel.sir3s_id]
                    if g["identity"]:
                        num[:, as_indexer(dest)] = values
                    else:
                        num[:, as_indexer(dest[present])] = values[:, tk_pos[present]]
                        num[:, dest[~present]] = ph

            elif kind == "vector_multi":
                gather = g["gather"]
                ok = gather >= 0
                num[:, as_indexer(dest[ok])] = arrays[g["channel"].sir3s_id][:, gather[ok]]
                num[:, dest[~ok]] = ph

            elif kind == "vector_str":
                strings = self._mx_format_floats(arrays[g["channel"].sir3s_id])
                for d, s0, s1, ok in zip(dest, g["seg_start"], g["seg_end"], g["present"]):
                    obj[:, d] = ["\t".join(row) for row in strings[:, s0:s1].tolist()] if ok else ph

            elif kind == "single_scalar":
                target = obj if g["is_obj"] else num
                for d, channel in zip(dest, g["channels"]):
                    if channel is None:
                        target[:, d] = ph
                    elif channel.datatype == "CHAR":
                        target[:, d] = self._mx_decode_char(arrays[channel.sir3s_id], channel)[:, 0]
                    else:
                        target[:, d] = arrays[channel.sir3s_id][:, 0]

            elif kind == "single_vector_multi":
                pos = 0
                for channel, count in zip(g["channels"], g["counts"]):
                    num[:, dest[pos:pos + count]] = arrays[channel.sir3s_id] if channel is not None else ph
                    pos += count

            elif kind == "single_vector_str":
                for d, channel in zip(dest, g["channels"]):
                    obj[:, d] = (["\t".join(row) for row in self._mx_format_floats(arrays[channel.sir3s_id]).tolist()]
                                 if channel is not None else ph)

        if not np.isnan(ph):
            np.copyto(num, ph, where=np.isnan(num))

    @staticmethod
    def _mx_placeholder_columns(values: np.ndarray, place_holder_value: float, rows_per_block: int = 64) -> np.ndarray:
        """Per column: True if every value is place_holder_value (checked in row blocks, so the
        comparison never needs a full-size temporary array)."""
        full = np.ones(values.shape[1], dtype=bool)
        is_nan = isinstance(place_holder_value, float) and np.isnan(place_holder_value)
        for start in range(0, values.shape[0], rows_per_block):
            block = values[start:start + rows_per_block]
            if values.dtype == object:
                full &= np.array([all(v == place_holder_value for v in col) for col in block.T], dtype=bool)
            else:
                full &= (np.isnan(block) if is_nan else block == place_holder_value).all(axis=0)
        return full

    @staticmethod
    def _mx_keep_columns(values: np.ndarray, keep: np.ndarray, rows_per_block: int = 64) -> np.ndarray:
        """values[:, keep] without a full-size copy: the kept columns are moved to the front of the same
        array, block of rows by block of rows; returns a view of them."""
        kept = np.flatnonzero(keep)
        for start in range(0, values.shape[0], rows_per_block):
            rows = slice(start, start + rows_per_block)
            values[rows, :len(kept)] = values[rows][:, kept]
        return values[:, :len(kept)]

    def _mx_read_frame(
        self,
        mx_file: "SIR3S_Model_MX._MxFile",
        layout: "SIR3S_Model_MX._MxLayout",
        tks: Sequence[str],
        props: Sequence[str],
        records: Sequence[Optional[int]],
        labels: Sequence,
        place_holder_value: float,
        vec_format: str,
        max_chunk_bytes: int,
        drop_full_place_holder_columns: bool = False,
    ) -> Tuple[pd.DataFrame, int]:
        """
        Result frame of one element type (only properties readable from the files), one row per record
        (labels as index). Rows whose record is None (timestamp not in the file) get place_holder_value.
        The result arrays are allocated once and filled chunk by chunk (raw arrays of at most
        max_chunk_bytes per chunk), so the peak memory is about the result plus one chunk.

        :return: (frame, number of dropped full-placeholder columns)
        """
        channel_ids = layout.channel_ids(props)
        plan = self._mx_frame_plan(layout, tks, props, place_holder_value=place_holder_value, vec_format=vec_format)
        ph = plan.place_holder_value
        n_rows = len(records)
        num = np.empty((n_rows, plan.n_float), dtype=self._MX_RESULT_DTYPE)
        obj = np.empty((n_rows, plan.n_obj), dtype=object) if plan.n_obj else None

        read_per_record = self._mx_bytes_per_record(mx_file, channel_ids, plan.items)
        rows_per_chunk = max(1, int(max_chunk_bytes // max(1, read_per_record)))
        n_known = sum(1 for r in records if r is not None)
        label = f"[mx] Reading {len(channel_ids)} channel(s) of '{layout.objtype}'"
        progress = self._MxProgress(logger, label, n_known, "records",
                                    enabled=read_per_record * n_known >= self._MX_PROGRESS_LOG_MIN_BYTES)
        if progress.enabled:
            logger.info(f"{label}: {n_known:,} records, {read_per_record * n_known / 1024**2:,.0f} MiB ...")
        for start in range(0, n_rows, rows_per_chunk):
            stop = min(start + rows_per_chunk, n_rows)
            known = [i for i in range(start, stop) if records[i] is not None]
            if len(known) < stop - start:  # timestamps not in the file
                missing = [i for i in range(start, stop) if records[i] is None]
                num[missing] = ph
                if obj is not None:
                    obj[missing] = ph
            if not known:
                continue
            arrays = self._mx_read(mx_file, channel_ids, [records[i] for i in known], items=plan.items, progress=progress)
            if len(known) == stop - start:
                self._mx_fill_frame(plan, arrays, num[start:stop], obj[start:stop] if obj is not None else None)
            else:
                part_num = np.empty((len(known), plan.n_float), dtype=self._MX_RESULT_DTYPE)
                part_obj = np.empty((len(known), plan.n_obj), dtype=object) if obj is not None else None
                self._mx_fill_frame(plan, arrays, part_num, part_obj)
                num[known] = part_num
                if obj is not None:
                    obj[known] = part_obj

        columns, float_columns, obj_columns, restore = plan.columns, plan.float_columns, plan.obj_columns, plan.restore
        dropped = 0
        if drop_full_place_holder_columns and n_rows:
            keep_f = ~self._mx_placeholder_columns(num, ph)
            keep_o = ~self._mx_placeholder_columns(obj, ph) if obj is not None else np.zeros(0, dtype=bool)
            dropped = int((~keep_f).sum() + (~keep_o).sum())
            if dropped:
                if obj is None:
                    columns = columns[keep_f]
                else:
                    keep_final = np.concatenate([keep_f, keep_o])[restore]
                    columns = columns[keep_final]
                    float_columns, obj_columns = float_columns[keep_f], obj_columns[keep_o]
                    rank = np.cumsum(np.concatenate([keep_f, keep_o])) - 1  # position among the kept ones
                    restore = rank[restore[keep_final]]
                    obj = self._mx_keep_columns(obj, keep_o)
                num = self._mx_keep_columns(num, keep_f)

        if obj is None:
            return pd.DataFrame(num, index=labels, columns=columns, copy=False), dropped
        df = pd.concat([pd.DataFrame(num, index=labels, columns=float_columns, copy=False),
                        pd.DataFrame(obj, index=labels, columns=obj_columns, copy=False)], axis=1)
        return df.iloc[:, restore], dropped

    def _mx_read_results(
        self,
        element_type: Union[Enum, str],
        properties: Optional[List[str]] = None,
        tks: Optional[List[str]] = None,
        timestamps: Optional[List[Union[str, pd.Timestamp]]] = None,
        snapshot_types: Optional[List[str]] = None,
        mx1_filepath: Optional[str] = None,
        place_holder_value: float = np.nan,
        vec_format: str = "multiindex",
    ) -> pd.DataFrame:
        """
        Result values of one element type straight from the result files, without the SIR 3S Toolkit
        API (also for result files of a model that isn't open) and for any record, including the STAT,
        TMIN and TMAX snapshots. For checks/diagnostics; users go through
        generate_element_results_dataframe(bulk=True).

        :return: Index (snapshot_type, timestamp); columns (tk, property[, interior points]).
        """
        mx_file = self._mx_get_file(mx1_filepath)
        layout = self._mx_object_layout(mx_file, self._mx_objtype(element_type))
        readable = layout.readable_props
        if properties is None:
            props = sorted(readable)
        else:
            props = [p for p in properties if p in readable]
            skipped = [p for p in properties if p not in readable]
            if skipped:
                logger.warning(f"[mx] Not readable from the result files for OBJTYPE '{layout.objtype}': {skipped}")
        if tks is None:
            use_tks = list(layout.tks)
            known = set(use_tks)
            for prop in props:
                for tk in layout.single_channels.get(prop, {}):
                    if tk not in known:
                        use_tks.append(tk)
                        known.add(tk)
        else:
            use_tks = [str(tk) for tk in tks]

        selected = mx_file.records
        if snapshot_types is not None:
            selected = selected[selected["snapshot_type"].isin([s.upper() for s in snapshot_types])]
        if timestamps is not None:
            selected = selected[selected["timestamp"].isin(pd.to_datetime(list(timestamps), utc=True))]
        records = selected.index.tolist()
        labels = list(zip(selected["snapshot_type"], selected["timestamp"]))

        estimate = self._mx_frame_bytes_estimate(layout, len(use_tks), props, len(records), vec_format)
        self._mx_check_result_size(estimate, "The requested results")
        df, _ = self._mx_read_frame(mx_file, layout, use_tks, props, records, labels,
                                    place_holder_value, vec_format, max_chunk_bytes=self._MX_MAX_CHUNK_BYTES)
        df.index = pd.MultiIndex.from_tuples(labels, names=["snapshot_type", "timestamp"]) if labels else \
            pd.MultiIndex.from_tuples([], names=["snapshot_type", "timestamp"])
        return self._mx_order_columns(df, use_tks, props)
