# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 09:22:31 2025

This module implements interactions between SIR 3S and pandas dataframes. You can obtain pandas dfs with model- or resultdata, insert nodes and pipes via a df, etc.

AI assistant: see sir3stoolkit/__init__.py for orientation (architecture, API/property reference,
known gotchas) before writing code against this module.

@author: Jablonski
"""
from __future__ import annotations

import re
import logging
import sys
import os
import struct
import tempfile
import shutil
import json
import io
import zipfile
import xml.etree.ElementTree as ET
from decimal import Decimal, Context, ROUND_HALF_UP
from dataclasses import dataclass, field
from typing import List, Optional, Union
from enum import Enum
from typing import List, Tuple, Any, Set
from enum import Enum
from collections import defaultdict
from datetime import datetime

from sir3stoolkit.dependency_check import require_packages
# pyarrow backs the on-disk MX results cache (_write_mx_cache_file()/_read_mx_cache_file()) - only
# ever imported lazily, inside those functions, so it isn't a hard requirement for the rest of this
# module - but it IS a real requirement of this module, so it's checked here too rather than only
# surfacing as a raw ModuleNotFoundError deep inside a cache read/write much later.
require_packages(__name__, "attrs", "pytoolconfig", "pandas", "geopandas", "shapely", "pyarrow")

from attrs import field
from pytoolconfig import dataclass
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely import wkt

from sir3stoolkit.logging_utils import get_logger
from sir3stoolkit.mantle.advanced_operations import mapping_for_groups

logger = get_logger(__name__)

from sir3stoolkit.core.wrapper import SIR3S_Model

# Sentinel for "Tier 1 MX results cache has never been loaded this session" (distinct from None, which
# means "the live/default cache").
_MX_CACHE_NOT_LOADED = object()

# MX1 DATATYPEs this module knows how to unpack.
_KNOWN_MX_DATATYPES = {"CHAR", "INT4", "REAL", "RVEC"}
_KNOWN_MX_NUMERIC_DATATYPES = {"INT4", "REAL"}

# SIR 3S formats result values as 7-significant-digit, upper-case-E strings, with ties rounded
# away from zero (Python's default rounds ties to even) - this context reproduces that.
_SIR3S_FLOAT_FORMAT_CTX = Context(prec=7, rounding=ROUND_HALF_UP)


def _format_sir3s_float(value: float) -> str:
    """Format a float the same way SIR 3S itself formats result values: 7 significant digits,
    upper-case scientific notation for very small/large magnitudes, ties rounded away from zero."""
    if value == 0.0:
        return "0"
    rounded = _SIR3S_FLOAT_FORMAT_CTX.create_decimal(Decimal(value))
    return "{:.7G}".format(float(rounded))


class SIR3S_Model_Dataframes(SIR3S_Model):
    """
    This class is supposed to extend the general SIR3S_Model class with the possibility of using pandas dataframes when working with SIR 3S. Getting dataframes, inserting elements via dataframes, running algorithms on dataframes should be made possible.
    """

    # Dataframe Creation

    ## Dataframe Creation: Basic Functions

    def generate_element_model_data_dataframe(
        self,
        element_type: Enum,
        tks: Optional[List[str]] = None,
        properties: Optional[List[str]] = None,
        geometry: Optional[bool] = False,
        end_nodes: Optional[bool] = False,
        element_type_col: Optional[bool] = False,
        resolve_references: Optional[bool] = False
    ) -> pd.DataFrame | gpd.GeoDataFrame:

        """
        Generate a dataframe with model data (static) properties for all devices of a given element type.

        :param element_type: The element type (e.g., self.ObjectTypes.Node).
        :type element_type: Enum
        :param tks: List of tks of instances of the element type to include. All other tks will be excluded. Use for filtering.
                    Default: None (no filtering)
        :type tks: list[str], optional
        :param properties: List of model data property names to include.  
                        If properties=None ⇒ all available properties are used.  
                        If properties=[] ⇒ no properties are used.
                        Default: None.
        :type properties: list[str], optional
        :param geometry: If True, includes geometric information for each element in the dataframe.  
                        Adds a 'geometry' column containing spatial data (WKT representation, e.g. POINT (x y)).  
                        An attempt will be made to transform the Dataframe into a GeoDataFrame. The success depends on whether an SRID is defined in the SIR 3S model.
                        Default: False.
        :type geometry: bool, optional
        :param end_nodes: If True and supported by the element type, includes tks of end nodes as columns  
                        (fkKI, fkKK, fkKI2, fkKK2).
                        Default: False.
        :type end_nodes: bool, optional
        :param element_type_col: If True, adds a column indicating the element type.  
                                Useful when merging dataframes later.
                                Default: False.
        :type element_type_col: bool, optional
        :param resolve_references: Determine whether references to tables such as Nominal Diameter Tables (Nennweitentabelle) should be resolved or left just as a reference. WORK IN PROGRESS. Works just for Nominal Diameter Tables for Pipes.
                        Default:  False
        :type resolve_references: bool, optional
        
        :return: DataFrame (or GeoDataFrame) with one row per device (tk) and columns for the requested model data properties,  
                geometry and end nodes.  
                Columns: ["tk", <model_data_props>]
        :rtype: pd.DataFrame | gpd.GeoDataFrame

        :description:  
        Generates a DataFrame (or GeoDataFrame) containing static model data for all elements of a given type. The core of the sir3stoolkit usually returns values without datatypes, that are then interpreted as strings. This function infers and assigns datatypes based on values, therefore misassignments of data types can happen. Tk retains string data type. Vectorized values are split into three columsn property_start, property_end, property_sequence(closed interval including start and end).
        """

        logger.info(f"[model_data] Generating model_data dataframe for element type: {element_type}")

        # --- Collect device keys (tks) ---
        try:
            available_tks = self.GetTksofElementType(ElementType=element_type)
        except Exception as e:
            logger.error(f"[model_data] Error retrieving element tks: {e}")
            return pd.DataFrame()
        
        if len(available_tks) < 1:
            logger.warning(f"[model_data] No elements exist of this element type {element_type}.")
            return pd.DataFrame()
        
        # --- Resolve tks ---
        if tks:
            tks=self.__resolve_given_tks(element_type=element_type, tks=tks, filter_container_tks=None)
            if len(tks) < 1:
                return pd.DataFrame()
        else:
            tks=available_tks
            logger.info(f"[model_data] Retrieved {len(available_tks)} element(s) of element type {element_type}.")
          
        # --- Resolve given model_data properties ---
        model_data_props = self.__resolve_given_model_data_properties(element_type=element_type, properties=properties)

        # --- Retrieve values ---
        to_retrieve = []
        if model_data_props != []:
            to_retrieve.append(f"model_data properties {model_data_props}")
        if geometry:
            to_retrieve.append("geometry")
        if end_nodes:
            to_retrieve.append("end nodes")
            
        logger.info(f"[model_data] Retrieving {', '.join(to_retrieve)}...")
        
        rows = []

        end_nodes_available = False
        if end_nodes:
            if self.__is_get_endnodes_applicable(element_type=element_type):
                end_nodes_available = True
            else:
                logger.warning(f"[model_data] End nodes are not defined for element type {element_type}. Dataframe is created without end nodes.")
            
        for tk in tks:
            
            row = {"tk": tk}
            
            # Add model_data properties
            for prop in model_data_props:
                try:
                    row[prop] = self.GetValue(Tk=tk, propertyName=prop)[0]
                except Exception as e:
                    logger.warning(f"[model_data] Failed to get property '{prop}' for tk '{tk}': {e}")
            
            # Add geometry if requested
            if geometry:
                try:
                    row["geometry"] = self.GetGeometryInformation(Tk=tk)
                except Exception as e:
                    logger.warning(f"[model_data] Failed to get geometry information for tk '{tk}': {e}")
            
            # Add end nodes if requested
            if end_nodes_available:
                try:
                    endnode_tuple = self.GetEndNodes(Tk=tk) 
                    row["fkKI"], row["fkKK"], row["fkKI2"], row["fkKK2"] = endnode_tuple
                except Exception as e:
                    logger.warning(f"[model_data] Failed to get end nodes for tk '{tk}': {e}")
            
             # Add element type col if requested
            if element_type_col:
                row["element type"] = str(element_type).split(".")[-1]

            rows.append(row)

        # --- Endnodes Post Processing ---
        if end_nodes_available:
            endnode_cols = ["fkKI", "fkKK", "fkKI2", "fkKK2"]
            used_cols = []

            for col in endnode_cols:
                if any(row.get(col, "-1") != "-1" for row in rows):
                    used_cols.append(col)
                else:
                    for row in rows:
                        row.pop(col, None)

            logger.info(f"[model_data] {len(used_cols)} non-empty end node columns were created.")

        # --- Dataframe creation ---
        df = pd.DataFrame(rows)

        # --- WORK IN PROGRESS: Post Processing: resolve refernces to tables ---
        if element_type.name == "Pipe" and resolve_references:
            df_v, _, _ = self.get_dataframes_from_nominal_diameter_tables()
            join_key = "tk_merge"
            df_v = df_v.rename(columns={
                col: f"PipeTable: {col}"
                for col in df_v.columns if col != join_key
            })
            df = df.merge(df_v, left_on="FkdtroRowd", right_on=join_key, how="left")
            df = df.drop(columns=["tk_merge"])

        # --- Post Processing: data types ---
        re_int       = re.compile(r"^[+-]?\d+$")        # 13
        re_float_dot = re.compile(r"^[+-]?\d+\.\d+$")   # 1.3
        re_float_com = re.compile(r"^[+-]?\d+,\d+$")    # 1,3

        for col in df.columns:
            # Skip geometry
            if col == "geometry":
                continue

            # tk → string
            if col == "tk":
                df[col] = df[col].astype("string")
                continue

            s = df[col]

            # Build masks
            non_null = ~s.isna()
            s_str = s.astype("string").str.strip()

            m_int       = s_str.str.fullmatch(re_int.pattern, na=False)
            m_float_dot = s_str.str.fullmatch(re_float_dot.pattern, na=False)
            m_float_com = s_str.str.fullmatch(re_float_com.pattern, na=False)

            valid = m_int | m_float_dot | m_float_com

            # Enforce: each non-null must match one of the three regexes
            if (valid[non_null]).all():
                # Convert per value
                out = []
                for val in s_str:
                    if pd.isna(val):
                        out.append(pd.NA)
                    elif re_int.fullmatch(val):
                        out.append(int(val))
                    elif re_float_dot.fullmatch(val):
                        out.append(float(val))
                    elif re_float_com.fullmatch(val):
                        out.append(float(val.replace(",", ".")))
                    else:
                        out.append(val)
                df[col] = pd.Series(out)
            else:
                df[col] = s_str

        # Transform to gpd ---
        if geometry:
            try:
                df["geometry"] = df["geometry"].apply(wkt.loads)
                srid, srid2, srid_string = self.get_EPSG()
                if srid and (srid != '0'):
                    df = gpd.GeoDataFrame(df, geometry="geometry", crs=f"EPSG: {srid}")
                    logger.info(f"[model_data] Transforming DataFrame to GeoDataFrame successful with EPSG: {srid}")
                else:
                    logger.warning(f"[model_data] Spatial Reference Identifier (SRID) not defined in model. DataFrame cannot be transformed to GeoDataFrame but geometry column can be created independently of SRID. Returning regular DataFrame with a geometry column.")
            except Exception as e:
                    logger.error(f"[model_data] Error transforming DataFrame to GeoDataFrame. {e}")

        logger.info(f"[model_data] Done. Shape: {df.shape}")
        return df

    ## Dataframe Creation: Bulk (MX-based) results cache, used by generate_element_results_dataframe(bulk=True)

    def _get_mx_raw_results_cache(self, cache_suffix: Optional[str] = None) -> pd.DataFrame:
        """
        Tier 1 of the bulk-results cache: the raw MX results dataframe (read_mx_results()'s shape),
        refreshed when the underlying .MXS file has changed. Tries an on-disk cache ("mxcache.zip" next
        to the .MX1 file) before falling back to a full read_mx_results() re-scan, and writes a fresh
        on-disk cache afterward. Holds exactly one calculation's results at a time; Tier 2 (the
        per-element-type caches) is cleared whenever this refreshes.

        :param cache_suffix: None (default) for the live cache. A name to instead load a specific
                        archived snapshot ("mxcache.<cache_suffix>.zip") unconditionally, without
                        checking it against the live .MXS - raises FileNotFoundError if that file
                        doesn't exist; it's never created automatically, only by manually
                        copying/renaming a previously-written default cache file. See
                        generate_element_results_dataframe()'s mx_cache_suffix param.
        :type cache_suffix: Optional[str]
        :return: The cached (or freshly read/loaded) raw MX results dataframe.
        :rtype: pd.DataFrame
        """
        cached_suffix = getattr(self, "_mx_results_cache_suffix", _MX_CACHE_NOT_LOADED)

        mx1_filepath = self.get_current_mx1_filepath(dot_resolution=1)
        mx_paths = self._resolve_mx_file_paths(mx1_filepath)
        mxs_filepath = mx_paths["mxs"]

        def _load_new_snapshot(raw_df: pd.DataFrame, suffix: Optional[str]) -> pd.DataFrame:
            self._mx_results_cache_raw = raw_df
            self._mx_results_cache_suffix = suffix
            self._mx_results_cache_by_element_type = {}
            self._mx_results_cache_vector_by_element_type = {}
            return raw_df

        if cache_suffix is not None:
            if cached_suffix == cache_suffix:
                logger.info(f"[bulk results] In-memory Tier 1 cache already holds archived snapshot {cache_suffix!r}; reusing.")
                return self._mx_results_cache_raw

            disk_path = self._mx_cache_filepath(mx_paths, cache_suffix)
            if not os.path.exists(disk_path):
                default_path = self._mx_cache_filepath(mx_paths, None)
                raise FileNotFoundError(
                    f"[bulk results] No on-disk Tier 1 cache found for archived snapshot mx_cache_suffix={cache_suffix!r}: "
                    f"{disk_path!r} does not exist. This file is never created automatically - copy/rename "
                    f"a previously-written default on-disk cache file ({default_path!r}) to this name first."
                )
            logger.info(f"[bulk results] Loading on-disk Tier 1 cache for archived snapshot (suffix={cache_suffix!r}): {disk_path}")
            raw_df, mx1_df, mx2_df, _signature = self._read_mx_cache_file(disk_path)
            self._apply_mx1_mx2(mx_paths, mx1_df, mx2_df)
            logger.info(f"[bulk results] Loaded archived snapshot into the in-memory Tier 1 cache. Shape: {raw_df.shape}")
            return _load_new_snapshot(raw_df, cache_suffix)

        # cache_suffix is None: the live/default cache.
        needs_refresh = True
        current_stat = None
        if cached_suffix is None and os.path.exists(mxs_filepath):
            current_stat = os.stat(mxs_filepath)
            current_signature = (current_stat.st_mtime, current_stat.st_size)
            if current_signature == getattr(self, "_mx_results_cache_signature", None):
                needs_refresh = False

        if not needs_refresh:
            logger.info("[bulk results] In-memory Tier 1 cache is fresh; reusing.")
            return self._mx_results_cache_raw

        disk_path = self._mx_cache_filepath(mx_paths, None)
        raw_df = None
        if os.path.exists(mxs_filepath):
            if current_stat is None:
                current_stat = os.stat(mxs_filepath)
            current_signature = (current_stat.st_mtime, current_stat.st_size)

            if os.path.exists(disk_path):
                try:
                    disk_raw_df, disk_mx1_df, disk_mx2_df, disk_signature = self._read_mx_cache_file(disk_path)
                    if disk_signature == current_signature:
                        logger.info(f"[bulk results] In-memory Tier 1 cache stale/missing; loaded fresh on-disk Tier 1 cache instead of re-scanning .MXS: {disk_path}")
                        raw_df = disk_raw_df
                        self._apply_mx1_mx2(mx_paths, disk_mx1_df, disk_mx2_df)
                    else:
                        logger.info("[bulk results] On-disk Tier 1 cache is stale (signature mismatch); ignoring it.")
                except Exception as e:
                    logger.warning(f"[bulk results] Failed to read on-disk Tier 1 cache ({disk_path}), ignoring it: {e}")

        if raw_df is None:
            logger.info("[bulk results] In-memory and on-disk Tier 1 caches both stale or missing; refreshing via read_mx_results() ...")
            raw_df = self.read_mx_results()
            current_stat = os.stat(mxs_filepath)
            current_signature = (current_stat.st_mtime, current_stat.st_size)
            try:
                self._write_mx_cache_file(disk_path, raw_df, self._mx1_df, self._mx2_df, current_signature)
                logger.info(f"[bulk results] Wrote on-disk Tier 1 cache: {disk_path}")
            except Exception as e:
                logger.warning(f"[bulk results] Failed to write on-disk Tier 1 cache ({disk_path}), continuing without it: {e}")

        self._mx_results_cache_signature = current_signature
        logger.info(f"[bulk results] In-memory Tier 1 cache refreshed. Shape: {raw_df.shape}")
        return _load_new_snapshot(raw_df, None)

    def _get_available_mx_channel_props_for_element_type(
        self, element_type: Enum, cache_suffix: Optional[str] = None
    ) -> Optional[Set[str]]:
        """
        Which result properties actually have an MX1 channel for this element type in the current
        calculation run - i.e. were actually selected/archived, as opposed to merely being part of the
        theoretical schema GetResultProperties_from_elementType() returns. Covers both scalar and VEC-named (interior-point) properties alike.
        
        :param element_type: The element type (e.g., self.ObjectTypes.Pipe).
        :type element_type: Enum
        :param cache_suffix: Forwarded to _get_mx_raw_results_cache() - None for the live cache, or a
                        name to check against a specific archived snapshot instead.
        :type cache_suffix: Optional[str]
        :return: Set of property names (without the "OBJTYPE~*~*~*~" prefix) that have an MX1 channel
                        for this element type, or None if this element type has no known OBJTYPE mapping
                        (mapping_for_groups) - callers should treat None as "unknown, don't filter".
        :rtype: Optional[Set[str]]
        """
        object_type_code = mapping_for_groups.get(element_type.name)
        if not object_type_code or object_type_code == -1:
            return None

        raw_df = self._get_mx_raw_results_cache(cache_suffix=cache_suffix)
        prefix = f"{object_type_code}~*~*~*~"
        return {col[len(prefix):] for col in raw_df.columns if col.startswith(prefix)}

    def _get_mx_scalar_results_for_element_type(
        self, element_type: Enum, cache_suffix: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Tier 2 of the bulk-results cache: for one element type, all scalar (non-VEC) result
        properties resolved down to individual tks, built lazily and cached in
        self._mx_results_cache_by_element_type. VEC-named (interior-point) channels are resolved
        separately, see _get_mx_vector_results_for_element_type().

        :param element_type: The element type (e.g., self.ObjectTypes.Pipe).
        :type element_type: Enum
        :param cache_suffix: Forwarded to _get_mx_raw_results_cache() - None for the live cache, or a
                        name to resolve against a specific archived snapshot instead.
        :type cache_suffix: Optional[str]
        :return: DataFrame with one row per UTC timestamp (matching Tier 1's index) and MultiIndex
                        columns [(tk, property)], scalar (non-VEC) result properties only.
        :rtype: pd.DataFrame
        """
        raw_df = self._get_mx_raw_results_cache(cache_suffix=cache_suffix)

        cache = getattr(self, "_mx_results_cache_by_element_type", None)
        if cache is None:
            cache = {}
            self._mx_results_cache_by_element_type = cache

        element_type_name = element_type.name
        if element_type_name in cache:
            return cache[element_type_name]

        object_type_code = mapping_for_groups.get(element_type_name)
        if not object_type_code or object_type_code == -1:
            raise ValueError(
                f"[bulk results] No MX OBJTYPE code known for element type '{element_type_name}'; "
                "bulk=True is not supported for this element type. Use bulk=False instead."
            )

        mx2_tk_rows = self._mx2_df[
            (self._mx2_df["ObjType"].str.strip() == object_type_code)
            & (self._mx2_df["AttrType"].str.strip().isin(["tk", "pk"]))
        ]
        if mx2_tk_rows.empty:
            logger.warning(f"[bulk results] No .MX2 tk list found for OBJTYPE '{object_type_code}'.")
            cache[element_type_name] = pd.DataFrame(index=raw_df.index)
            return cache[element_type_name]
        mx2_tks = list(mx2_tk_rows.iloc[0]["Data"])

        # Most non-VEC result channels are numeric (REAL/INT4), but not all of them are - some are CHAR
        # (e.g. a status/text-valued property). read_mx_results() leaves CHAR scalar values as raw bytes
        # (unlike MX2's CHAR arrays, which it decodes) - decoded (verbatim, see below) below instead, so
        # this Tier 2 cache never has to guess a column's type from its values the way a blind
        # DataFrame-wide .astype(float) downstream used to (that failed *all* properties at once the
        # moment any one column turned out to be text - see generate_element_results_dataframe()).
        mx1_datatype_by_sir3s_id = self._mx1_df.set_index("Sir3sID")["DATATYPE"]

        prefix = f"{object_type_code}~*~*~*~"
        resolved_pieces = []
        for col in raw_df.columns:
            if not col.startswith(prefix):
                continue
            prop = col[len(prefix):]
            if "VEC" in prop:
                continue  # interior-point channel: not resolved here, see docstring

            values = raw_df[col]
            if len(values) == 0:
                continue
            n_items = len(values.iloc[0])
            if n_items != len(mx2_tks):
                logger.warning(
                    f"[bulk results] Column '{col}' has {n_items} value(s) per record but .MX2 lists "
                    f"{len(mx2_tks)} '{object_type_code}' tk(s); skipping this property."
                )
                continue

            col_datatype = mx1_datatype_by_sir3s_id.get(col)

            if col_datatype == "CHAR":
                # Plain decode, no stripping/normalizing - verified empirically that this matches
                # GetResultfortimestamp()'s own returned string for the same (tk, prop, timestamp)
                # exactly, padding/null bytes and all (SIR 3S fixed-width CHAR fields, e.g. an unset
                # PHI1, decode to something like "\x00           " both ways) - bulk=True has to
                # reproduce that literally, not "clean it up", to actually match bulk=False's output.
                rows = [tuple(v.decode("utf-8", errors="replace") for v in row) for row in values]
                expanded = pd.DataFrame(rows, index=values.index, columns=mx2_tks)
            elif col_datatype in _KNOWN_MX_NUMERIC_DATATYPES:
                try:
                    # np.asarray(..., dtype=...) first, instead of handing pd.DataFrame() the raw
                    # nested list of tuples directly: pandas' own per-column dtype inference over a
                    # Python list is ~100x slower than building the 2D float array in one numpy call up
                    # front (measured: 0.8s vs 0.006s for one 3000 x 1000 column) - same values either
                    # way, just constructed the fast way.
                    array = np.asarray(values.tolist(), dtype=np.float64)
                except (TypeError, ValueError) as e:
                    # Shouldn't happen for REAL/INT4 (struct.unpack() already guarantees native
                    # floats/ints) - kept as a defensive fallback so a surprise here degrades to
                    # "this one property is unavailable" (via the reindex()-fills-missing-with-
                    # place_holder_value path downstream), not "every scalar property for this element
                    # type is unavailable", the way this used to fail before.
                    logger.warning(
                        f"[bulk results] Column '{col}' is DATATYPE={col_datatype!r} but its values "
                        f"aren't all numeric ({e}); skipping this property."
                    )
                    continue
                expanded = pd.DataFrame(array, index=values.index, columns=mx2_tks)
            else:
                # Anything other than CHAR/REAL/INT4 shouldn't reach here at all: reading raw_df in the
                # first place already requires _build_mx_record_unpack_format() to have accepted every
                # channel's DATATYPE (it hard-fails on an unrecognized one - see its own docstring/logs
                # for *why* that's a whole-file failure, not scoped to one property). This branch exists
                # so a *future* DATATYPE this module learns to unpack at that stage, but forgets to
                # classify here, fails the same soft way as the block above instead of crashing every
                # scalar property for this element type via a bare numeric cast.
                logger.warning(
                    f"[bulk results] Column '{col}' has DATATYPE={col_datatype!r}, which "
                    "_get_mx_scalar_results_for_element_type() doesn't know how to classify as numeric "
                    "or text; skipping this property."
                )
                continue

            expanded.columns = pd.MultiIndex.from_tuples([(tk, prop) for tk in mx2_tks])
            resolved_pieces.append(expanded)

        resolved = pd.concat(resolved_pieces, axis=1) if resolved_pieces else pd.DataFrame(index=raw_df.index)
        cache[element_type_name] = resolved
        logger.info(f"[bulk results] In-memory Tier 2 (scalar) cache built for element type '{element_type_name}'. Shape: {resolved.shape}")
        return resolved

    def _get_mx_vector_results_for_element_type(
        self, element_type: Enum, cache_suffix: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Tier 2b of the bulk-results cache: for one element type, all VEC-named (interior-point) result
        properties resolved down to individual tks, built lazily and cached in
        self._mx_results_cache_vector_by_element_type. Values are tab-separated strings, matching the
        convention used elsewhere (e.g. add_interior_points_to_start_end_sequence()).

        Only works for element types where .MX2 provides a per-object segment-length row alongside its
        tk list - currently just ROHR/Pipe, via "N_OF_POINTS". Element types without such a row return
        an empty DataFrame; generate_element_results_dataframe(bulk=True) falls back to the existing
        per-value GetResultfortimestamp() loop for those properties.

        :param element_type: The element type (e.g., self.ObjectTypes.Pipe).
        :type element_type: Enum
        :param cache_suffix: Forwarded to _get_mx_raw_results_cache() - None for the live cache, or a
                        name to resolve against a specific archived snapshot instead.
        :type cache_suffix: Optional[str]
        :return: DataFrame with one row per UTC timestamp (matching Tier 1's index) and MultiIndex
                        columns [(tk, property)], VEC-named result properties only, values as
                        tab-separated strings of floats. Empty if this element type has no resolvable
                        VEC properties.
        :rtype: pd.DataFrame
        """
        raw_df = self._get_mx_raw_results_cache(cache_suffix=cache_suffix)

        cache = getattr(self, "_mx_results_cache_vector_by_element_type", None)
        if cache is None:
            cache = {}
            self._mx_results_cache_vector_by_element_type = cache

        element_type_name = element_type.name
        if element_type_name in cache:
            return cache[element_type_name]

        object_type_code = mapping_for_groups.get(element_type_name)
        if not object_type_code or object_type_code == -1:
            cache[element_type_name] = pd.DataFrame(index=raw_df.index)
            return cache[element_type_name]

        mx2_tk_rows = self._mx2_df[
            (self._mx2_df["ObjType"].str.strip() == object_type_code)
            & (self._mx2_df["AttrType"].str.strip().isin(["tk", "pk"]))
        ]
        mx2_len_rows = self._mx2_df[
            (self._mx2_df["ObjType"].str.strip() == object_type_code)
            & (self._mx2_df["AttrType"].str.strip() == "N_OF_POINTS")
        ]
        if mx2_tk_rows.empty or mx2_len_rows.empty:
            logger.info(
                f"[bulk results] No .MX2 per-object segment-length row (N_OF_POINTS) for OBJTYPE "
                f"'{object_type_code}'; VEC properties for '{element_type_name}' aren't resolvable "
                "from the MX cache, falling back to GetResultfortimestamp() for those."
            )
            cache[element_type_name] = pd.DataFrame(index=raw_df.index)
            return cache[element_type_name]

        mx2_tks = list(mx2_tk_rows.iloc[0]["Data"])
        segment_lengths = list(mx2_len_rows.iloc[0]["Data"])
        if len(segment_lengths) != len(mx2_tks):
            logger.warning(
                f"[bulk results] .MX2 N_OF_POINTS has {len(segment_lengths)} entries but the tk list "
                f"has {len(mx2_tks)} for OBJTYPE '{object_type_code}'; skipping VEC resolution."
            )
            cache[element_type_name] = pd.DataFrame(index=raw_df.index)
            return cache[element_type_name]

        offsets = [0]
        for length in segment_lengths:
            offsets.append(offsets[-1] + length)

        prefix = f"{object_type_code}~*~*~*~"
        resolved_pieces = []
        for col in raw_df.columns:
            if not col.startswith(prefix):
                continue
            prop = col[len(prefix):]
            if "VEC" not in prop:
                continue  # scalar channel, handled by _get_mx_scalar_results_for_element_type()

            flat_values = raw_df[col]
            if len(flat_values) == 0:
                continue
            if len(flat_values.iloc[0]) != offsets[-1]:
                logger.warning(
                    f"[bulk results] Column '{col}' has {len(flat_values.iloc[0])} value(s) per record "
                    f"but .MX2 N_OF_POINTS sums to {offsets[-1]} for OBJTYPE '{object_type_code}'; "
                    "skipping this property."
                )
                continue

            per_object_columns = {}
            for i, tk in enumerate(mx2_tks):
                start, length = offsets[i], segment_lengths[i]
                per_object_columns[(tk, prop)] = flat_values.apply(
                    lambda flat, start=start, length=length: "\t".join(
                        _format_sir3s_float(v) for v in flat[start:start + length]
                    )
                )
            resolved_pieces.append(pd.DataFrame(per_object_columns, index=raw_df.index))

        resolved = pd.concat(resolved_pieces, axis=1) if resolved_pieces else pd.DataFrame(index=raw_df.index)
        cache[element_type_name] = resolved
        logger.info(f"[bulk results] In-memory Tier 2 (vector) cache built for element type '{element_type_name}'. Shape: {resolved.shape}")
        return resolved

    def _build_mx_timestamp_label_map(self, utc_index, api_timestamps=None) -> dict:
        """
        Maps each UTC pd.Timestamp in utc_index to the corresponding local-time-with-offset timestamp
        string as returned by self.GetTimeStamps(), matched by parsed instant. Calls
        self.GetTimeStamps() exactly once, not once per timestamp - unless the caller already has that
        result (e.g. from its own earlier call, or another call to this method in the same pipeline)
        and passes it in via api_timestamps, in which case this makes no GetTimeStamps() call at all.

        :param utc_index: UTC-tz-aware timestamps to find matching labels for (e.g. Tier 1's/Tier 2's
                        DataFrame index).
        :type utc_index: Iterable[pandas.Timestamp]
        :param api_timestamps: Pre-fetched self.GetTimeStamps()[0] result, to avoid a redundant
                        GetTimeStamps() call when the caller already has it. Default: None (fetch it).
        :type api_timestamps: Optional[Sequence[str]]
        :return: Mapping of {utc_timestamp: matching self.GetTimeStamps() string}. Entries with no
                        matching API timestamp are omitted.
        :rtype: dict
        """
        if api_timestamps is None:
            api_timestamps, _tsStat, _tsMin, _tsMax = self.GetTimeStamps()
        if not api_timestamps:
            return {}
        # pd.to_datetime() on the whole list at once instead of once per string: parsing each string
        # individually forces pandas to re-guess the datetime format from scratch every single time
        # (measured: 5.6s for 3000 timestamps, the single biggest cost in a fully-cached bulk=True
        # call) instead of inferring it once and reusing it. utc=True normalizes every parsed instant
        # to UTC - api_timestamps can span a DST boundary (mixed +01:00/+02:00 offsets), which a
        # non-utc batch parse would raise on in a future pandas version; instant equality/hashing
        # against utc_index (already UTC) is unaffected either way; the *values* stored below are
        # still the original local-offset strings, unchanged.
        parsed = pd.to_datetime(list(api_timestamps), utc=True)
        instant_to_label = dict(zip(parsed, api_timestamps))
        return {
            utc_ts: instant_to_label[utc_ts]
            for utc_ts in utc_index
            if utc_ts in instant_to_label
        }

    def generate_element_results_dataframe(
        self,
        element_type: Enum,
        tks: Optional[List[str]] = None,
        properties: Optional[List[str]] = None,
        timestamps: Optional[Union[List[str], List[int]]] = None,
        place_holder_value: Optional[float] = 99999.0,
        drop_full_place_holder_columns: Optional[bool] = True,
        bulk: Optional[bool] = False,
        mx_cache_suffix: Optional[str] = None,

    ) -> pd.DataFrame:

        """
        Generate a dataframe with RESULT (time-dependent) properties for all devices and timestamps.

        :param element_type: The element type (e.g., self.ObjectTypes.Node).
        :type element_type: Enum
        :param tks: List of tks of instances of the element type to include. All other tks will be excluded. Use for filtering.
                    Default: None (no filtering)
        :type tks: list[str], optional
        :param properties: List of RESULT property names to include.
                        If properties=None ⇒ includes all available result properties (per element, only if values exist).
                        If properties=[] ⇒ no properties are used.
                        Default: None.
        :type properties: list[str], optional
        :param timestamps: List of timestamps to include. Can be:
                        - List of timestamp strings
                            (e.g., ["2025-09-25 00:00:00.000 +02:00", "2025-09-25 00:05:00.000 +02:00"])
                        - List of integer indices
                            (e.g., [0, 7, -1])
                            where 0 = first timestamp, 7 = eighth timestamp, -1 = last timestamp.
                        Default: None (includes all available timestamps).
        :type timestamps: list[Union[str, int]], optional
        :param place_holder_value: float values to be used if SIR 3S calculations do not return results.
                        Default: 99999.0
        :type place_holder_value: float, optional
        :param drop_full_place_holder_columns: Determine whether columns, that are completley filled with place holder values, get dropped.
                Default: True
        :type drop_full_place_holder_columns: bool, optional
        :param bulk: WORK IN PROGRESS. If False (default), retrieve every value via one
                        GetResultfortimestamp() call each - reliable, but slow for large requests. If
                        True, result properties are instead retrieved from a cached bulk read of the
                        model's .MXS result file where possible (see read_mx_results()), falling back
                        to the GetResultfortimestamp() loop for whatever can't be resolved that way.
                        Output shape is identical either way; only retrieval speed/cost differs. Only
                        use bulk=True for genuinely large requests - the cache-building step itself
                        isn't free.
        :type bulk: bool, optional
        :param mx_cache_suffix: WORK IN PROGRESS. Only meaningful when bulk=True (ignored, with a
                        warning, otherwise). None (default): use the live MX results cache for the
                        model's current calculation, refreshed automatically whenever the underlying
                        .MXS file changes. A name: instead load a specific archived snapshot of a past
                        calculation, previously preserved by copying/renaming the on-disk cache file
                        ("mxcache.zip", written next to the .MX1 file) to "mxcache.<mx_cache_suffix>.zip".
                        Loaded unconditionally (no freshness check); raises FileNotFoundError if that
                        file doesn't exist. Only one calculation's results are ever cached at once, so
                        switching snapshots replaces whatever was cached before.
        :type mx_cache_suffix: str, optional

        :return: DataFrame with one row per timestamp and MultiIndex columns:
                - Level 0: tk (device ID)
                - Level 1: name (device name)
                - Level 2: end_nodes (tuple of connected node tks as string)
                - Level 3: property (result name)
                Data types: float for scalars, str for vectorized data and literal strings.
        :rtype: pd.DataFrame

        :description:
        Generates a DataFrame containing time-dependent result vectors for all selected devices and timestamps.
        Supports both timestamp strings and index-based selection. Produces a MultiIndex-column DataFrame grouped by device, name, end-nodes, and property.
        """

        # --- Param validity ---
        if mx_cache_suffix is not None and not bulk:
            logger.warning(
                f"[results] mx_cache_suffix={mx_cache_suffix!r} was given but bulk=False; it only "
                "applies to the MX-based bulk=True retrieval path and is ignored here."
            )

        # --- Validate time stamps ---
        logger.info(f"[results] Generating results dataframe for element type: {element_type}")

        valid_timestamps = self._resolve_given_timestamps(timestamps)
        if not valid_timestamps:
            logger.warning("[results] No valid timestamps. Returning empty dataframe.")
            return pd.DataFrame()
            
        # --- Resolve tks ---
        tks=self.__resolve_given_tks(element_type=element_type, tks=tks, filter_container_tks=None)
        if len(tks) < 1:
            return pd.DataFrame()
        
        # --- Resolve given properties ---
        try:
            available_model_data_props = self.GetPropertiesofElementType(ElementType=element_type)
            available_result_props = self.GetResultProperties_from_elementType(
                elementType=element_type,
                onlySelectedVectors=False
            )
            available_result_vector_props=[available_result_props for available_result_props in available_result_props if "VEC" in available_result_props]
            available_result_non_vector_props = [available_result_props for available_result_props in available_result_props if "VEC" not in available_result_props]

            result_props: List[str] = []

            if properties is None:
                logger.info(f"[results] No properties given → using ALL result properties for {element_type}.")
                result_props = available_result_props
            else:
                for prop in properties:
                    if prop in available_result_props:
                        result_props.append(prop)
                    elif prop in available_model_data_props:
                        logger.warning(f"[results] Property '{prop}' is a model_data property; excluded from results.")
                    else:
                        logger.warning(
                            f"[results] Property '{prop}' not found in model_data or result properties of type {element_type}. Excluding."
                        ) 
            logger.info(f"[results] Using {len(result_props)} result properties.")
        except Exception as e:
            logger.error(f"[results] Error determining result properties: {e}")
            return pd.DataFrame()

        end_nodes_available = False
        if self.__is_get_endnodes_applicable(element_type=element_type):
            end_nodes_available = True

        # --- Retrieve values ---
        logger.info(f"[results] Retrieving result values... (bulk={bulk})")

        data_dict = defaultdict(dict)
        bulk_frames: List[pd.DataFrame] = []

        if bulk:
            # Fetched once and shared with both _build_mx_timestamp_label_map() calls below (scalar and
            # vector) instead of each doing its own GetTimeStamps() call - a real, measured COM
            # round-trip cost (~0.5s/call), not a cheap local lookup.
            raw_api_timestamps, _tsStat, _tsMin, _tsMax = self.GetTimeStamps()

            available_mx_channel_props = self._get_available_mx_channel_props_for_element_type(
                element_type, cache_suffix=mx_cache_suffix
            )
            if available_mx_channel_props is not None:
                props_without_mx_channel = [prop for prop in result_props if prop not in available_mx_channel_props]
            else:
                props_without_mx_channel = []  # unknown OBJTYPE mapping - don't filter, keep old behavior
            if props_without_mx_channel:
                logger.info(
                    f"[bulk results] {len(props_without_mx_channel)} requested propert"
                    f"{'y has' if len(props_without_mx_channel) == 1 else 'ies have'} no MX1 channel for "
                    f"'{element_type.name}' in this calculation run (not selected/archived) - filling "
                    f"with place_holder_value directly, skipping the API-loop fallback for them: "
                    f"{props_without_mx_channel}"
                )
                ts_labels = [str(ts) for ts in valid_timestamps]
                placeholder_columns = pd.MultiIndex.from_product([tks, props_without_mx_channel])
                bulk_frames.append(pd.DataFrame(place_holder_value, index=ts_labels, columns=placeholder_columns))

            props_with_mx_channel = [prop for prop in result_props if prop not in props_without_mx_channel]

            # Scalar (non-VEC) properties: fast MX-based bulk path (Tier 1 + Tier 2 cache).
            scalar_props = [prop for prop in props_with_mx_channel if prop not in available_result_vector_props]
            vector_props_all = [prop for prop in props_with_mx_channel if prop in available_result_vector_props]
            vector_props_remaining = list(vector_props_all)  # default: none resolved from MX yet

            if scalar_props:
                try:
                    bulk_df = self._get_mx_scalar_results_for_element_type(element_type, cache_suffix=mx_cache_suffix)
                    label_map = self._build_mx_timestamp_label_map(bulk_df.index, api_timestamps=raw_api_timestamps)
                    valid_timestamps_set = set(valid_timestamps)
                    wanted_utc_ts = [utc_ts for utc_ts, ts_label in label_map.items() if ts_label in valid_timestamps_set]

                    if wanted_utc_ts:
                        # One vectorized row/column selection instead of a per-cell Python loop: bulk_df's
                        # columns are a MultiIndex assembled via pd.concat() (not lexsorted), so per-cell
                        # membership checks/lookups degrade to O(n) each - reindex() does the equivalent
                        # selection (missing (tk, prop) combos become NaN columns) in one vectorized call.
                        wanted_columns = pd.MultiIndex.from_product([tks, scalar_props])
                        scalar_slice = bulk_df.loc[wanted_utc_ts].reindex(columns=wanted_columns)
                        scalar_slice.index = [label_map[utc_ts] for utc_ts in scalar_slice.index]
                        # No blanket .astype(float) here - most scalar properties are numeric (already
                        # float64, from _get_mx_scalar_results_for_element_type()), but some are
                        # legitimately CHAR-typed text (already decoded to str/NaN there too, same
                        # module). A DataFrame-wide astype(float) would raise the moment it hit any text
                        # column, which - caught by the except below - used to drop *every* scalar
                        # property at once, not just the offending one. .where() works uniformly on
                        # mixed per-column dtypes: NaN (genuinely missing, or reindex()'s fill for a
                        # missing (tk, prop) combo) becomes place_holder_value either way, real values
                        # (numeric or text) pass through untouched.
                        scalar_slice = scalar_slice.where(scalar_slice.notna(), place_holder_value)
                        bulk_frames.append(scalar_slice)
                except Exception as e:
                    logger.error(f"[results] bulk=True scalar retrieval failed, falling back to none for those properties: {e}")

            # VEC-named (interior-point) properties: fast MX-based bulk path too, where resolvable (see
            # _get_mx_vector_results_for_element_type() - currently ROHR/Pipe only, via .MX2 N_OF_POINTS).
            # Whatever isn't resolvable falls through to the API loop below, same as before.
            if vector_props_all:
                try:
                    vector_bulk_df = self._get_mx_vector_results_for_element_type(element_type, cache_suffix=mx_cache_suffix)
                    available_vec_props = {prop for (_tk, prop) in vector_bulk_df.columns}
                    resolvable_vector_props = [prop for prop in vector_props_all if prop in available_vec_props]

                    if resolvable_vector_props:
                        label_map = self._build_mx_timestamp_label_map(vector_bulk_df.index, api_timestamps=raw_api_timestamps)
                        valid_timestamps_set = set(valid_timestamps)
                        wanted_utc_ts = [utc_ts for utc_ts, ts_label in label_map.items() if ts_label in valid_timestamps_set]

                        if wanted_utc_ts:
                            wanted_columns = pd.MultiIndex.from_product([tks, resolvable_vector_props])
                            vector_slice = vector_bulk_df.loc[wanted_utc_ts].reindex(columns=wanted_columns)
                            vector_slice.index = [label_map[utc_ts] for utc_ts in vector_slice.index]
                            # missing (tk, prop) combos become NaN via reindex() - same place_holder_value
                            # convention the API-loop path below uses for GetResultfortimestamp() returning
                            # "" for a vector property. .where() is vectorized and works fine on this
                            # object-dtype (string-valued) frame, same as the scalar branch above.
                            vector_slice = vector_slice.where(vector_slice.notna(), place_holder_value)
                            bulk_frames.append(vector_slice)

                        vector_props_remaining = [prop for prop in vector_props_all if prop not in resolvable_vector_props]
                except Exception as e:
                    logger.error(f"[results] bulk=True vector retrieval failed, falling back to API for those properties: {e}")
        else:
            # bulk=False: every property retrieved the same way, via the loop below.
            vector_props_remaining = None  # sentinel: loop below iterates result_props, not just vector_props

        # Whatever wasn't resolved from the MX cache above (VEC properties for element types without a
        # usable .MX2 segment-length row, e.g. anything but ROHR/Pipe right now), or every property for
        # bulk=False: unchanged per-value GetResultfortimestamp() loop.
        props_via_api = result_props if vector_props_remaining is None else vector_props_remaining
        for ts in map(str, valid_timestamps):
            for tk in tks:
                for prop in props_via_api:
                    try:
                        value = self.GetResultfortimestamp(timestamp=ts, Tk=tk, property=prop)[0]
                        if value == "":
                            data_dict[(tk, prop)][ts] = place_holder_value
                        elif prop in available_result_vector_props:
                            value = str(value)
                            data_dict[(tk, prop)][ts] = value
                        else:
                            try:
                                value = float(value)
                                data_dict[(tk, prop)][ts] = value
                            except (ValueError, TypeError):
                                value = str(value)
                                data_dict[(tk, prop)][ts] = value
                    except Exception as e:
                        logger.warning(f"[results] Failed to get result '{prop}' for tk '{tk}' at '{ts}': {e}")

        # Merge the API-loop's dict-of-dicts frame (if any) with the bulk-resolved frames (if any) in one
        # vectorized concat, aligned by their shared ts_label index - see bulk_frames comment above.
        frames_to_concat = list(bulk_frames)
        if data_dict:
            frames_to_concat.append(pd.DataFrame(data_dict))
        df = pd.concat(frames_to_concat, axis=1) if frames_to_concat else pd.DataFrame()

        # Reorder columns to tk-major/property-minor traversal order (matching tks x result_props),
        # regardless of which path resolved which property. bulk=False already builds data_dict in this
        # order naturally (the loop below is tk-major already); bulk=True populates data_dict from two
        # separate vectorized merges (scalar block, then vector block), which otherwise leaves all scalar
        # columns grouped before all vector columns instead of interleaved per tk - i.e. each pipe's own
        # columns would end up split apart instead of adjacent.
        # Membership against a plain Python set of tuples, not `(tk, prop) in df.columns` (a MultiIndex)
        # directly - the latter's __contains__/get_loc turned out NOT to be reliably O(1) here in
        # practice (measured 33x slower, and this loop was 57% of one profiled call's total time at a
        # real 524-tk/82-property scale) - a set's hashing has no such dependency on the MultiIndex's
        # internal engine state, which a pd.concat()-assembled index (as df's is, from bulk_frames plus
        # the API-loop's frame) doesn't appear to hit the fast path for.
        existing_columns = set(df.columns)
        canonical_column_order = [(tk, prop) for tk in tks for prop in result_props if (tk, prop) in existing_columns]
        df = df.reindex(columns=canonical_column_order)

        if drop_full_place_holder_columns:
            mask_placeholder_all = df.eq(place_holder_value).all()
            amount_of_dropped_cols = int(mask_placeholder_all.sum())
            df = df.loc[:, ~mask_placeholder_all]
            logger.info(f"[results] {amount_of_dropped_cols} fully NaN columns dropped.")
        df.index.name = "timestamp"
        
        
        # --- Add Name, End Nodes and Interior points to column MultiIndex ---
        # One GetValue(Name)/GetEndNodes() call per unique tk, not per (tk, prop) column - the same tk
        # appears in one column per requested property, so looking it up again for each of those is
        # pure waste (measured: ~23x more COM calls than necessary at a 1000-tk/23-property scale,
        # ~2.8s of a fully-cached bulk=True call).
        label_by_tk = {}
        for tk in df.columns.get_level_values(0).unique():
            try:
                name = self.GetValue(tk, "Name")[0]
            except Exception as e:
                logger.warning(f"[results] Failed to get name for tk '{tk}': {e}")
                name = "UNKNOWN"

            if end_nodes_available:
                try:
                    end_nodes = self.GetEndNodes(tk)
                    end_nodes_str = str(end_nodes)
                except Exception as e:
                    logger.warning(f"[results] Failed to get end nodes for tk '{tk}': {e}")
                    end_nodes_str = "UNKNOWN"
            else:
                end_nodes_str = "No end nodes on element type"

            label_by_tk[tk] = (name, end_nodes_str)

        col_tuples = [(tk, label_by_tk[tk][0], label_by_tk[tk][1], prop) for tk, prop in df.columns]

        df.columns = pd.MultiIndex.from_tuples(
            col_tuples,
            names=["tk", "name", "end_nodes", "property"]
        )
       

        logger.info(f"[results] Done. Shape: {df.shape}")
        return df

    def convert_rows_to_single_tuple_row(
        self,
        df: pd.DataFrame
    ) -> Tuple[pd.DataFrame, dict]:

        """
        Collapse a multi-row dataframe into a single-row dataframe where each
        column cell contains a tuple with all row values in index order.

        A dictionary mapping each dataframe index value to its tuple position
        is stored in an additional column.

        :param df: Input dataframe with one or multiple rows.
        :type df: pd.DataFrame
        :return: Single-row dataframe with tuple values per original column and
            one mapping column containing ``{index_value: tuple_position}``.
        :rtype: Tuple[pd.DataFrame, dict]

        :description:
        This method is intended for result-style dataframes where rows usually
        represent timestamps. The row order of ``df`` is preserved when building
        tuples. Works with regular columns and MultiIndex columns (as produced by
        ``generate_element_results_dataframe``). The mapping dictionary allows
        tracing tuple positions back to the original index values. This method
        expects a unique dataframe index.
        """

        logger.info("[rows_to_tuple_row] Collapsing dataframe rows into tuple row...")

        if df is None or df.empty:
            logger.info("[rows_to_tuple_row] Input dataframe is empty. Returning empty dataframe.")
            return pd.DataFrame(), {}

        if not df.index.is_unique:
            logger.error("[rows_to_tuple_row] Dataframe index is not unique. Please provide a dataframe with unique index values.")
            return pd.DataFrame(), {}
        
        # .to_numpy().T.tolist() once, instead of a per-column df[col].tolist(): 3-6x faster at
        # realistic tk x property column counts (verified). Must go through .tolist() specifically
        # (not raw numpy iteration) so values stay native Python types (e.g. float, not numpy.float64),
        # matching the previous per-column .tolist() behavior exactly.
        rows_as_lists = df.to_numpy().T.tolist()
        tuple_row = dict(zip(df.columns, map(tuple, rows_as_lists)))

        out = pd.DataFrame([tuple_row])
        out.columns = df.columns

        timestamp_to_tuple_index = {
            str(idx): pos
            for pos, idx in enumerate(df.index.tolist())
        }

        logger.info(f"[rows_to_tuple_row] Done. Shape: {out.shape}")
        return out, timestamp_to_tuple_index

    ## Dataframe Creation: Explicit Dataframe Creation

    def generate_element_dataframe(
        self,
        element_type: str,
        tks: Optional[list[str]] = None,
        timestamps: Optional[Union[List[str], List[int]]] = None,
        bulk: bool = False,
        mx_cache_suffix: Optional[str] = None,
    ) -> pd.DataFrame | gpd.GeoDataFrame:

        """
        Generates a comprehensive DataFrame containing model_data and static result values for all requested elements of the given type. Result values are written in the df as tuple of floats (or tuple (time) of tuple (interior point) of floats for pipe interior points) with each entry corresponding to a simulations timestamp. 
        Geometry and end-node tks are always included. All model_data and result values (self.GetResultProperties_from_elementType(onlySelectedVectors=False)) for are included.
        The tks of end nodes are included (fkKI, fkKK). Geometry information is also included.

        :param element_type: The element type (e.g., self.ObjectTypes.Node, self.ObjectTypes.Pipe).
        :type element_type: Enum
        :param tks: List of tks to include in the dataframe.
                    Default: None.
        :type tks: list[str], optional
        :param timestamps: Timestamps used for obtaining result values.
                    Default: Static.
        :type timestamps: Optional[Union[List[str], List[int]]], optional
        :param bulk: Whether to use bulk mode for result retrieval.
                    Default: False.
        :type bulk: bool, optional
        :param mx_cache_suffix: Suffix for the cache file used in bulk mode.
                    Default: None.
        :type mx_cache_suffix: Optional[str], optional
        :return: DataFrame containing one row per element instance, including model_data, end
                nodes, geometry, and available static result values. Dict mapping timestamps to tuple indices for result values is also returned.
        :rtype: tuple[pd.DataFrame, dict[str, int]]
        """

        logger.info(f"[generate_element_dataframe] Generating df for element type: {element_type} ...")
        
        try:
            logger.info(f"[generate_element_dataframe] Generating df_model_data for element type: {element_type} ...")
            df_model_data = self.generate_element_model_data_dataframe(element_type=element_type
                                                                ,tks=tks
                                                                ,properties=None
                                                                ,geometry=True
                                                                ,end_nodes=self.__is_get_endnodes_applicable(element_type)
                                                                ,element_type_col=False
                                                                ,resolve_references=True
            )
            if df_model_data.empty:
                logger.error(f"[generate_element_dataframe] Obtained model dataframe is empty.")
                return pd.DataFrame(), dict()
            
            if timestamps is None:
                timestamps = [self.GetTimeStamps()[1]]

            result_values_to_obtain = self.GetResultProperties_from_elementType(element_type, False)

            logger.info(f"[generate_element_dataframe] Generating df_results for element type: {element_type} ...")
            df_results = self.generate_element_results_dataframe(element_type=element_type
                                                                        ,tks=tks
                                                                        ,properties=result_values_to_obtain
                                                                        ,timestamps=timestamps
                                                                        ,bulk=bulk
                                                                        ,mx_cache_suffix=mx_cache_suffix
                                                                        
            )
            if df_results.empty:
                logger.error(f"[generate_element_dataframe] Obtained results dataframe is empty.")
                return pd.DataFrame(), dict()
            
            df_results = self.add_interior_points_to_start_end_sequence(df_results)

            df_results, timestamp_to_tuple_index = self.convert_rows_to_single_tuple_row(df_results)

            logger.info(f"[generate_element_dataframe] Merging df_model_data with df_results for element type: {element_type} ...")
            df_merged = self.merge_model_data_and_results(df_model_data=df_model_data, df_results=df_results)

            return df_merged, timestamp_to_tuple_index
        
        except Exception as e:
            logger.error(f"[generate_element_dataframe] Error Generating df for element type: {element_type}: {e}")
            return pd.DataFrame(), dict()
        
    def add_interior_points_as_multiindex(self, df_results):
        """
        Expand vector properties from tab-separated strings into multiple interior-point
        segments along a new MultiIndex column level.

        Vector properties are identified by having 'VEC' in the last column-level name.
        Their tab-separated string values are split into float segments representing
        interior points along the device. Non-vector properties have their interior
        point index set to -1 and retain their scalar values.

        :param df_results: Results DataFrame containing scalar and vector properties.
        :type df_results: pd.DataFrame

        :return: A DataFrame in which vector properties are expanded along a new
                MultiIndex level named 'interior points', with float values for each
                interior segment. Non-vector properties are assigned interior point -1.
        :rtype: pd.DataFrame

        :description:
            This method processes the result DataFrame by expanding tab-separated
            vector-valued properties (typically from pipes) into properly structured
            numerical segments. Each vector entry becomes a sequence of interior point
            values along a new index level. Scalar properties remain unchanged and are
            placed under interior point -1 to maintain consistent indexing.
        """

        if df_results is None or df_results.empty or len(df_results.columns) == 0:
            return df_results.copy() if isinstance(df_results, pd.DataFrame) else pd.DataFrame()

        last_level = df_results.columns.get_level_values(-1)
        vec_props = {p for p in last_level.unique() if "VEC" in str(p)}

        new_level_name = "interior points"
        new_names = list(df_results.columns.names) + [new_level_name]

        pieces = []

        for col_key in df_results.columns:

            key = col_key if isinstance(col_key, tuple) else (col_key,)
            prop = key[-1]
            col = df_results[col_key]

            if prop in vec_props:

                s = col.where(col.notna())
                
                split_lists = s.apply(lambda x: x.split("\t") if isinstance(x, str) else [])

                # Determine max number of segments for THIS column
                max_len = split_lists.apply(len).max()

                if max_len == 0:
                    continue

                
                segs = pd.DataFrame(
                    split_lists.apply(lambda lst: lst + [None] * (max_len - len(lst))).tolist(),
                    index=col.index
                )

                # Convert to numeric
                segs = segs.apply(pd.to_numeric, errors="coerce")

                # Assign MultiIndex columns
                segs.columns = pd.MultiIndex.from_tuples(
                    [key + (i,) for i in range(max_len)],
                    names=new_names
                )

                pieces.append(segs)

            else:
                # Non-vector property → interior point = -1
                df1 = col.to_frame()
                df1.columns = pd.MultiIndex.from_tuples(
                    [key + (-1,)],
                    names=new_names
                )
                pieces.append(df1)

        if not pieces:
            return df_results.copy()

        out = pd.concat(pieces, axis=1)
        out = out.dropna(axis=1, how="all")
        return out
            
    def add_interior_points_to_start_end_sequence(self, df_results):
        """
        Convert VEC vector columns from tab-separated strings into:
        - <prop>_start:   first element
        - <prop>_end:     last element
        - <prop>_sequence: a tuple containing all elements

        Non-VEC properties remain scalar and unchanged.

        :param df_results: pd.DataFrame with VEC properties as tab-separated strings
        :type df_results: pd.DataFrame
        :return: DataFrame with expanded scalar VEC columns
        :rtype: pd.DataFrame
        """

        if df_results is None or df_results.empty or len(df_results.columns) == 0:
            return df_results.copy() if isinstance(df_results, pd.DataFrame) else pd.DataFrame()

        last_level = df_results.columns.get_level_values(-1)
        vec_props = {p for p in last_level.unique() if "VEC" in str(p)}

        is_multi = isinstance(df_results.columns, pd.MultiIndex)

        # A per-column loop building/concatenating one tiny DataFrame (plus its own
        # pd.MultiIndex.from_tuples() call) per column is a well-known slow pandas pattern at real
        # tk x property column counts (verified: ~9x speedup from the rewrite below, at 1000 tks x 7
        # properties). Instead: classify columns first (still respecting original column order for the
        # final result), batch-parse all real VEC columns' values via one to_numpy() + plain Python
        # loop (no per-column pandas .apply() overhead, and no stack()/unstack() round-trip - tried
        # that too, it was both slower AND wrong at this scale), then build the whole output DataFrame
        # once at the end.
        candidate_vec_cols = [
            c for c in df_results.columns if (c if isinstance(c, tuple) else (c,))[-1] in vec_props
        ]
        real_vec_col_set = set()
        if candidate_vec_cols:
            has_tab = df_results[candidate_vec_cols].apply(self._column_has_vector_values, axis=0)
            real_vec_col_set = set(has_tab.index[has_tab])

        def _split_start_end_sequence(x):
            if isinstance(x, str):
                parts = tuple(float(v) for v in x.split("\t"))
                if parts:
                    return (parts[0], parts[-1], parts)
            return (None, None, ())

        parsed_by_col = {}
        if real_vec_col_set:
            ordered_vec_cols = [c for c in df_results.columns if c in real_vec_col_set]
            arr = df_results[ordered_vec_cols].to_numpy()
            for j, col_key in enumerate(ordered_vec_cols):
                parsed_by_col[col_key] = [_split_start_end_sequence(v) for v in arr[:, j]]

        new_cols = {}
        for col_key in df_results.columns:
            key = col_key if isinstance(col_key, tuple) else (col_key,)
            prop = key[-1]
            base_key = key[:-1]  # everything except the last level (property name)

            if col_key in real_vec_col_set:
                triples = parsed_by_col[col_key]
                start = [t[0] for t in triples]
                end = [t[1] for t in triples]
                sequence = [t[2] for t in triples]
                if is_multi:
                    new_cols[base_key + (prop + "_start",)] = start
                    new_cols[base_key + (prop + "_end",)] = end
                    new_cols[base_key + (prop + "_sequence",)] = sequence
                else:
                    new_cols[f"{prop}_start"] = start
                    new_cols[f"{prop}_end"] = end
                    new_cols[f"{prop}_sequence"] = sequence
            else:
                # Keep scalar property untouched
                new_cols[key if is_multi else key[0]] = df_results[col_key].tolist()

        out = pd.DataFrame(new_cols, index=df_results.index)
        if is_multi:
            out.columns = pd.MultiIndex.from_tuples(list(new_cols.keys()), names=df_results.columns.names)
        return out

    def add_interior_points_as_flat_cols(self, df):
        """
        Expand tab-separated vector columns (name contains "VEC") into *_0..*_N-1 columns.
        Non-VEC columns remain unchanged.

        :param df: Input DataFrame with scalar columns and VEC columns containing tab-separated strings.
        :type df: pd.DataFrame

        :return: DataFrame with new numeric columns for each interior point.
        :rtype: pd.DataFrame

        :description:
            This method processes the result DataFrame by expanding tab-separated
            vector-valued properties (typically from pipes) into properly structured
            numerical segments. Each vector entry becomes a new column.
        """
        df_out = df.copy()
        vec_cols = [c for c in df_out.columns if "VEC" in str(c)]

        for col in vec_cols:
            s = df_out[col]

            # Split only string cells; treat empty strings as no segments; strip whitespace
            split_lists = s.map(
                lambda x: [p for p in str(x).strip().split("\t") if p != ""]
                if isinstance(x, str) and x.strip() != ""
                else []
            )

            max_len = split_lists.map(len).max()
            if not max_len:  # no segments anywhere → optionally drop or leave as-is
                df_out.drop(columns=[col], inplace=True)
                continue

            # Pad lists to same length and convert to numeric
            padded = split_lists.map(lambda lst: lst + [None] * (max_len - len(lst)))
            segs = pd.DataFrame(padded.tolist(), index=df_out.index)
            segs = segs.apply(pd.to_numeric, errors="coerce")  # floats/NaN

            # Name new columns: <original>_0, <original>_1, ..., <original>_<max_len-1>
            segs.columns = [f"{col}_{i}" for i in range(max_len)]

            # Attach to output; optionally drop original VEC column
            df_out[segs.columns] = segs
            df_out.drop(columns=[col], inplace=True)

        return df_out


    
    def generate_longitudinal_section_dataframes(
        self
    ) -> List[pd.DataFrame]:
        """
        Generates dataframes for longitudinal sections. Stationary timestamp is used for result values.
        
        :param self: Instance of SIR_Model_Dataframes class
        :return: List of dataframes of the form [section_1_VL, section_1_RL, section_2_VL, section_2_RL, ..., section_lfdnr_VL, section_lfdnr_RL, ...]
        :rtype: List[DataFrame|GeoDataFrame]
        """

        df_agsn_model_data = self.generate_element_model_data_dataframe(self.ObjectTypes.AGSN_HydraulicProfile)
        df_agsn_model_data = df_agsn_model_data.sort_values('Lfdnr')

        """
        # Only include active 
        df_agsn_model_data["Aktiv"] = df_agsn_model_data["Aktiv"].astype(str)
        df_agsn_model_data = df_agsn_model_data[df_agsn_model_data["Aktiv"] == "101"]
        """

        dfs = []

        for tk, lfdnr, name in df_agsn_model_data[['tk', 'Lfdnr', 'Name']].itertuples(index=False):

            # --- Retrieve Hydraulic Profile
            logger.info(f"Retrieving Hydraulic Profile with Lfdnr: {lfdnr}.")
            try:
                hydraulicProfile = self.GetCourseOfHydraulicProfile(tkAgsn=tk, uid="0")
                if hydraulicProfile.nrOfBranches != 0:
                    logger.info(f"Method does not work for longitudinal sections with branches. Not including hydraulic profile: {lfdnr}.")
                    continue
                # VL
                nodes_VL = list(hydraulicProfile.nodesVL)
                links_VL = list(hydraulicProfile.linksVL)
                x_VL = list(hydraulicProfile.xVL)
                x_VL = x_VL[1:]
                links_VL_tk_to_x_sum = dict(zip(links_VL, x_VL))
                df_pipes_VL, _ = self.generate_element_dataframe(element_type=self.ObjectTypes.Pipe
                                                            ,tks=links_VL)
                if df_pipes_VL is None or df_pipes_VL.empty:
                    logger.warning(f"No VL pipe dataframe generated for Hydraulic Profile with Lfdnr: {lfdnr}. Skipping profile.")
                    continue
                df_pipes_VL["l_sum"] = df_pipes_VL["tk"].map(links_VL_tk_to_x_sum)
                df_pipes_VL["AGSN_Lfdnr"] = lfdnr
                df_pipes_VL["AGSN_Name"] = name
                df_pipes_VL.sort_values(by='l_sum', ascending=True, inplace=True)
                df_pipes_VL = df_pipes_VL.reset_index(drop=True)
                    
                # RL
                nodes_RL = list(hydraulicProfile.nodesRL)
                links_RL = list(hydraulicProfile.linksRL)
                x_RL = list(hydraulicProfile.xRL)
                x_RL = x_RL[1:]
                links_RL_tk_to_x_sum = dict(zip(links_RL, x_RL))
                df_pipes_RL, _ = self.generate_element_dataframe(element_type=self.ObjectTypes.Pipe
                                                            ,tks=links_RL)
                if df_pipes_RL is None or df_pipes_RL.empty:
                    logger.warning(f"No RL pipe dataframe generated for Hydraulic Profile with Lfdnr: {lfdnr}. Skipping profile.")
                    continue
                df_pipes_RL["l_sum"] = df_pipes_RL["tk"].map(links_RL_tk_to_x_sum)
                df_pipes_RL["AGSN_Lfdnr"] = lfdnr
                df_pipes_RL["AGSN_Name"] = name
                df_pipes_RL.sort_values(by='l_sum', ascending=True, inplace=True)
                df_pipes_RL = df_pipes_RL.reset_index(drop=True)
                
                dfs_pipes_tuple = (df_pipes_VL, df_pipes_RL)
                dfs.append(dfs_pipes_tuple)
            except Exception as e:
                logger.error(f"Error retrieving Hydraulic Profile with Lfdnr: {lfdnr}: {e}")
                return []

        return dfs
    
    def generate_edge_dataframe(
        self,
        properties: Optional[List[str]] = [],      
        timestamps: Optional[Union[List[str], List[int]]] = None,
        tks: Optional[List[str]] = None
    ) -> Tuple[pd.DataFrame, dict]:

        """
        Generate one combined dataframe for all supported edge element types.

        The function retrieves requested model data and result data for each supported
        edge type, merges both per type, and concatenates all edge-type dataframes into
        one unified dataframe. Result values are written in the df as tuple of floats (or tuple (time) of tuple (interior point) of floats for pipe interior points) with each entry corresponding to a simulations timestamp. 

        Supported edge element types are:
        'Pipe', 'Valve', 'SafetyValve', 'PressureRegulator', 'DifferentialRegulator',
        'FlapValve', 'PhaseSeparation', 'FlowControlUnit', 'ControlValve', 'Pump',
        'DistrictHeatingConsumer', 'DistrictHeatingFeeder', 'Compressor', 'HeaterCooler', 'HeatFeederConsumerStation'.

        Not supported:
        'HeatExchanger'

        :param properties: Properties requested across all edge types. Each property is
                           validated per element type and split into model-data vs. result
                           properties. Unknown properties are ignored for that type.
                           Default: []. Meaning only tk, Fkcont, geometry, fkKI, fkKK, element_type, L (L=0, if missing) will be given as default cols in df_edges.
        :type properties: list[str], optional
        :param timestamps: Timestamps to use when retrieving result properties.
                           Supports timestamp string (eg. timestamps=['2023-02-13 08:00:00.000 +01:00', '2023-02-13 09:00:00.000 +01:00']) or int index (eg. timestamps=[8, 9]. corresponding to simulation timestamps self.GetTimeStamps()[0])
                           Default: self.GetTimeStamps()[1].(Stationary)
        :type timestamps: Union[List[str], List[int]], optional
        :param tks: TKs of elements to exclusively make up the dataframe. 
        :type tks: List[str], optional

        :return: A dataframe containing all retrieved edges across supported types.
                 Column sets are aligned across edge types before concatenation, so
                 properties not available for some types remain empty (NaN).
                 If no edge rows are available, an empty dataframe is returned. 
                 Dict mapping timestamps to tuple indices for result values is also returned.
        :rtype: tuple[pd.DataFrame, dict[str, int]]
        """

        edge_types = [
            'Pipe', 'Valve', 'SafetyValve', 'PressureRegulator', 'DifferentialRegulator',
            'FlapValve', 'PhaseSeparation', 'FlowControlUnit', 'ControlValve', 'Pump',
            'DistrictHeatingConsumer', 'DistrictHeatingFeeder', 'Compressor', 'HeaterCooler', 'HeatFeederConsumerStation'
        ]

        try:
            logger.info(f"[edge dataframe] Generating edge dataframe ...")
            if timestamps is None:
                ts = self.GetTimeStamps()[1]
                timestamps = [ts] # stationary
            enum_members = self.__get_object_type_enums(edge_types, self.ObjectTypes)
            dfs = []
            enume_members_used = 0
            timestamp_to_tuple_index = {}
            tks_filter_active = False
            remaining_tks = []
            if tks:
                tks_filter_active = True
                logger.info(f"[edge dataframe] TK filtering active. Requested tks: {tks}")
                remaining_tks = list(tks)
            for em in enum_members:
                tks_available = self.GetTksofElementType(ElementType=em)
                if tks_available:
                    if tks_filter_active:
                        set_tks = set(remaining_tks)
                        set_tks_available = set(tks_available)
                        tks_to_use = list(set_tks & set_tks_available)
                        remaining_tks = list(set_tks - set_tks_available)
                        if not tks_to_use:
                            continue
                    else:
                        tks_to_use = None

                    logger.info(f"[edge dataframe] Generating dataframe for {em} ...")
                    enume_members_used += 1
                    model_data_matches, result_matches, uncategorized = self.__sort_properties_into_model_data_and_results(element_type=em, properties=properties)
                    model_data_properties = list(model_data_matches)
                    if "Fkcont" not in model_data_properties:
                        model_data_properties.append("Fkcont")
                    result_properties = result_matches
                    
                    df_model = self.generate_element_model_data_dataframe(
                        element_type=em,
                        properties=model_data_properties,
                        geometry=True,
                        end_nodes=True,
                        element_type_col=True,
                        tks=tks_to_use
                    )
                    if "L" not in df_model.columns:
                        df_model["L"] = 0

                    df_results = self.generate_element_results_dataframe(
                        element_type=em,
                        properties=result_properties,
                        timestamps=timestamps,
                        tks=tks_to_use
                    )
                    df_results = self.add_interior_points_to_start_end_sequence(df_results)
                    df_results, timestamp_to_tuple_index_new = self.convert_rows_to_single_tuple_row(df_results)
                    if timestamp_to_tuple_index_new:
                        timestamp_to_tuple_index = timestamp_to_tuple_index_new
                    df = self.merge_model_data_and_results(df_model, df_results)
                    
                    dfs.append(df)
                    logger.info(f"[edge dataframe] Generated dataframe for {em}.")
            if not dfs:
                logger.warning("[edge dataframe] No edge dataframes were created. Returning empty dataframe.")
                return pd.DataFrame(), dict()

            if tks_filter_active:
                if len(remaining_tks) > 0:
                    logger.warning(f"[edge dataframe] The following tks were requested but not found in any edge element type and thus not included in the dataframe: {remaining_tks}")

            # Align column sets across edge types so missing properties stay empty (NaN)
            all_columns = sorted(set().union(*(df.columns for df in dfs)))
            dfs_aligned = [df.reindex(columns=all_columns) for df in dfs]

            df_edges = pd.concat(dfs_aligned, ignore_index=True, sort=False)
            logger.info(f"[edge dataframe] Retrieved {len(df_edges)} edges from {enume_members_used} element types.")
        except Exception as e:
            logger.error(f"[edge dataframe] Failed to retrieve edges: {e}")
            return pd.DataFrame(), dict()

        return df_edges, timestamp_to_tuple_index
        
    def __get_object_type_enums(self, names, enum_class):
        return [getattr(enum_class, name) for name in names if hasattr(enum_class, name)]

    ## Dataframe Creation: Helpers

    def merge_model_data_and_results(self, df_model_data, df_results):
        try:
            if df_results is None or df_results.empty or len(df_results.columns) == 0:
                return df_model_data.copy()

            if not df_results.empty and df_results.index.nunique() > 1:
                logger.error( "[merge] Aborting merge: df_results contains multiple timestamps.Please provide a single timestamp.")
                return pd.DataFrame()

            df_results.columns = df_results.columns.droplevel([1, 2])
            df_results = df_results.T.unstack(level=0).T
            df_results = df_results.droplevel(0, axis=0)
            df = df_model_data.merge(on="tk",
                                           how="outer",
                                           right=df_results)
            return df
        except Exception as e:
            logger.error(f"[merge] Error merging model data and results: {e}")
            return pd.DataFrame()

    def __sort_properties_into_model_data_and_results(
        self, 
        element_type: Enum,
        properties: List[str],
    ) -> Tuple[List[str], List[str], List[str]]:
        """
        Sorts the given properties into three categories:
        - model_data properties
        - Result properties
        - Uncategorized properties (not found in either model_data or result properties)
        
        Args:
            element_type (Enum): The type of element to query properties for.
            properties (List[str]): The list of properties to sort.
        
        Returns:
            Tuple[List[str], List[str], List[str]]: A tuple containing three lists:
                - model_data_matches
                - result_matches
                - uncategorized
        """
        model_data_properties = self.GetPropertiesofElementType(ElementType=element_type)
        result_properties = self.GetResultProperties_from_elementType(elementType=element_type, onlySelectedVectors=False)

        model_data_matches = [prop for prop in properties if prop in model_data_properties]
        result_matches = [prop for prop in properties if prop in result_properties]
        uncategorized = [prop for prop in properties if prop not in model_data_properties and prop not in result_properties]

        return model_data_matches, result_matches, uncategorized

    def __decapitalize(s: str) -> str:
        return s[:1].lower() + s[1:] if s else s

    def get_EPSG(self
    ) -> Tuple[str]:
        """
        Returns SRID, SRID and combined String. For example: ('25832', '1571', '25832-1571')
        """
        
        tk_SIRGRAF = self.GetTksofElementType(self.ObjectTypes.SIRGRAF)[0]
        srid = str(self.GetValue(tk_SIRGRAF, "Srid")[0])
        srid2 = str(self.GetValue(tk_SIRGRAF, "Srid2")[0])
        srid_string = self.GetValue(tk_SIRGRAF, "SridString")[0]

        return srid, srid2, srid_string
    
    def __resolve_given_tks(
        self,
        element_type: Enum,
        tks: Optional[List[str]] = None,
        filter_container_tks: Optional[List[str]] = None
    ) -> List:

        # --- Collect device keys (tks) ---
        try:
            available_tks = self.GetTksofElementType(ElementType=element_type)
            logger.info(f"[Resolving tks] Retrieved {len(available_tks)} element(s) of element type {element_type}.")
        except Exception as e:
            logger.error(f"[model_data] Error retrieving element tks: {e}")
            return pd.DataFrame()
        
        if len(available_tks) < 1:
            logger.warning(f"[Resolving tks] No elements exist of this element type {element_type}.")
            return pd.DataFrame()
        
        # --- Filter for given tks ---
        given_tks = tks
        if tks:
            try:
                for tk in tks:
                    if tk not in available_tks:
                        logger.warning(f"[Resolving tks] {tk} does not exist or is not of element type {element_type}. Excluding.")
                        tks.remove(tk)
                if len(tks) < 1:
                    logger.error(f"[Resolving tks] No elements remain after filtering for given tks: {given_tks}")
                    return pd.DataFrame()
                else:
                    logger.info(f"[Resolving tks] {len(tks)} tks remain after filtering for given tks.")

            except Exception as e:
                logger.error(f"[Resolving tks] Error validating given tks: {e}")
                return pd.DataFrame()
            
        else:
            tks = available_tks
            
        
        # --- Filer for container tk list ---
        if filter_container_tks:
            try:
                all_container_tks = self.GetTksofElementType(self.ObjectTypes.ObjectContainerSymbol)
                for tk in filter_container_tks[:]:
                    if tk not in all_container_tks:
                        logger.warning(f"[Resolving tks] Removed invalid container tk: {tk}. Proceeding without it.")
                        filter_container_tks.remove(tk)

                if filter_container_tks:
                    tks = [tk for tk in tks if self.GetValue(tk, "FkCont")[0] in filter_container_tks]
                if len(tks) < 1:
                    logger.error(f"[Resolving tks] No elements remain after container filtering.")
                    return []
                logger.info(f"[Resolving tks] {len(tks)} tks remain after container filtering.")
            except Exception as e:
                logger.error(f"[Resolving tks] Error occured while filtering with filter_container_tks: {e}")

        return tks
    
    def _resolve_given_timestamps(self, timestamps: Optional[List[Union[str, int]]]) -> List[str]:
        """
        Resolve the list of timestamps to use:
        - If `timestamps` is None: use all simulation timestamps (if available) else STAT.
        - If list contains integers: treat them as indices into the available timestamps.
        - If list contains strings: treat them as actual timestamp strings.
        - Validate against available timestamps and filter out invalid ones.

        Returns
        -------
        List[str]
            A list of valid timestamp strings (possibly empty).
        """
        # Single GetTimeStamps() call covering both the "no timestamps given" and the "validate given
        # timestamps" cases below (previously two separate calls, one per case, when timestamps was
        # None - a real, measured cost: ~0.5s per call, this alone was a quarter of one profiled
        # generate_element_results_dataframe() call's total GetTimeStamps() time).
        try:
            simulation_timestamps, tsStat, tsMin, tsMax = self.GetTimeStamps()
        except Exception as e:
            logger.error(f"[Resolving Timestamps] Error retrieving timestamps: {e}")
            return []

        # --- Default timestamp resolution ---
        if timestamps is None:
            logger.info("[Resolving Timestamps] No timestamps were given. Checking available simulation timestamps (SIR3S_Model.GetTimeStamps()[0]).")
            if simulation_timestamps:
                timestamps = simulation_timestamps
                logger.info(f"[Resolving Timestamps] {len(timestamps)} simulation timestamp(s) are available.")
            else:
                logger.warning("[Resolving Timestamps] No valid simulation timestamps exist in result data.")
                return []

        # --- Validate given timestamps ---
        try:
            available_timestamps = list(simulation_timestamps) if simulation_timestamps else []

            valid_timestamps = []

            # Check if input is list of integers (indices)
            if isinstance(timestamps[0], int):
                for idx in timestamps:
                    try:
                        resolved_ts = available_timestamps[idx]
                        valid_timestamps.append(resolved_ts)
                    except IndexError:
                        logger.warning(f"[Resolving Timestamps] Index {idx} out of bounds for available timestamps. It will be excluded.")
            else:
                # Assume list of timestamp strings
                for ts in timestamps:
                    if ts in available_timestamps:
                        valid_timestamps.append(ts)
                    else:
                        logger.warning(
                            f"[Resolving Timestamps] Timestamp {ts} is not valid (SIR3S_Model.GetTimeStamps()). It will be excluded."
                        )

            if len(valid_timestamps) == 1 and tsStat == valid_timestamps[0]:
                logger.info(f"[Resolving Timestamps] Only static timestamp {tsStat} is used")
            else:
                logger.info(f"[Resolving Timestamps] Using {len(valid_timestamps)} timestamps: {valid_timestamps}")
            return valid_timestamps
        except Exception as e:
            logger.error(f"Error validating timestamps: {e}")
            return []

    def __resolve_given_model_data_properties(
        self,
        element_type: Enum,
        properties: Optional[List[str]] = None,
    ) -> List[str]:
        """
        Checks the validity of given list of model_data properties. 
        If properties=None => All available properties will be used
        If properties=[] => No properties will be used
        """

        try:
            available_model_data_props = self.GetPropertiesofElementType(ElementType=element_type)
            available_result_props = self.GetResultProperties_from_elementType(
                elementType=element_type,
                onlySelectedVectors=False
            )

            model_data_props: List[str] = []

            if properties is None:
                logger.info(f"[Resolving model_data Properties] No properties given → using ALL model_data properties for {element_type}.")
                model_data_props = available_model_data_props
            else:
                for prop in properties:
                    if prop in available_model_data_props:
                        model_data_props.append(prop)
                    elif prop in available_result_props:
                        logger.warning(f"[Resolving model_data Properties] Property '{prop}' is a RESULT property; excluded from model_data.")
                    else:
                        logger.warning(
                            f"[Resolving model_data Properties] Property '{prop}' not found in model_data or result properties of type {element_type}. Excluding."
                        )

            logger.info(f"[Resolving model_data Properties] Using {len(model_data_props)} model_data properties.")
       
        except Exception as e:
            logger.error(f"[Resolving model_data Properties] Error resolving model_data properties: {e}")
        
        return model_data_props

    def __is_get_endnodes_applicable(self, element_type):
        element_type_net = self.to_dotnet_enum(element_type)
        dummy, _insert_error = self.toolkit.InsertElement(
            element_type_net,
            "[Toolkit: __is_get_endnodes_applicable()]: to be deleted",
        )

        if dummy == "-1":
            return True

        try:
            return_value, _fkKI, _fkKK, _fkKI2, _fkKK2, error = self.toolkit.GetEndNodes(dummy)
            error_text = str(error).lower() if error is not None else ""
            if not return_value and (
                "doesnt apply to such type of elements" in error_text
                or "doesn't apply to such type of elements" in error_text
            ):
                return False
            return True
        except Exception as ex:
            error_text = str(ex).lower()
            if (
                "doesnt apply to such type of elements" in error_text
                or "doesn't apply to such type of elements" in error_text
            ):
                return False
            return True
        finally:
            self.toolkit.DeleteElement(dummy)

    ## MX read helpers here

    def get_current_mx1_filepath(self, dot_resolution: int = 1) -> str:
        """
        Build the absolute path to the .MX1 result metadata file of the currently open model.

        Derived from the model's working directory (GetWorkingDirectory()) and its model identifier
        (self.Mid, e.g. "M-1-0-1"): the three numbers in Mid become the B/V/BZ subdirectories, e.g.:
        "<working_directory>\\B1\\V0\\BZ1\\M-1-0-1.1.MX1"

        TODO before shipping: dot_resolution is currently assumed to always be 1; confirm where this
        value actually comes from before relying on this in production.

        :param dot_resolution: The dot-resolution segment of the .MX1 filename (the ".Y" from 90-10 on).
                        Default: 1 (current assumption, unverified for all cases).
        :type dot_resolution: int, optional
        :return: Absolute path to the .MX1 file of the currently open model. Existence of the file is
                        not checked here.
        :rtype: str
        """
        if not self.Mid:
            raise ValueError(
                "[get_current_mx1_filepath] No model is open (self.Mid is not set). Call OpenModel() first."
            )

        parts = self.Mid.split("-")
        if len(parts) != 4 or parts[0] != "M":
            raise ValueError(
                f"[get_current_mx1_filepath] Unexpected Mid format: {self.Mid!r}. Expected 'M-<b>-<v>-<bz>'."
            )
        _, b, v, bz = parts

        working_directory = self.GetWorkingDirectory()
        if not working_directory:
            raise ValueError("[get_current_mx1_filepath] GetWorkingDirectory() returned no working directory.")

        mx1_filename = f"{self.Mid}.{dot_resolution}.MX1"
        mx1_filepath = os.path.join(working_directory, f"B{b}", f"V{v}", f"BZ{bz}", mx1_filename)

        return mx1_filepath

    def _resolve_mx_file_paths(self, mx1_filepath: str) -> dict:
        """
        Pure path derivation (no file reads, no existence checks) from an .MX1 filepath: the
        corresponding .MX2/.MXS/.ZIP paths, dot_resolution, working dir and base name. Factored out of
        initialize_mx_read_helpers() so callers that only need the paths (e.g. the on-disk Tier 1 cache,
        which has to know the .MXS path before deciding whether a full MX1/MX2 parse is needed) can
        reuse the same derivation.

        :param mx1_filepath: Absolute or relative path to an .MX1 file (e.g. "...\\M-1-0-1.1.MX1").
        :type mx1_filepath: str
        :return: dict with keys "mx1", "mx2", "mxs", "mxs_zip", "dot_resolution", "work_dir", "base".
        :rtype: dict
        """
        w_d, file_name = os.path.split(mx1_filepath)
        base, _ext = os.path.splitext(file_name)
        base, dot_resolution = os.path.splitext(base)

        return {
            "mx1": mx1_filepath,
            "mx2": os.path.join(w_d, f"{base}.MX2"),
            "mxs": os.path.join(w_d, f"{base}{dot_resolution}.MXS"),
            "mxs_zip": os.path.join(w_d, f"{base}{dot_resolution}.ZIP"),
            "dot_resolution": dot_resolution,
            "work_dir": w_d,
            "base": base,
        }

    def _mx_cache_filepath(self, mx_paths: dict, cache_suffix: Optional[str]) -> str:
        """
        Build the on-disk Tier 1 cache path next to the .MX1 file: "mxcache.zip" by default, or
        "mxcache.{cache_suffix}.zip" for a named/archived snapshot (see
        generate_element_results_dataframe()'s mx_cache_suffix param).

        Deliberately excludes the .MX1 base name and dot_resolution - the containing directory already
        disambiguates by Mid, and dot_resolution is currently hardcoded to 1 everywhere (see
        get_current_mx1_filepath()'s TODO). TODO before shipping, together with that: once multiple
        resolutions are supported, this will need a resolution-keyed name to avoid collisions.

        Only the default (cache_suffix=None) file is ever written by this codebase - a suffixed one is
        expected to be created manually, by copying/renaming a previously-written default cache file.

        :param mx_paths: Result of _resolve_mx_file_paths() (or self._mx_paths).
        :type mx_paths: dict
        :param cache_suffix: None for the default/live cache file, or a name for an archived snapshot.
        :type cache_suffix: Optional[str]
        :return: Absolute path to the cache file (existence not checked here).
        :rtype: str
        """
        work_dir = mx_paths["work_dir"]
        suffix_part = "" if cache_suffix is None else f".{cache_suffix}"
        return os.path.join(work_dir, f"mxcache{suffix_part}.zip")

    def _write_mx_cache_file(
        self,
        path: str,
        raw_df: pd.DataFrame,
        mx1_df: pd.DataFrame,
        mx2_df: pd.DataFrame,
        signature: Tuple[float, int],
    ) -> None:
        """
        Write a Tier 1 cache to disk: a zip file bundling the raw-results dataframe (read_mx_results()'s
        shape) together with the MX1 and MX2 dataframes it was resolved from, each as its own Feather
        entry, plus a small meta.json holding ``signature`` (the source .MXS file's (mtime, size), so a
        later read can verify freshness without re-parsing the .MXS).

        Bundling MX1/MX2 in means a later read - especially of an archived snapshot, see
        generate_element_results_dataframe()'s mx_cache_suffix param - never has to touch the live
        .MX1/.MX2 files, so it stays correct even if the model's topology has since changed. See
        _apply_mx1_mx2().

        Written atomically (temp file + os.replace()) so a concurrent reader never observes a
        partially-written file.

        :param path: Destination file path.
        :type path: str
        :param raw_df: The Tier 1 raw-results dataframe to persist.
        :type raw_df: pd.DataFrame
        :param mx1_df: The parsed MX1 dataframe (self._mx1_df) this raw_df was resolved with.
        :type mx1_df: pd.DataFrame
        :param mx2_df: The parsed MX2 dataframe (self._mx2_df) this raw_df was resolved with.
        :type mx2_df: pd.DataFrame
        :param signature: (mtime, size) of the source .MXS file raw_df was read from.
        :type signature: Tuple[float, int]
        """
        import pyarrow as pa
        import pyarrow.ipc as pa_ipc

        def _feather_bytes(df: pd.DataFrame) -> bytes:
            # Feather V2 *is* the Arrow IPC file format (pyarrow.feather.write_feather()/read_table()
            # are, as of pyarrow 24, a deprecated convenience wrapper around exactly this) - writing via
            # pyarrow.ipc.new_file() directly avoids that deprecation without changing the file format.
            table = pa.Table.from_pandas(df)
            buf = io.BytesIO()
            with pa_ipc.new_file(buf, table.schema) as writer:
                writer.write_table(table)
            return buf.getvalue()

        # mx2_df's "Data" column holds one tuple per row, but the tuples' element type varies row to
        # row (strings for tk/pk rows, ints for the N_OF_POINTS row) - a single Arrow list type can't
        # represent that (pyarrow's from_pandas() type inference fails, e.g. trying to convert a tk
        # string like "5393031835236689087" to int64). JSON-encoding each row's tuple into a plain
        # string column sidesteps needing one consistent Arrow list type, and round-trips both element
        # types exactly (JSON distinguishes numbers from strings) without depending on the "DataType"
        # column to decide how to decode each row.
        mx2_df_for_storage = mx2_df.reset_index(drop=True).copy()
        mx2_df_for_storage["Data"] = mx2_df_for_storage["Data"].apply(lambda t: json.dumps(list(t)))

        tmp_path = f"{path}.tmp-{os.getpid()}"
        try:
            with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                zf.writestr("raw.feather", _feather_bytes(raw_df.reset_index()))
                zf.writestr("mx1.feather", _feather_bytes(mx1_df.reset_index(drop=True)))
                zf.writestr("mx2.feather", _feather_bytes(mx2_df_for_storage))
                zf.writestr("meta.json", json.dumps({"signature": list(signature)}))
            os.replace(tmp_path, path)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def _read_mx_cache_file(
        self, path: str
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, Optional[Tuple[float, int]]]:
        """
        Read an on-disk Tier 1 cache zip file back - see _write_mx_cache_file().

        :param path: Cache file path.
        :type path: str
        :return: (raw_df, mx1_df, mx2_df, signature) - signature is the embedded (mtime, size) tuple
                        the file was written with, or None if missing (e.g. hand-crafted meta.json).
        :rtype: Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, Optional[Tuple[float, int]]]
        """
        import pyarrow.ipc as pa_ipc

        def _read_feather_entry(zf: zipfile.ZipFile, name: str) -> pd.DataFrame:
            return pa_ipc.open_file(io.BytesIO(zf.read(name))).read_all().to_pandas()

        with zipfile.ZipFile(path, "r") as zf:
            raw_df = _read_feather_entry(zf, "raw.feather").set_index("TIMESTAMP")
            mx1_df = _read_feather_entry(zf, "mx1.feather")
            mx2_df = _read_feather_entry(zf, "mx2.feather")
            meta = json.loads(zf.read("meta.json").decode("utf-8"))

        # Reverse the JSON-encoding _write_mx_cache_file() applies to mx2_df's "Data" column - see its
        # docstring for why (heterogeneous per-row element types, which a single Arrow list type can't
        # represent directly).
        mx2_df["Data"] = mx2_df["Data"].apply(json.loads)

        signature = tuple(meta["signature"]) if "signature" in meta else None
        return raw_df, mx1_df, mx2_df, signature

    def initialize_mx_read_helpers(self, mx1_filepath: str) -> dict:
        """
        Initialize MX read helper state from an MX1 filepath.

        This method mirrors the legacy initialization sequence:
        parse MX1, parse MX2, build record-unpack format, then build channel indices.

        :param mx1_filepath: Absolute or relative path to .MX1 file.
        :type mx1_filepath: str
        :return: Summary dictionary with resolved paths and basic counts.
        :rtype: dict
        """
        logger.info("[mx helpers] Initializing MX read helpers ...")

        if not isinstance(mx1_filepath, str) or mx1_filepath.strip() == "":
            raise ValueError("[mx helpers] mx1_filepath must be a non-empty string.")

        if not os.path.exists(mx1_filepath):
            raise FileNotFoundError(f"[mx helpers] MX1 file does not exist: {mx1_filepath}")

        mx_paths = self._resolve_mx_file_paths(mx1_filepath)
        mx1_df = self._parse_mx1_to_dataframe(mx1_filepath)
        mx2_df = self._parse_mx2_to_dataframe(mx_paths["mx2"])
        self._apply_mx1_mx2(mx_paths, mx1_df, mx2_df)

        return {
            "paths": self._mx_paths,
            "mx1_rows": len(self._mx1_df.index),
            "mx2_rows": len(self._mx2_df.index),
            "non_vector_channels": len(self._mx_layout["mx_column_names"]),
            "vector_channels": len(self._mx_layout["mx_column_names_vecs"]),
        }

    def _apply_mx1_mx2(self, mx_paths: dict, mx1_df: pd.DataFrame, mx2_df: pd.DataFrame) -> None:
        """
        Populate self's MX1/MX2-derived state (self._mx_paths, self._mx1_df, self._mx2_df,
        self._mx_record_struct_fmt_string, self._mx_layout) from already-available mx1_df/mx2_df
        dataframes.

        Shared by initialize_mx_read_helpers() (mx1_df/mx2_df freshly parsed from the live .MX1/.MX2
        files) and _get_mx_raw_results_cache()'s cache-hit paths (mx1_df/mx2_df restored from a cached
        or archived mxcache.zip instead, without touching the live .MX1/.MX2 files - which is what
        keeps an archived snapshot correct even after the model's topology has since changed).

        :param mx_paths: Result of _resolve_mx_file_paths().
        :type mx_paths: dict
        :param mx1_df: Parsed (or cache-restored) MX1 dataframe.
        :type mx1_df: pd.DataFrame
        :param mx2_df: Parsed (or cache-restored) MX2 dataframe.
        :type mx2_df: pd.DataFrame
        """
        self._mx_paths = mx_paths
        self._mx1_df = mx1_df
        self._mx2_df = mx2_df
        self._mx_record_struct_fmt_string, self._mx1_df = self._build_mx_record_unpack_format(self._mx1_df)
        self._mx_layout = self._build_mx_record_unpack_layout(self._mx1_df)

        logger.info(
            "[mx helpers] MX1/MX2 state ready. MX1 rows: %d, MX2 rows: %d, non-vector channels: %d, vector channels: %d",
            len(self._mx1_df.index),
            len(self._mx2_df.index),
            len(self._mx_layout["mx_column_names"]),
            len(self._mx_layout["mx_column_names_vecs"]),
        )

    def _parse_mx1_to_dataframe(self, mx1_filepath: str) -> pd.DataFrame:
        """
        Parse an MX1 XML file to a dataframe and add derived helper columns.

        :param mx1_filepath: Path to .MX1 XML file.
        :type mx1_filepath: str
        :return: Parsed MX1 dataframe including vector flags and Sir3sID.
        :rtype: pd.DataFrame
        """
        logger.info(f"[mx helpers] Parsing MX1: {mx1_filepath}")

        mx1_tree = ET.parse(mx1_filepath)
        mx1_root = mx1_tree.getroot()

        all_records = []
        for mx_channel in mx1_root.findall("XL1"):
            record = {attr_name: mx_channel.get(attr_name) for attr_name in sorted(mx_channel.keys())}
            all_records.append(record)

        mx1_df = pd.DataFrame(all_records)
        if mx1_df.empty:
            raise ValueError(f"[mx helpers] Parsed MX1 is empty: {mx1_filepath}")

        for col in ["DATALENGTH", "DATATYPELENGTH", "DATAOFFSET", "FLAGS"]:
            mx1_df[col] = pd.to_numeric(mx1_df[col], errors="raise").astype("int64")

        sep = "~"
        mx1_df["Sir3sID"] = (
            mx1_df["OBJTYPE"].astype(str)
            + sep
            + mx1_df["NAME1"].astype(str)
            + sep
            + mx1_df["NAME2"].astype(str)
            + sep
            + mx1_df["OBJTYPE_PK"].astype(str)
            + sep
            + mx1_df["ATTRTYPE"].astype(str)
        )

        mx1_df["NOfItems"] = [
            int(data_length / data_type_length)
            for data_length, data_type_length in zip(mx1_df["DATALENGTH"], mx1_df["DATATYPELENGTH"])
        ]

        mx1_df["is_vector_channel"] = [
            True if n_items > 1 or (len(objtype_pk) < 3 and objtype != "ALLG") else False
            for n_items, objtype_pk, objtype in zip(mx1_df["NOfItems"], mx1_df["OBJTYPE_PK"], mx1_df["OBJTYPE"])
        ]

        mx1_df["is_vector_channel_mx2"] = [
            True if is_vector and flags >= 4 and bin(flags)[-3] == "1" else False
            for is_vector, flags in zip(mx1_df["is_vector_channel"], mx1_df["FLAGS"])
        ]

        mx1_df["is_vector_channel_mx2_rvec"] = [
            True if is_mx2_vector and data_type == "RVEC" else False
            for is_mx2_vector, data_type in zip(mx1_df["is_vector_channel_mx2"], mx1_df["DATATYPE"])
        ]

        logger.info(f"[mx helpers] Parsed MX1 successfully. Shape: {mx1_df.shape}")
        return mx1_df

    def _parse_mx2_to_dataframe(self, mx2_filepath: str) -> pd.DataFrame:
        """
        Parse an MX2 binary file to a dataframe.

        :param mx2_filepath: Path to .MX2 binary file.
        :type mx2_filepath: str
        :return: Parsed MX2 dataframe.
        :rtype: pd.DataFrame
        """
        logger.info(f"[mx helpers] Parsing MX2: {mx2_filepath}")

        if not os.path.exists(mx2_filepath):
            raise FileNotFoundError(f"[mx helpers] MX2 file does not exist: {mx2_filepath}")

        header_fmt_string = "12s12s4si28xi"
        all_records = []

        with open(mx2_filepath, "rb") as f:
            offset_to_next_header = 0

            while True:
                header = f.read(64)
                header_length = len(header)

                if header_length != 64:
                    if header_length != 0:
                        logger.warning(
                            "[mx helpers] Unexpected MX2 trailing header bytes: %d",
                            header_length,
                        )
                    break

                header_data = struct.unpack(header_fmt_string, header)

                obj_type = header_data[0].decode("utf-8").rstrip()
                attr_type = header_data[1].decode("utf-8").rstrip()
                data_type = header_data[2].decode("utf-8").rstrip()
                data_type_length = int(header_data[3])
                data_length = int(header_data[4])
                n_of_items = int(data_length / data_type_length)

                if data_type == "CHAR":
                    data_fmt_string = f"{data_type_length}s" * n_of_items
                elif data_type == "INT4":
                    data_fmt_string = "i" * n_of_items
                else:
                    data_fmt_string = f"{data_length}x"

                data_bytes = f.read(data_length)
                data = struct.unpack(data_fmt_string, data_bytes)

                if data_type == "CHAR":
                    data = [item.decode("utf-8").rstrip() for item in data]

                all_records.append(
                    {
                        "ObjType": obj_type,
                        "AttrType": attr_type,
                        "DataType": data_type,
                        "DataTypeLength": data_type_length,
                        "DataLength": data_length,
                        "NOfItems": n_of_items,
                        "Data": data,
                    }
                )

                offset_to_next_header += 64 + data_length
                if f.tell() != offset_to_next_header:
                    f.seek(offset_to_next_header)

        mx2_df = pd.DataFrame(all_records)
        logger.info(f"[mx helpers] Parsed MX2 successfully. Shape: {mx2_df.shape}")
        return mx2_df

    def _build_mx_record_unpack_format(self, mx1_df: pd.DataFrame) -> Tuple[str, pd.DataFrame]:
        """
        Build the struct unpack format string and unpack indices from MX1 metadata.

        :param mx1_df: MX1 dataframe.
        :type mx1_df: pd.DataFrame
        :return: Tuple of format string and MX1 dataframe with unpackIdx column.
        :rtype: Tuple[str, pd.DataFrame]
        """
        logger.info("[mx helpers] Building MX record unpack format ...")

        # Detect ALL unrecognized DATATYPEs up front, in one pass, rather than only ever discovering
        # them one at a time (the loop below still raises on the first one it reaches, same as before -
        # this is purely a better diagnostic: which channels, not just which type, and all of them at
        # once instead of a new crash per newly-added unknown type).
        unknown_datatypes = set(mx1_df["DATATYPE"]) - _KNOWN_MX_DATATYPES
        if unknown_datatypes:
            offending = mx1_df[mx1_df["DATATYPE"].isin(unknown_datatypes)][["Sir3sID", "DATATYPE"]]
            logger.error(
                f"[mx helpers] {len(unknown_datatypes)} unrecognized MX1 DATATYPE(s) found: "
                f"{sorted(unknown_datatypes)}. Affected channels:\n{offending.to_string(index=False)}"
            )

        fmt_string = ""
        unpack_idx = []
        idx_unpack = 0

        for row in mx1_df.itertuples():
            fmt_item = ""
            data_type = row.DATATYPE
            data_type_length = int(row.DATATYPELENGTH)
            data_length = int(row.DATALENGTH)
            n_items = int(row.NOfItems)
            is_vector_channel = bool(row.is_vector_channel)

            if data_type == "CHAR":
                unpack_idx.append(idx_unpack)
                if is_vector_channel:
                    fmt_item = f"{data_type_length}s" * n_items
                    idx_unpack += n_items
                else:
                    fmt_item = f"{data_length}s"
                    idx_unpack += 1
            elif data_type == "INT4":
                if data_type_length != 4:
                    raise ValueError(
                        f"[mx helpers] Invalid DATATYPELENGTH for INT4: {data_type_length}"
                    )
                unpack_idx.append(idx_unpack)
                fmt_item = f"{n_items}i" if is_vector_channel else "i"
                idx_unpack += n_items if is_vector_channel else 1
            elif data_type in {"REAL", "RVEC"}:
                if data_type_length != 4:
                    raise ValueError(
                        f"[mx helpers] Invalid DATATYPELENGTH for {data_type}: {data_type_length}"
                    )
                unpack_idx.append(idx_unpack)
                fmt_item = f"{n_items}f" if is_vector_channel else "f"
                idx_unpack += n_items if is_vector_channel else 1
            else:
                raise ValueError(f"[mx helpers] Unknown DATATYPE in MX1: {data_type}")

            fmt_string += fmt_item

        mx_record_length_mx1 = int(mx1_df["DATAOFFSET"].iloc[-1]) + int(mx1_df["DATALENGTH"].iloc[-1])
        mx_record_length_fmt = struct.calcsize(fmt_string)
        if mx_record_length_mx1 != mx_record_length_fmt:
            raise ValueError(
                "[mx helpers] Record size mismatch between MX1 metadata "
                f"({mx_record_length_mx1}) and struct format ({mx_record_length_fmt})."
            )

        mx1_df_with_unpack = mx1_df.copy()
        mx1_df_with_unpack["unpackIdx"] = pd.Series(unpack_idx, dtype="int64")

        logger.info(
            "[mx helpers] Built unpack format successfully. Record length: %d bytes",
            mx_record_length_fmt,
        )
        return fmt_string, mx1_df_with_unpack

    def _build_mx_record_unpack_layout(self, mx1_df: pd.DataFrame) -> dict:
        """
        Build channel layout indices and column-name lists for later MXS decoding.

        :param mx1_df: MX1 dataframe with unpackIdx and vector flags.
        :type mx1_df: pd.DataFrame
        :return: Dictionary with important indices and channel lists.
        :rtype: dict
        """
        logger.info("[mx helpers] Building MX unpack layout ...")

        idx_cverso = mx1_df.index[mx1_df["ATTRTYPE"] == "CVERSO"][0]
        idx_timestamp = mx1_df.index[mx1_df["ATTRTYPE"] == "TIMESTAMP"][0]
        idx_snapshottype = mx1_df.index[mx1_df["ATTRTYPE"] == "SNAPSHOTTYPE"][0]

        unpack_idx_cverso = int(mx1_df.loc[idx_cverso, "unpackIdx"])
        unpack_idx_timestamp = int(mx1_df.loc[idx_timestamp, "unpackIdx"])
        unpack_idx_snapshottype = int(mx1_df.loc[idx_snapshottype, "unpackIdx"])

        mx_column_names = []
        mx_column_names_vecs = []
        for row in mx1_df.itertuples():
            if int(row.unpackIdx) < 0:
                continue
            if bool(row.is_vector_channel):
                mx_column_names_vecs.append(row.Sir3sID)
            else:
                mx_column_names.append(row.Sir3sID)

        timestamp_sir3sid = mx1_df.loc[idx_timestamp, "Sir3sID"]
        if timestamp_sir3sid in mx_column_names:
            mx_column_names.remove(timestamp_sir3sid)

        idx_unpack_non_vector_channels = [
            int(mx1_df.iloc[idx]["unpackIdx"])
            for idx, is_vector in enumerate(mx1_df["is_vector_channel"])
            if not is_vector
        ]
        if unpack_idx_timestamp in idx_unpack_non_vector_channels:
            idx_unpack_non_vector_channels.remove(unpack_idx_timestamp)

        idx_unpack_vector_channels = [
            int(mx1_df.iloc[idx]["unpackIdx"])
            for idx, is_vector in enumerate(mx1_df["is_vector_channel"])
            if is_vector
        ]

        idx_of_non_vector_channels = [
            idx for idx, is_vector in enumerate(mx1_df["is_vector_channel"]) if not is_vector
        ]
        if idx_timestamp in idx_of_non_vector_channels:
            idx_of_non_vector_channels.remove(idx_timestamp)

        idx_of_vector_channels = [
            idx for idx, is_vector in enumerate(mx1_df["is_vector_channel"]) if is_vector
        ]

        layout = {
            "idx_cverso": idx_cverso,
            "idx_timestamp": idx_timestamp,
            "idx_snapshottype": idx_snapshottype,
            "unpack_idx_cverso": unpack_idx_cverso,
            "unpack_idx_timestamp": unpack_idx_timestamp,
            "unpack_idx_snapshottype": unpack_idx_snapshottype,
            "mx_column_names": mx_column_names,
            "mx_column_names_vecs": mx_column_names_vecs,
            "idx_unpack_non_vector_channels": idx_unpack_non_vector_channels,
            "idx_unpack_vector_channels": idx_unpack_vector_channels,
            "idx_of_non_vector_channels": idx_of_non_vector_channels,
            "idx_of_vector_channels": idx_of_vector_channels,
        }

        logger.info("[mx helpers] Built MX unpack layout successfully.")
        return layout

    def _discover_output_factors(self) -> Tuple[int, int]:
        """
        Discover the currently configured MX result-output factors (SIR 3S: TIMD.DTFAK_KLEIN /
        TIMD.DTFAK_GROSS) of the currently open model.

        These control how often the calculation core archives results: ``output_factor_small`` is the
        interval used for time-curve ("Zeitkurven") output, and ``output_factor_large`` is the interval
        used for numeric displays / longitudinal sections / network-graph coloring. Both end up as
        literal dot-resolution numbers in the resulting file names (e.g. "M-1-0-1.1.MX1") — see
        get_current_mx1_filepath(). If they're equal, only one resolution (and one file) exists.

        Implemented by exporting a throwaway SirCalc XML file (via WriteSirCalcXmlFile()) into a
        temporary directory that is deleted again afterwards; no existing result files are touched.

        KNOWN BUG, NOT CURRENTLY CALLED: read_mx_results() no longer calls this - see the TODO note on
        its ``mx1_filepath`` param. WriteSirCalcXmlFile() was found to leave GetResultfortimestamp()
        returning stale/frozen values for the rest of the session afterwards (a toolkit-side bug, not
        fixable from here). Re-enable the call in read_mx_results() once that's fixed.

        :return: (output_factor_small, output_factor_large)
        :rtype: Tuple[int, int]
        """
        if not self.Mid:
            raise ValueError(
                "[_discover_output_factors] No model is open (self.Mid is not set). Call OpenModel() first."
            )

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

        logger.info(
            f"[_discover_output_factors] output_factor_small={output_factor_small}, "
            f"output_factor_large={output_factor_large}."
        )
        return output_factor_small, output_factor_large

    def _resolve_given_mx_timestamps(self, timestamps: Optional[List[str]]) -> Optional[Set[pd.Timestamp]]:
        """
        Validate the format of timestamps passed to read_mx_results().

        Unlike _resolve_given_timestamps(), this does not check given entries against
        self.GetTimeStamps() of the currently open model, since read_mx_results() may target an .MX1
        file unrelated to whatever model (if any) is currently open. Each entry is only checked for
        being a parseable timestamp; whether it actually occurs in the .MXS file is determined naturally
        during the scan itself (non-matching records are simply skipped).

        :param timestamps: Timestamp strings to filter on, or None to keep every timestamp found in the file.
        :type timestamps: list[str], optional
        :return: Set of parsed timestamps to keep, or None (meaning: no filter, keep everything).
        :rtype: set[pandas.Timestamp], optional
        """
        if timestamps is None:
            return None

        resolved = set()
        for ts in timestamps:
            try:
                resolved.add(pd.to_datetime(ts))
            except Exception as e:
                logger.warning(f"[Resolving MX Timestamps] Timestamp {ts!r} is not parseable. It will be excluded: {e}")

        logger.info(f"[Resolving MX Timestamps] Using {len(resolved)} timestamp(s) to filter records.")
        return resolved

    def read_mx_results(
        self,
        mx1_filepath: Optional[str] = None,
        timestamps: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """
        Standalone MX result reader. Reads simulation results directly from the binary .MXS result file
        (via the .MX1/.MX2 metadata) instead of going through the SIR 3S Toolkit API.

        WORK IN PROGRESS: Not wired into generate_element_results_dataframe() or any other dataframe
        generation/filtering yet. Intended for checking the raw MX read against the legacy PT3S.Mx output.

        NOT HANDLED: SIR 3S can also write wall-clock-timestamped archive snapshots
        ("{base}_{YYYY-MM-DD_HH-MM}_UTC.{res}.MXS", gated by TIMD.JARCH/NARCH/JZEIT) alongside the
        regular "{base}.{res}.MXS" files - out of scope here, this function only targets the two
        deterministic per-resolution files.

        :param mx1_filepath: Absolute or relative path to .MX1 file.
                        Default: None. If not given, dot_resolution=1 is assumed and the path is built
                        via get_current_mx1_filepath(dot_resolution=1) - covers the common case where
                        only one output resolution exists.
                        TEMPORARY, TODO before shipping: this used to auto-discover the model's actual
                        output_factor_small/output_factor_large via _discover_output_factors() instead of
                        assuming 1/1, and raise if they differed. Disabled for now - see
                        _discover_output_factors()'s docstring for why. If your model actually has
                        output_factor_small != output_factor_large, dot_resolution=1 will silently pick
                        the wrong (or a nonexistent) file - pass mx1_filepath explicitly instead.
        :type mx1_filepath: str, optional
        :param timestamps: Timestamps to keep, in the same form as self.GetTimeStamps()'s strings.
                        Matching is done on the parsed instant, not the literal string. Every record in
                        the .MXS file is still scanned sequentially to read its TIMESTAMP field, but only
                        matching records pay the full per-channel unpack/decode cost.
                        Default: None (keep all TIMESTAMPs found in the file).
        :type timestamps: list[str], optional
        :return: DataFrame with one row per unique TIMESTAMP (first occurrence kept for duplicates, e.g.
                        the initial STAT/TIME pair) and one column per MX channel (Sir3sID:
                        OBJTYPE~NAME1~NAME2~tk~ATTRTYPE). Scalar channels hold their raw unpacked value;
                        vector channels (interior points) hold a tuple of raw unpacked values.
        :rtype: pd.DataFrame
        """
        if mx1_filepath is None:
            # TODO before shipping: this used to call self._discover_output_factors() here to look up
            # the model's actual TIMD.DTFAK_KLEIN/DTFAK_GROSS and raise a ValueError (naming both
            # candidate paths) if they differed - see _discover_output_factors()'s docstring and the
            # note on the mx1_filepath param above for why that's disabled (WriteSirCalcXmlFile(), which
            # it calls, was found to break the Toolkit API's own result reading for the rest of the
            # session). Re-enable this once that toolkit-side issue is fixed:
            #
            # output_factor_small, output_factor_large = self._discover_output_factors()
            # if output_factor_small != output_factor_large:
            #     path_small = self.get_current_mx1_filepath(dot_resolution=output_factor_small)
            #     path_large = self.get_current_mx1_filepath(dot_resolution=output_factor_large)
            #     raise ValueError(
            #         "[mx read] output_factor_small != output_factor_large "
            #         f"({output_factor_small} != {output_factor_large}, SIR 3S: TIMD.DTFAK_KLEIN/"
            #         "DTFAK_GROSS); two structurally different resolution files exist. "
            #         f"Pass mx1_filepath explicitly to pick one: {path_small!r} or {path_large!r}."
            #     )
            # mx1_filepath = self.get_current_mx1_filepath(dot_resolution=output_factor_small)
            #
            # For now: assume the common/default case (dot_resolution=1) instead. If that's wrong for
            # your model, pass mx1_filepath explicitly.
            mx1_filepath = self.get_current_mx1_filepath(dot_resolution=1)

        logger.info(f"[mx read] Reading MX results from: {mx1_filepath}")

        self.initialize_mx_read_helpers(mx1_filepath)

        mxs_filepath = self._mx_paths["mxs"]
        if not os.path.exists(mxs_filepath):
            raise FileNotFoundError(f"[mx read] MXS file does not exist: {mxs_filepath}")

        requested_times = self._resolve_given_mx_timestamps(timestamps)
        if requested_times is not None:
            logger.info(f"[mx read] Timestamp filter active: {len(requested_times)} requested timestamp(s).")

        record_length = struct.calcsize(self._mx_record_struct_fmt_string)
        mx_column_names = self._mx_layout["mx_column_names"]
        mx_column_names_vecs = self._mx_layout["mx_column_names_vecs"]
        idx_unpack_non_vector_channels = self._mx_layout["idx_unpack_non_vector_channels"]
        idx_of_vector_channels = self._mx_layout["idx_of_vector_channels"]
        idx_unpack_vector_channels = self._mx_layout["idx_unpack_vector_channels"]
        n_of_items = self._mx1_df["NOfItems"]

        # Byte offsets/lengths of CVERSO and TIMESTAMP within a raw record, so both can be read directly
        # from the record bytes without a full struct.unpack of all channels.
        cverso_offset = int(self._mx1_df.loc[self._mx_layout["idx_cverso"], "DATAOFFSET"])
        cverso_length = int(self._mx1_df.loc[self._mx_layout["idx_cverso"], "DATALENGTH"])
        timestamp_offset = int(self._mx1_df.loc[self._mx_layout["idx_timestamp"], "DATAOFFSET"])
        timestamp_length = int(self._mx1_df.loc[self._mx_layout["idx_timestamp"], "DATALENGTH"])

        time_delta_read_offset = None
        times = []
        rows = []

        with open(mxs_filepath, "rb") as f:
            f.seek(0, 2)
            file_size = f.tell()
            f.seek(0)

            records_read = 0
            records_decoded = 0
            while f.tell() < file_size:
                record = f.read(record_length)
                if len(record) != record_length:
                    if len(record) != 0:
                        logger.warning(f"[mx read] Unexpected trailing MXS bytes: {len(record)}")
                    break
                records_read += 1

                if time_delta_read_offset is None:
                    cverso = record[cverso_offset: cverso_offset + cverso_length].decode("utf-8")
                    match = re.search(r"SIR 3S (\d{2})-(\d{2})-(\d{2})-(\d{2})", cverso)
                    sub_version = int(match.group(2)) if match else 99
                    if sub_version < 10:
                        time_delta_read_offset = pd.to_timedelta("1 hour")
                    else:
                        time_delta_read_offset = pd.to_timedelta("0 seconds")

                timestamp_raw = record[timestamp_offset: timestamp_offset + timestamp_length]
                time = pd.to_datetime(timestamp_raw.decode("utf-8"), utc=True) + time_delta_read_offset

                if requested_times is not None and time not in requested_times:
                    continue

                record_data = struct.unpack(self._mx_record_struct_fmt_string, record)

                row = {}
                for col, idx in zip(mx_column_names, idx_unpack_non_vector_channels):
                    row[col] = record_data[idx]
                for col, idx_of, idx_unpack in zip(
                    mx_column_names_vecs, idx_of_vector_channels, idx_unpack_vector_channels
                ):
                    row[col] = record_data[idx_unpack: idx_unpack + int(n_of_items.iloc[idx_of])]

                times.append(time)
                rows.append(row)
                records_decoded += 1

        df = pd.DataFrame(rows, index=pd.Index(times, name="TIMESTAMP"), columns=mx_column_names + mx_column_names_vecs)
        df = df.loc[~df.index.duplicated(keep="first")]

        logger.info(
            f"[mx read] Done. Records scanned: {records_read}. Records decoded: {records_decoded}. "
            f"Unique timestamps: {len(df)}."
        )
        return df

    # Dataframe Operations

    def delete_elements_in_dataframe(
        self,
        dataframe: pd.DataFrame,
        tk_col: str = "tk",
    ) -> List[str]:
        """
        Delete all elements in a model that are present in the given dataframe, based on their tk in the specified column.

        :param dataframe: DataFrame containing the elements to delete. Must include a column with the element's tk.
        :type dataframe: pd.DataFrame
        :param tk_col: Name of the column in `dataframe` that contains the element's tk.
        :type tk_col: str, optional
        :return: List of all tks that were successfully deleted from the model. If no elements were deleted, an empty list is returned.
        :rtype: List[str]
        """
        # Determine tks to delete
        tks_to_delete = dataframe[tk_col].dropna().unique().tolist()

        # Delete tks and collect successfully deleted tks
        tks_deleted =[]
        for tk in tks_to_delete:
            try:
                self.DeleteElement(Tk=tk)
                tks_deleted.append(tk)
            except Exception as e:
                logger.error(f"[delete_elements_in_dataframe] Error deleting element with TK={tk}: {e}")

        return tks_deleted


    def __apply_model_data_property_updates(
        self,
        element_type: Enum,
        updates_df: pd.DataFrame,
        properties_new: Optional[List[str]] = None,
        tag: Optional[str] = "_new",
    ) -> pd.DataFrame:
        """
        WORK IN PROGRESS
        Apply model_data updates for a single property using a DataFrame with keys and new values.

        Expects:
        - One key column (default: 'tk'), and
        - Exactly one column named '<model_data_property>_new' (or pass `property_name` to target one explicitly).

        Parameters
        ----------
        element_type : Enum
            The element type to update (e.g., self.ObjectTypes.Pipe).
        updates_df : pd.DataFrame
            Input with at least:
            - key column (default 'tk'), and
            - one '<property>_new' column (e.g., 'diameter_mm_new').
        property_name : Optional[str], default None
            If given, we will look for the column f"{property_name}_new".
            If None, we auto-detect a single '*_new' column.
        on : str, default 'tk'
            Name of the key column in `updates_df`. If it's the index, it will be reset.
        create_missing : bool, default False
            If True, allow creating model_data rows that don't exist yet (your set-logic decides how).
        dry_run : bool, default False
            If True, do NOT apply; just return a normalized summary of what would be changed.
        allow_na : bool, default True
            If False, rows with NaN in the '<property>_new' column will be dropped (skipped).

        Returns
        -------
        pd.DataFrame
            A summary dataframe with columns:
            ['tk', 'property', 'new_value'] (+ 'status' when dry_run)
            representing the intended updates.
        """
        logger.info(f"[update] Applying model_data updates for element type: {element_type}")

        if updates_df is None or updates_df.empty:
            logger.warning("[update] Empty updates_df provided. Nothing to do.")
            return pd.DataFrame(columns=["tk", "property", "new_value"])

        df = updates_df.copy()

        # --- Ensure key ('tk') column is present ---
        if tk not in df.columns:
            if df.index.name == tk:
                df = df.reset_index()
                logger.info(f"[update] Using index as column.")
            else:
                msg = f"[update] tk not found in updates_df (nor as index)."
                logger.error(msg)
                raise KeyError(msg)

        # --- Resolve & Validate given properties_new ---
        logger.info("[update] Resolving & validating given properties_new...")
        properties_new_in_index=df.columns.intersection(properties_new).tolist()
        logger.info(f"[update] In updates_df found: {properties_new_in_index}")
        properties_new_stripped = [p.removesuffix(tag) for p in properties_new]
        model_data_props_new=self.__resolve_given_model_data_properties(element_type=element_type, properties=properties_new_stripped)
        model_data_props_new_with_suffix = [p + tag for p in model_data_props_new]
        logger.info("[update] Resolved & validated given properties_new")

        # TODO
        # --- Set model_data values in model ---
        for tk in self.GetTksofElementType(ElementType=element_type):
            for prop in model_data_props_new:
                msg=self.SetValue(prop, updates_df.iloc[tk, model_data_props_new_with_suffix])
                logger.info

    def __AddNodesAndPipes(self, dfXL):
        """
        Takes a dataframe with each row representing one pipe and adds it to the model. Only dfXL
        This function should be moved to Dataframes.py to create a general module for working with Dataframes in SIR 3S.
        """
        for i, row in dfXL.iterrows():
            kvr = int(row['KVR'])

            # Create KI node
            x_ki, y_ki = row['geometry'].coords[0]
            tk_ki = self.AddNewNode(
                "-1", f"Node{i}KI {self.__VL_or_RL(kvr)}", f"Node{i}", x_ki, y_ki,
                1.0, 0.1, 2.0, f"Node{i}KI", f'ID{row.nodeKI_id}', kvr
            )
            dfXL.at[i, 'nodeKI'] = tk_ki

            # Create KK node
            x_kk, y_kk = row['geometry'].coords[-1]
            tk_kk = self.AddNewNode(
                "-1", f"Node{i}KK {self.__VL_or_RL(kvr)}", f"Node{i}", x_kk, y_kk,
                1.0, 0.1, 2.0, f"Node{i}KK", f'ID{row.nodeKK_id}', kvr
            )
            dfXL.at[i, 'nodeKK'] = tk_kk

            # Create pipe
            tk_pipe = self.AddNewPipe(
                "-1", tk_ki, tk_kk, row['geometry'].length,
                str(row['geometry']), str(row['MATERIAL']), str(row['DN']),
                1.5, f'ID{i}', f'Pipe {i}', kvr
            )
            dfXL.at[i, 'tk'] = tk_pipe

            try:
                baujahr = dfXL.at[i, 'BAUJAHR']
                if pd.notna(baujahr):
                    self.SetValue(tk_pipe, "Baujahr", str(baujahr))
            except Exception as e:
                logger.info(f"BAUJAHR of Pipe {tk_pipe} not assigned: {e}")

            try:
                hal = dfXL.at[i, 'HAL']
                if pd.notna(hal):
                    self.SetValue(tk_pipe, "Hal", str(hal))
            except Exception as e:
                logger.info(f"HAL of Pipe {tk_pipe} not assigned: {e}")

            # 2LROHR does not work
            try:
                partner_id = dfXL.at[i, '2LROHR_id']
                if pd.notna(partner_id):
                    match = dfXL[dfXL['tk_id'] == partner_id]
                    if not match.empty:
                        partner_pipe_tk = match.iloc[0]['tk']
                        self.SetValue(tk_pipe, "Fk2lrohr", partner_pipe_tk)
            except Exception as e:
                logger.info(f"2LROHR of Pipe {tk_pipe} not assigned: {e}")

        return dfXL

    def __insert_dfPipes(self, dfPipes):
        """
        Takes a dataframe with each row representing one pipe and adds it to the model.
        The dataframe needs minimum of cols: geometry (LINESTRING), MATERIAL (str), DN (int), KVR (int)
        """
        func_name = sys._getframe().f_code.co_name
        logger.info(f"{func_name}: Start.")

        climbing_index = 0
        for idx in range(len(dfPipes)):
            dfPipes.at[idx, 'nodeKI_id'] = climbing_index
            dfPipes.at[idx, 'nodeKK_id'] = climbing_index + 1
            climbing_index += 2

        self.StartEditSession(SessionName="AddNodesAndPipes")

        dfPipes['KVR'] = dfPipes['KVR'].astype(str).str.strip()
        dfVL = dfPipes[dfPipes['KVR'] == '1'].reset_index(drop=True)
        dfRL = dfPipes[dfPipes['KVR'] == '2'].reset_index(drop=True)

        dfVL = self.AddNodesAndPipes(dfVL)
        dfRL = self.AddNodesAndPipes(dfRL)

        dfPipes = pd.concat([dfVL, dfRL], ignore_index=True)

        self.EndEditSession()
        self.SaveChanges()
        self.RefreshViews()

        return dfPipes

    ## Dataframe Operations: Time/Static Tables

    def get_dataframes_from_nominal_diameter_tables(
        self
        ) -> pd.DataFrame:
        """
        Retrieve and assemble row-wise property data for all nominal diameter tables, returning both a vertically concatenated DataFrame
        and a dictionary of individual nominal diameter DataFrames.

        :param element_type: Static table element type whose row data should be extracted (eg. table_type=self.ObjectTypes.PipeTable).
        :type element_type: Enum

        :return: A tuple containing:

                - df_v: vertically concatenated DataFrame of all rows from all tables (needed for other functions)

                - dfs: dictionary mapping each table tk to its DataFrame

                - tks_of_nominal_diameter_table: list of table tks of the given type

        :rtype: Tuple[pd.DataFrame, Dict[Any, pd.DataFrame], List[Any]]
        """

        # --- Obtain all rows from all table of given type ---
        tks_of_nominal_diameter_table = self.GetTksofElementType(self.ObjectTypes.PipeTable)
        properties_rows=self.GetPropertiesofElementType(self.ObjectTypes.PipeTable_Row)
        dfs = {}
        for table_tk in tks_of_nominal_diameter_table:
            rows = self.GetTableRows(tablePkTk=table_tk)
            row_tks = list(rows[0])
            table_name = self.GetValue(Tk=table_tk, propertyName="Name")[0]
            data = {
                tk: {prop: self.GetValue(tk, prop)[0] for prop in properties_rows}
                for tk in row_tks
            }
            df = pd.DataFrame.from_dict(data, orient='index')
            df.insert(0, "Table Name", table_name)
            df = df.reset_index(names="tk_merge") 

            dfs[table_tk] = df

        # --- Obtain data and Build df ---
        
        if len(dfs) > 1:
            df_v = pd.concat(dfs, axis=0, ignore_index=True, join="outer")
            df_v = df_v.sort_index(ascending=True)
        else:
            df_v = dfs[tks_of_nominal_diameter_table[0]]

        return (df_v, dfs, tks_of_nominal_diameter_table)

    def insert_dataframe_into_time_table(
        self,
        time_table_tk: str,
        dataframe: pd.DataFrame,
        reference_time_stamp = None,
        overwrite: bool = True,
        keep: bool = True,
        date_col: str = "TAG",
        time_col: str = "UHRZEIT",
        value_col: str = "WERT",
    ) -> pd.DataFrame:
        """
        Imports time-value pairs for a time table based on the provided dataframe into a SIR 3S model.
        Existing rows are matched by simulation-time value in seconds (derived from date/time and reference_time_stamp).
        If source time series has duplicates, the one with lowest numerical value is used.
        How previously existing rows in the target time table are handled is determined by the params overwrite and keep.

        :param self:
        :param time_table_tk: Tk of time table (["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable", "ThermalOutputTable", "TemperatureTable"]) to set time-value pairs for. Does not work with weather data table.
        :type time_table_tk: int
        :param dataframe: Pandas dataframe with date_col, time_col, value_col
        :type dataframe: pd.Dataframe
        :param reference_time_stamp: "0-timestamp" - the difference to this timestamp will be calculated for each timestamp in the dataframe and used in the time table, default=self.GetTimeStamps()[0][0] - first simulation timestamp, values like "%Y-%m-%d %H:%M:%S.%f"
        :type reference_time_stamp: str
        :param overwrite: If True, existing matching time deltas are updated in-place; if False, matching entries are deleted and reinserted.
        :type overwrite: bool
        :param keep: If True, old target time deltas without source counterpart are kept; if False, they are deleted.
        :type keep: bool
        :param date_col: Name of date col in dataframe, default = "TAG", values like "2026-01-01", "%Y-%m-%d"
        :type date_col: str
        :param time_col: Name of time col in dataframe, default = "UHRZEIT", values like "00:00:20.000000", "%H:%M:%S.%f"
        :type time_col: str
        :param value_col: Name of value col in dataframe, default = "WERT", values like 83 or 1.2
        :type value_col: str

        :return: Dataframe with time-value pairs inserted into the time table with operation flag (overwritten/inserted/kept) column
        :rtype: pd.DataFrame
        """

        # --- Input data validation ---
        logger.info("[insert dataframe into time table] Validating input data ...")
        available_time_table_tks=[]

        for type in ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable", "ThermalOutputTable", "TemperatureTable"]:
            tks = self.GetTksofElementType(self.ObjectTypes[type])
            available_time_table_tks.extend(tks)

        if time_table_tk not in available_time_table_tks:
            logger.error(f"[insert dataframe into time table] Time table with tk {time_table_tk} does not exist.")
            return pd.DataFrame()
        
        logger.info("[insert dataframe into time table] tks check done")
        
        if dataframe.empty:
            logger.error(f"[insert dataframe into time table] Dataframe is empty.")
            return pd.DataFrame()
        
        available_dataframe_columns = dataframe.columns
        if date_col not in available_dataframe_columns:
            logger.error(f"[insert dataframe into time table] Date col {date_col} not in dataframe columns.")
            return pd.DataFrame()
        if time_col not in available_dataframe_columns:
            logger.error(f"[insert dataframe into time table] Time col {time_col} not in dataframe columns.")
            return pd.DataFrame()
        if value_col not in available_dataframe_columns:
            logger.error(f"[insert dataframe into time table] Value col {value_col} not in dataframe columns.")
            return pd.DataFrame()

        try:
            internal_ref_time = self.GetTimeStamps()[0][0]
        except:
            internal_ref_time = None

        if reference_time_stamp:
            used_reference_time_stamp = reference_time_stamp
        elif internal_ref_time:
            s = self.GetTimeStamps()[0][0]
            used_reference_time_stamp = s.split()[0] + " " + s.split()[1]
        else:
            logger.error(f"[insert dataframe into time table] No valid simulation timestamp in model, nor reference time stamp given.")
            return pd.DataFrame()
        used_reference_time_stamp_as_datetime = datetime.strptime(used_reference_time_stamp, "%Y-%m-%d %H:%M:%S.%f")

        df = dataframe[[date_col, time_col, value_col]].copy()
        if df.empty:
            logger.error("[insert dataframe into time table] Working dataframe is empty after selecting parametrized column names.")
            return pd.DataFrame()

        # --- Strict format check for date_col to avoid silent coercion later ---
        parsed_date_col = pd.to_datetime(df[date_col].astype(str), format="%Y-%m-%d", errors="coerce")
        if parsed_date_col.isna().any():
            invalid_values = df.loc[parsed_date_col.isna(), date_col].astype(str).head(5).tolist()
            logger.error(
                f"[insert dataframe into time table] Invalid values in date column {date_col}. "
                f"Expected format is %Y-%m-%d (e.g. 2026-01-01). Samples: {invalid_values}"
            )
            return pd.DataFrame()

        # --- Strict format check for time_col to avoid silent coercion later ---
        parsed_time_col = pd.to_datetime(df[time_col].astype(str), format="%H:%M:%S.%f", errors="coerce")
        if parsed_time_col.isna().any():
            invalid_values = df.loc[parsed_time_col.isna(), time_col].astype(str).head(5).tolist()
            logger.error(
                f"[insert dataframe into time table] Invalid values in time column {time_col}. "
                f"Expected format is %H:%M:%S.%f (e.g. 00:00:20.000000). Samples: {invalid_values}"
            )
            return pd.DataFrame()

        logger.info("[insert dataframe into time table] Successfully validated input data.")

        ts_series = pd.to_datetime(
            df[date_col].astype(str) + " " + df[time_col].astype(str),
            format="%Y-%m-%d %H:%M:%S.%f",
            errors="coerce"
        )

        # --- Keep the row with the lower numeric value_col for duplicate timestamps ---
        value_numeric = pd.to_numeric(df[value_col])

        if ts_series.duplicated().any():
            logger.warning(
                "[insert dataframe into time table] Duplicate timestamps found. "
                f"Keeping row with lower numerical value in column {value_col} per timestamp. Check your input df for duplicate timestamps."
            )

            keep_index = (
                pd.DataFrame({"timestamp": ts_series, "value_numeric": value_numeric}, index=df.index)
                .sort_values(by=["timestamp", "value_numeric"], na_position="last", kind="mergesort")
                .drop_duplicates(subset=["timestamp"], keep="first")
                .index
            )
            df = df.loc[keep_index]

        ts_series = pd.to_datetime(
            df[date_col].astype(str) + " " + df[time_col].astype(str),
            format="%Y-%m-%d %H:%M:%S.%f",
            errors="coerce"
        )
        sort_index = ts_series.sort_values(kind="mergesort").index
        df = df.loc[sort_index].reset_index(drop=True)
        ts_series = ts_series.loc[sort_index].reset_index(drop=True)
        
        # --- Timeseries for new version of time table ---
        delta_time_col_new_float = (ts_series - used_reference_time_stamp_as_datetime).dt.total_seconds()
        delta_time_to_value_new = pd.Series(df[value_col].values, index=delta_time_col_new_float).to_dict()
        property_name, _ = self._get_time_table_col_name_from_tk(time_table_tk=time_table_tk)

        # --- Timeseries for old version of time table ---
        df_table_old = self.get_dataframe_from_time_table(time_table_tk=time_table_tk, value_col_name="WERT")
        if ("tk" not in df_table_old.columns or "WERT" not in df_table_old.columns or (df_table_old["tk"].isna().all() and df_table_old["WERT"].isna().all())):
            delta_time_col_old_float = pd.Series(dtype="float64")
            delta_time_to_value_and_tk_old = {}
            if keep:
                logger.warning(f"[insert dataframe into time table] No existing rows in time table with tk {time_table_tk} to keep. Function will behave as if Keep=False")
                keep = False
        else:
            tks_rows_old = df_table_old["tk"]
            values_rows_old = df_table_old["WERT"]
            delta_time_col_old_float = pd.Series(df_table_old.index)
            delta_time_to_value_and_tk_old = {
                dt: (val, tk)
                for dt, val, tk in zip(delta_time_col_old_float, values_rows_old, tks_rows_old)
            }

        # --- Construct sets of time deltas to keep, insert, overwrite, delete ---
        old_delta_times = pd.Index(delta_time_col_old_float)
        new_delta_times = pd.Index(delta_time_col_new_float)

        delta_time_same = old_delta_times.intersection(new_delta_times).sort_values()
        delta_time_only_old = old_delta_times.difference(new_delta_times).sort_values()
        delta_time_only_new = new_delta_times.difference(old_delta_times).sort_values()

        delta_time_to_keep = pd.Series(dtype="float64")
        delta_time_to_insert = pd.Series(dtype="float64")
        delta_time_to_overwrite = pd.Series(dtype="float64")
        delta_time_to_delete = pd.Series(dtype="float64")

        if overwrite:
            if keep:
                delta_time_to_keep = delta_time_only_old
                delta_time_to_insert = delta_time_only_new
                delta_time_to_overwrite = delta_time_same
                delta_time_to_delete = pd.Index([], dtype="float64")
            else: # !keep
                delta_time_to_keep = pd.Index([], dtype="float64")
                delta_time_to_insert = delta_time_only_new
                delta_time_to_overwrite = delta_time_same
                delta_time_to_delete = delta_time_only_old
        else: # !overwrite
            if keep:
                delta_time_to_keep = delta_time_only_old
                delta_time_to_insert = delta_time_same.union(delta_time_only_new)
                delta_time_to_overwrite = pd.Index([], dtype="float64") 
                delta_time_to_delete = delta_time_same
            else: # !keep
                delta_time_to_keep = pd.Index([], dtype="float64") 
                delta_time_to_insert = delta_time_same.union(delta_time_only_new)
                delta_time_to_overwrite = pd.Index([], dtype="float64") 
                delta_time_to_delete = delta_time_same.union(delta_time_only_old)

        delta_time_to_operation_flag = {}

        # --- Delete rows ---
        for dt in delta_time_to_delete:
            tk_row_to_delete = delta_time_to_value_and_tk_old[dt][1]
            self.DeleteElement(tk_row_to_delete)
            logger.info(f"[insert dataframe into time table] Deleting row at time delta {dt} with value {delta_time_to_value_and_tk_old[dt][0]} and tk {delta_time_to_value_and_tk_old[dt][1]} ...")
            delta_time_to_operation_flag[dt] = "deleted"

        # --- Insert rows ---
        for dt in delta_time_to_insert:
            v = delta_time_to_value_new[dt]
            tk_row = self.AddTableRow(tablePkTk=time_table_tk)[0]
            self.SetValue(Tk=tk_row, propertyName="Zeit", Value=(f"{dt:.6f}".replace(".", ",")))
            self.SetValue(Tk=tk_row, propertyName=property_name, Value=str(v))
            logger.info(f"[insert dataframe into time table] Inserting row at time delta {dt} with value {v} at tk {tk_row} ...")
            delta_time_to_operation_flag[dt] = "inserted"
        
        # --- Overwrite rows ---
        for dt in delta_time_to_overwrite:
            v = delta_time_to_value_new[dt]
            tk_row = delta_time_to_value_and_tk_old[dt][1]
            self.SetValue(Tk=tk_row, propertyName=property_name, Value=str(v))
            logger.info(f"[insert dataframe into time table] Overwriting row at time delta {dt} with new value {v} at tk {tk_row} ...")
            delta_time_to_operation_flag[dt] = "overwritten"

        # --- Keep rows ---
        for dt in delta_time_to_keep:
            v = delta_time_to_value_and_tk_old[dt][0]
            tk_row = delta_time_to_value_and_tk_old[dt][1]
            logger.info(f"[insert dataframe into time table] Keeping row at time delta {dt} with value {v} at tk {tk_row} ...")
            delta_time_to_operation_flag[dt] = "kept"

        df = self.get_dataframe_from_time_table(
            time_table_tk=time_table_tk,
            value_col_name=value_col,
            flag_mapping=delta_time_to_operation_flag
        )

        return df

    def get_dataframes_from_time_table_type(
        self,
        time_table_type: str,
    ) -> List[pd.DataFrame]:
        """
        Get DataFrames for all time tables of a given type and a joint horizontally concatenated DataFrame.
        
        :param self:
        :param time_table_type: The time table type to extract. Must be one of:
                                ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable", "ThermalOutputTable", "TemperatureTable"].
        :type time_table_type: str
        :return: A tuple containing:

                - df_h: 
                    The joint DataFrame. If multiple tables are found, this is a column-wise concatenation (``axis=1``, ``join='outer'``) of all per-TK DataFrames with the index sorted ascending. If only one table exists, it is returned directly.
                
                - dfs: 
                    A dictionary mapping each TK to its corresponding DataFrame (key: TK, value: DataFrame).
                
                - tks_of_time_table_type: 
                    The list of TKs for the requested time table type, in the order returned by ``GetTksofElementType``.
        
        :rtype: tuple[pd.DataFrame, dict[Any, pd.DataFrame], list[Any]]
        """
        logger.info(f"[get dataframes from time table type] ...")
        # --- Validate input ---
        
        if time_table_type not in ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable", "ThermalOutputTable", "TemperatureTable"]:
            logger.error(f"Invalid time table type. Has to be of type: ['VarPressureTable', 'VarFlowTable', 'ValveLiftTable', 'PumpSpeedTable', 'MeasuredVariableTable', 'LoadFactorTable']")
        
        # --- Obtain tks of time table type ---
        tks_of_time_table_type = self.GetTksofElementType(self.ObjectTypes[time_table_type])
        _, _value_col_name = self._get_time_table_col_name_from_tk(time_table_tk=tks_of_time_table_type[0]) 
        
        dfs = {}

        # --- Obtain table for each tk ---
        for tk in  tks_of_time_table_type:
            table_name = self.GetValue(Tk=tk, propertyName="Name")[0]
            dfs[tk]=self.get_dataframe_from_time_table(time_table_tk=tk, value_col_name=table_name)# + " " + _value_col_name)

        # --- Create Joint df ---

        if len(dfs) > 1:
            df_h = pd.concat(
                [df.drop(columns=["tk"], errors="ignore") for df in dfs.values()],
                axis=1,
                join='outer'
            )
            df_h = df_h.sort_index(ascending=True)
        else:
            df_h = dfs[tks_of_time_table_type[0]].drop(columns=["tk"], errors="ignore")

        logger.info(f"[get dataframes from time table type] Successful")

        return df_h, dfs, tks_of_time_table_type
        

    def get_dataframe_from_time_table(
        self,
        time_table_tk: str,
        value_col_name: str = None,
        flag_mapping: dict = None
    ) -> pd.DataFrame:
        """
        Obtain time variable table (tables = ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable", "ThermalOutputTable", "TemperatureTable"]) in format of a pandas dataframe with time and value column.
        
        :param self: 
        :param time_table_tk: Tk of time table to get time-value pairs from.
        :type time_table_tk: str
        :param value_col_name: Name given to the value column.
        :type value_col_name: str
        :param flag_mapping: Optional mapping of delta_time. If provided, an additional column operation_flag is added to the returned dataframe. Not necessary for usual use.
        :type flag_mapping: dict

        :return: DataFrame with time index (Zeit [s]) and columns value_col and tk.
        :rtype: pd.DataFrame
        """

        # --- Validate input tk and find time table type ---
        logger.info(f"[get dataframe from time table] Validating input data (time_table_tk={time_table_tk})...")

        value_name, _value_col_name = self._get_time_table_col_name_from_tk(time_table_tk=time_table_tk) 
        if value_name == -1:
            return -1

        if value_col_name:
            value_col_name_to_use = value_col_name
        else:
            value_col_name_to_use = _value_col_name

        logger.info("[get dataframe from time table] Successfully validated input data.")

        # --- Build dataframe
        logger.info("[get dataframe from time table] Building dataframe ...")

        rows = self.GetTableRows(tablePkTk=time_table_tk)
        row_tks = list(rows[0]) 

        rows = []
        for tk in row_tks:
            time = self.GetValue(tk, "Zeit")[0]
            time = float(time.replace(",", "."))
            value = self.GetValue(tk, value_name)[0]
            value = float(value.replace(",", "."))
            rows.append({"Zeit [s]": time, "tk": tk, value_col_name_to_use: value})

        if not rows:
            logger.info("[get dataframe from time table] time table is empty.")
            df = pd.DataFrame(data=[[np.nan, None, np.nan]], columns=["Zeit [s]", "tk", value_name])
            df = df.set_index("Zeit [s]")
        else:
            df = pd.DataFrame(rows)
            if df["Zeit [s]"].duplicated().any():
                duplicate_mask = df["Zeit [s]"].duplicated(keep=False)
                duplicate_rows = df.loc[duplicate_mask, ["Zeit [s]", "tk", value_col_name_to_use]].sort_values("Zeit [s]")
                duplicate_count = int(df["Zeit [s]"].duplicated().sum())
                logger.warning(f"[get dataframe from time table] Found {duplicate_count} duplicate time index value(s). Keeping the last row per timestamp for stable concatenation.")
                logger.error(f"[get dataframe from time table] Duplicate rows:\n{duplicate_rows.to_string(index=False)}")
                df = df.drop_duplicates(subset=["Zeit [s]"], keep="last")
            df = df.set_index("Zeit [s]")
            logger.info("[get dataframe from time table] Successfully built dataframe.")

        if flag_mapping is not None:
            df["operation_flag"] = df.index.map(flag_mapping).fillna("unmapped")

        

        return df

    def _get_time_table_col_name_from_tk(
        self,
        time_table_tk: str        
    ) -> str:
        
        if time_table_tk in self.GetTksofElementType(self.ObjectTypes.VarPressureTable):
            value_name = 'Ph'                                                                    # needed to retrieve numeric value from row: self.GetPropertiesofElementType(self.ObjectTypes.VarPressureTable) 
            _value_col_name = 'Druck p [bar]'                                                     # needed to name column in output df: look up in SIR Graf
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.VarFlowTable):
            value_name = 'Qm'
            _value_col_name = 'Einspeisung/Abnahme Q [m^3/h]'
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.ValveLiftTable):
            value_name = 'Phi'
            _value_col_name = 'Stellung phi [%]'
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.PumpSpeedTable):
            value_name = 'N'
            _value_col_name = 'Drehzahl [1/min]'
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.MeasuredVariableTable):
            value_name = 'W'
            _value_col_name = 'Sollwert'
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.LoadFactorTable):
            value_name = 'Lf'
            _value_col_name = 'Lastfaktor [-]'
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.ThermalOutputTable):
            value_name = 'W'
            _value_col_name = 'Leistung [kW]'
        elif time_table_tk in self.GetTksofElementType(self.ObjectTypes.TemperatureTable):
            value_name = 'T'
            _value_col_name = 'Temperatur T [°C]'
        # could extend for WeatherDataTable
        else:
            logger.error(f"[_get_time_table_col_name_from_tk] No time table with tk {time_table_tk}")
            return -1, -1
        
        return value_name, _value_col_name
    
    def _column_has_vector_values(self, col):
        """Return True if at least one value contains tabs."""
        return col.dropna().astype(str).str.contains("\t").any()

    # Miscellaneous
    def __Get_Node_Tks_From_Pipe(self, pipe_tk):
        func_name = sys._getframe().f_code.co_name
        logger.info(f"{func_name}: Start.")

        from_node_name = self.GetValue(pipe_tk, 'FromNode.Name')[0]
        to_node_name = self.GetValue(pipe_tk, 'ToNode.Name')[0]

        from_node_tk = None
        to_node_tk = None

        for node_tk in self.GetTksofElementType(ElementType=self.ObjectTypes.Node):
            node_name = self.GetValue(node_tk, 'Name')[0]
            if node_name == from_node_name:
                from_node_tk = node_tk
            if node_name == to_node_name:
                to_node_tk = node_tk

        return from_node_tk, to_node_tk

    def __Get_Pipe_Tk_From_Nodes(self, fkKI, fkKK, Order=True):
        func_name = sys._getframe().f_code.co_name
        logger.info(f"{func_name}: Start.")

        from_node_name = self.GetValue(fkKI, 'Name')[0]
        to_node_name = self.GetValue(fkKK, 'Name')[0]

        pipe_tk_ret = None

        if Order:
            for pipe_tk in self.GetTksofElementType(ElementType=self.ObjectTypes.Pipe):
                if (self.GetValue(pipe_tk, 'FromNode.Name')[0] == from_node_name and
                   self.GetValue(pipe_tk, 'ToNode.Name')[0] == to_node_name):
                    pipe_tk_ret = pipe_tk
                    break
        else:
            for pipe_tk in self.GetTksofElementType(ElementType=self.ObjectTypes.Pipe):
                from_name = self.GetValue(pipe_tk, 'FromNode.Name')[0]
                to_name = self.GetValue(pipe_tk, 'ToNode.Name')[0]
                if ((from_name == from_node_name and to_name == to_node_name) or
                   (from_name == to_node_name and to_name == from_node_name)):
                    pipe_tk_ret = pipe_tk
                    break

        return pipe_tk_ret

    def __VL_or_RL(self, KVR):
        func_name = sys._getframe().f_code.co_name
        logger.info(f"{func_name}: Start.")
        if KVR == 1:
            return 'VL'
        elif KVR == 2:
            return 'RL'
        else:
            return 'Unknown'

    def __Check_Node_Name_Duplicates(self, name):
        func_name = sys._getframe().f_code.co_name
        logger.info(f"{func_name}: Start.")

        tks = []
        for node_tk in self.GetTksofElementType(ElementType=self.ObjectTypes.Node):
            current_name = self.GetValue(node_tk, 'Name')[0]
            if current_name == name:
                tks.append(node_tk)

        if len(tks) == 1:
            logger.info(f'Only the node with tk {tks[0]} has the name {name}')
        else:
            logger.info(f'The nodes of the following tks have the same name ({name}):')
            for tk in tks:
                logger.info(f'{tk}')

        return tks

    def __is_a_model_open(self):
        """
        Returns true if a model is open, false if no model is open or the NetworkType is undefined.
        """
        is_a_model_open = True
        if(self.GetNetworkType=="NetworkType.Undefined"):
            is_a_model_open = False
        return is_a_model_open
    