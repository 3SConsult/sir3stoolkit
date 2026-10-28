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
import time
from typing import Dict, List, Optional, Union
from enum import Enum
from typing import List, Tuple, Any, Set
from collections import defaultdict
from datetime import datetime

from sir3stoolkit.dependency_check import require_packages
require_packages(__name__, "attrs", "pytoolconfig", "pandas", "geopandas", "shapely")

from attrs import field
from pytoolconfig import dataclass
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely import wkt

from sir3stoolkit.logging_utils import get_logger
from sir3stoolkit.mantle.advanced_operations import mapping_for_groups
from sir3stoolkit.mantle.mx import SIR3S_Model_MX

logger = get_logger(__name__)


# API loops (GetResultfortimestamp(), name/end-node lookups) with at least this many calls log their progress.
_API_PROGRESS_LOG_MIN_CALLS = 1000


class SIR3S_Model_Dataframes(SIR3S_Model_MX):
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
                df[col] = pd.Series(out, index=df.index)
            else:
                df[col] = s_str

        # Transform to gpd ---
        if geometry:
            try:
                df["geometry"] = df["geometry"].apply(wkt.loads)
                srid, srid2, srid_string = self.get_EPSG()
                if srid and (srid != '0'):
                    df = gpd.GeoDataFrame(df, geometry="geometry", crs=f"EPSG:{srid}")
                    logger.info(f"[model_data] Transforming DataFrame to GeoDataFrame successful with EPSG: {srid}")
                else:
                    logger.warning(f"[model_data] Spatial Reference Identifier (SRID) not defined in model. DataFrame cannot be transformed to GeoDataFrame but geometry column can be created independently of SRID. Returning regular DataFrame with a geometry column.")
            except Exception as e:
                    logger.error(f"[model_data] Error transforming DataFrame to GeoDataFrame. {e}")

        logger.info(f"[model_data] Done. Shape: {df.shape}")
        return df

    def _resolve_result_properties(self, element_type: Enum, properties: Optional[List[str]]) -> Tuple[List[str], Set[str]]:
        """
        Validate requested result properties against GetResultProperties_from_elementType().

        :return: (result properties to use, in order; the subset of all result properties that are
                 interior-point/VEC properties)
        :rtype: Tuple[List[str], Set[str]]
        """
        available_model_data_props = self.GetPropertiesofElementType(ElementType=element_type)
        available_result_props = self.GetResultProperties_from_elementType(
            elementType=element_type,
            onlySelectedVectors=False
        )
        vector_props = {prop for prop in available_result_props if "VEC" in prop}

        result_props: List[str] = []
        if properties is None:
            logger.info(f"[results] No properties given → using ALL result properties for {element_type}.")
            result_props = list(available_result_props)
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
        return result_props, vector_props

    def _mx_file_properties(self, element_type: Enum, layout, properties: Optional[List[str]]) -> Tuple[List[str], Set[str]]:
        """
        Result properties for bulk=True, from what the result file holds for the element type:
        properties=None gives all readable ones (in GetResultProperties_from_elementType() order where
        known); requested properties the file doesn't hold, or can't split per element, are left out
        with a warning.

        :return: (properties to read, the interior-point (VEC) ones among them)
        :rtype: Tuple[List[str], Set[str]]
        """
        readable = layout.readable_props
        unreadable = set(layout.unresolvable_vector_props) | set(layout.skipped_props)
        if not readable and not unreadable:
            logger.warning(f"[bulk results] The result file holds no results for '{element_type.name}'.")
        try:
            api_order = list(self.GetResultProperties_from_elementType(elementType=element_type, onlySelectedVectors=False))
        except Exception:
            api_order = []
        rank = {p: i for i, p in enumerate(api_order)}
        if properties is None:
            props = sorted(readable, key=lambda p: (rank.get(p, len(rank)), readable.index(p)))
            left_unreadable, missing = sorted(unreadable), []
        else:
            props = list(dict.fromkeys(p for p in properties if p in readable))
            left_unreadable = [p for p in properties if p in unreadable]
            missing = [p for p in properties if p not in readable and p not in unreadable]
        if left_unreadable:
            logger.warning(f"[bulk results] Stored for '{element_type.name}' but can't be split per element from the "
                           f"result file - left out: {left_unreadable}")
        if missing:
            logger.warning(f"[bulk results] Not in the result file for '{element_type.name}' (not selected for this "
                           f"output resolution) - left out: {missing}")
        logger.info(f"[results] Using {len(props)} result properties from the result file.")
        return props, {p for p in props if "VEC" in p}

    def _result_column_labels(self, tks, end_nodes_available: bool) -> dict:
        """(name, end_nodes string) per tk - one GetValue(Name)/GetEndNodes() call per tk."""
        label_by_tk = {}
        t0 = time.perf_counter()
        progress = self._MxProgress(logger, "[results] Looking up names/end nodes", len(tks), "elements",
                               enabled=len(tks) >= _API_PROGRESS_LOG_MIN_CALLS)
        for tk in tks:
            try:
                name = self.GetValue(tk, "Name")[0]
            except Exception as e:
                logger.warning(f"[results] Failed to get name for tk '{tk}': {e}")
                name = "UNKNOWN"

            if end_nodes_available:
                try:
                    end_nodes_str = str(self.GetEndNodes(tk))
                except Exception as e:
                    logger.warning(f"[results] Failed to get end nodes for tk '{tk}': {e}")
                    end_nodes_str = "UNKNOWN"
            else:
                end_nodes_str = "No end nodes on element type"

            label_by_tk[tk] = (name, end_nodes_str)
            progress.update()
        logger.info(f"[results] Names/end nodes of {len(label_by_tk):,} element(s) looked up ({time.perf_counter() - t0:.1f} s).")
        return label_by_tk

    @staticmethod
    def _cast_float_columns(df: pd.DataFrame, dtype: np.dtype) -> pd.DataFrame:
        """Cast all float columns (e.g. float64 from parsed API strings) to dtype; other columns stay."""
        if df.shape[1] == 0:
            return df
        is_float = np.array([d.kind == "f" for d in df.dtypes])
        needs_cast = is_float & np.array([d != dtype for d in df.dtypes])
        if not needs_cast.any():
            return df
        if is_float.all():
            return df.astype(dtype)
        positions = np.flatnonzero(needs_cast)
        df = df.copy()
        for pos in positions:
            df.isetitem(int(pos), df.iloc[:, pos].astype(dtype))
        return df

    @staticmethod
    def _add_name_and_end_node_levels(df: pd.DataFrame, label_by_tk: Optional[dict], props: Optional[List[str]] = None) -> pd.DataFrame:
        """
        (tk, property[, interior points]) columns → (tk, name, end_nodes, property[, interior points]),
        or with label_by_tk=None just rebuilt as (tk, property[, interior points]).

        The levels are built in column order (tk, name, end_nodes as they appear, property in the order of
        props, interior points ascending) instead of alphabetically, so the column index stays lexsorted
        for the tk-major / property-minor column order and selecting e.g. df.loc[ts, (tk, "PVEC")] (after
        dropping name/end_nodes) doesn't raise pandas' "indexing past lexsort depth" PerformanceWarning.
        Name/end_nodes are looked up once per element and mapped to the columns via the tk codes (a
        model can have millions of columns but only one label per element).
        """
        tk_codes, tk_uniques = pd.factorize(df.columns.get_level_values(0), use_na_sentinel=False)
        levels, codes, names = [pd.Index(tk_uniques)], [tk_codes], ["tk"]
        if label_by_tk is not None:
            for j, name in ((0, "name"), (1, "end_nodes")):
                label_codes, label_uniques = pd.factorize(pd.Index([label_by_tk[tk][j] for tk in tk_uniques]),
                                                          use_na_sentinel=False)
                levels.append(pd.Index(label_uniques))
                codes.append(label_codes[tk_codes])
                names.append(name)
        prop_values = df.columns.get_level_values(1)
        present = set(pd.unique(prop_values))
        order = list(dict.fromkeys(([p for p in props if p in present] if props else []) + list(pd.unique(prop_values))))
        levels.append(pd.Index(order))
        codes.append(levels[-1].get_indexer(prop_values))
        names.append("property")
        if df.columns.nlevels > 2:
            point_values = df.columns.get_level_values(2)
            levels.append(pd.Index(sorted(pd.unique(point_values))))
            codes.append(levels[-1].get_indexer(point_values))
            names.append("interior points")
        df.columns = pd.MultiIndex(levels=levels, codes=codes, names=names, verify_integrity=False)
        return df

    def generate_element_results_dataframe(
        self,
        element_type: Enum,
        tks: Optional[List[str]] = None,
        properties: Optional[List[str]] = None,
        timestamps: Optional[Union[List[str], List[int]]] = None,
        place_holder_value: Optional[float] = 99999.0,
        drop_full_place_holder_columns: Optional[bool] = True,
        bulk: Optional[bool] = False,
        vec_format: str = "str",
        output_factor: Optional[int] = None,
        include_name_and_end_nodes: bool = True,
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
        :param bulk: If False (default), retrieve every value via one GetResultfortimestamp() call
                        each - reliable, but slow for large requests. If True, read the values directly
                        from the model's result file (.MX1/.MX2/.MXS, see output_factor) instead.
                        Timestamps and properties are then those the file holds: timestamps (indices or
                        strings) refer to the file's timeline, properties=None gives all properties stored
                        for the element type, and requested properties the file doesn't hold - or can't
                        split per element - are left out with a warning. With the default file, the same
                        output as bulk=False (values equal within float32 precision).
                        Only the requested properties' channels are read, and only at the requested
                        timestamps. Raises MemoryError upfront if the resulting DataFrame wouldn't fit
                        into memory, FileNotFoundError if there are no result files, and RuntimeError
                        if they can't be used (e.g. inconsistent) - then use bulk=False. If the file
                        holds no results for the element type, an empty DataFrame is returned with a
                        warning.
        :type bulk: bool, optional
        :param vec_format: How interior-point (VEC) properties are returned. "str" (default): one
                        tab-separated string per value, formatted like GetResultfortimestamp() returns
                        it (7 significant digits). "multiindex": one float column per interior point,
                        under an additional column level "interior points" (scalar properties: -1),
                        with the exact float32 values - much less memory and time than "str" for large
                        requests. The two formats can therefore differ in the 7th significant digit.
        :type vec_format: str, optional
        :param output_factor: Only for bulk=True: which result file to read. Result files come in two
                        formats - without an output factor in the name ("M-1-0-1.MX1") or with one
                        ("M-1-0-1.<factor>.MX1", factor = SIR 3S TIMD.DTFAK_KLEIN / DTFAK_GROSS). With
                        different factors there are two of the latter: DTFAK_GROSS with all channels at
                        the coarser interval (the timestamps of GetTimeStamps()), and DTFAK_KLEIN with
                        only the time-curve channels at the finer interval.
                        None (default): the file without an output factor if it exists, otherwise the
                        DTFAK_GROSS file of the most recent calculation. A factor: the file of that
                        factor - any factor with result files, also left over from an earlier
                        calculation (ValueError if there are none) - also when a file without an output
                        factor exists. Only the chosen file is read; reading a file older than the most
                        recent calculation logs a warning (the element lists come from the most recent
                        calculation, so values can be assigned to the wrong elements if the network
                        changed in between).
        :type output_factor: int, optional
        :param include_name_and_end_nodes: If True (default), the column MultiIndex has the levels name
                        and end_nodes, looked up via the Toolkit API (two calls per element - for models
                        with many elements this can take longer than reading the results with bulk=True).
                        If False, these levels are left out (columns: tk, property[, interior points]) and
                        no lookups are made; get names/end nodes from
                        generate_element_model_data_dataframe() instead if needed.
        :type include_name_and_end_nodes: bool, optional

        :return: DataFrame with one row per timestamp and MultiIndex columns:
                - Level 0: tk (device ID)
                - Level 1: name (device name) - only for include_name_and_end_nodes=True
                - Level 2: end_nodes (tuple of connected node tks as string) - only for include_name_and_end_nodes=True
                - Level 3: property (result name)
                - Level 4: interior points (only for vec_format="multiindex")
                Data types: float32 for numeric values (the precision SIR 3S stores results in), str for vectorized data (vec_format="str") and literal strings.
        :rtype: pd.DataFrame

        :description:
        Generates a DataFrame containing time-dependent result vectors for all selected devices and timestamps.
        Supports both timestamp strings and index-based selection. Produces a MultiIndex-column DataFrame grouped by device, name, end-nodes, and property.
        """
        # TODO: vec_format defaults to "str" for backwards compatibility; revisit (and clean up the
        # str/multiindex conversions downstream, e.g. add_interior_points_*) later.
        if vec_format not in self._MX_VEC_FORMATS:
            raise ValueError(f"[results] vec_format must be one of {self._MX_VEC_FORMATS}, got {vec_format!r}.")
        multi = vec_format == "multiindex"

        # --- Validate time stamps ---
        logger.info(f"[results] Generating results dataframe for element type: {element_type}")
        t_start = t_phase = time.perf_counter()

        # --- Timestamps: from the result file for bulk=True, from GetTimeStamps() otherwise ---
        mx_file = layout = file_records = None
        if bulk:
            mx1_filepath = self._mx_resolve_mx1(output_factor)  # ValueError for an invalid output_factor
            try:
                mx_file = self._mx_get_file(mx1_filepath)
                layout = self._mx_object_layout(mx_file, self._mx_objtype(element_type))
            except Exception as e:
                raise RuntimeError(
                    f"[bulk results] The result files can't be used for '{element_type.name}': {e} "
                    "Use bulk=False to retrieve the values via GetResultfortimestamp() instead."
                ) from e
            logger.info(f"[bulk results] Result file: {self._mx_describe_file(mx1_filepath, output_factor)}, "
                        f"{len(self._mx_timeline_records(mx_file))} timestamps.")
            ts_labels, file_records = self._mx_file_timestamps(mx_file, timestamps)
        else:
            if output_factor is not None:
                logger.warning(f"[results] output_factor={output_factor!r} only applies to bulk=True; ignored.")
            ts_labels = [str(ts) for ts in self._resolve_given_timestamps(timestamps)]
        if not ts_labels:
            logger.warning("[results] No valid timestamps. Returning empty dataframe.")
            return pd.DataFrame()

        # --- Resolve tks ---
        tks = self.__resolve_given_tks(element_type=element_type, tks=tks, filter_container_tks=None)
        if len(tks) < 1:
            return pd.DataFrame()

        # --- Properties: what the result file holds for bulk=True, the API's result properties otherwise ---
        try:
            if bulk:
                result_props, vector_props = self._mx_file_properties(element_type, layout, properties)
            else:
                result_props, vector_props = self._resolve_result_properties(element_type, properties)
        except Exception as e:
            logger.error(f"[results] Error determining result properties: {e}")
            return pd.DataFrame()

        logger.info(f"[results] {len(ts_labels):,} timestamp(s), {len(tks):,} element(s), {len(result_props)} "
                    f"propert{'y' if len(result_props) == 1 else 'ies'} resolved ({time.perf_counter() - t_phase:.1f} s).")

        # --- Retrieve values ---
        logger.info(f"[results] Retrieving result values... (bulk={bulk})")
        frames: List[pd.DataFrame] = []
        props_via_api = [] if bulk else list(result_props)

        if bulk and result_props:
            t_phase = time.perf_counter()
            estimate = self._mx_frame_bytes_estimate(layout, len(tks), result_props, len(file_records), vec_format)
            self._mx_check_result_size(estimate, f"The results DataFrame for '{element_type.name}'")
            # rows in ts_labels order, NaN already replaced, float32, tk-major columns: no reindex/cast/
            # reordering needed below; full-placeholder columns are dropped in place while reading.
            df_bulk, n_dropped = self._mx_read_frame(
                mx_file, layout, tks, result_props, file_records, ts_labels,
                place_holder_value=place_holder_value, vec_format=vec_format,
                max_chunk_bytes=self._MX_MAX_CHUNK_BYTES,
                drop_full_place_holder_columns=drop_full_place_holder_columns,
            )
            frames.append(df_bulk)
            logger.info(f"[bulk results] {len(result_props)} propert{'y' if len(result_props) == 1 else 'ies'} read "
                        f"from {os.path.basename(mx_file.mx1_path)} ({time.perf_counter() - t_phase:.1f} s).")

        # Per-value GetResultfortimestamp() loop (bulk=False only).
        data_dict = defaultdict(dict)
        n_calls = len(ts_labels) * len(tks) * len(props_via_api)
        t_phase = time.perf_counter()
        progress = self._MxProgress(logger, "[results] GetResultfortimestamp()", n_calls, "values",
                               enabled=n_calls >= _API_PROGRESS_LOG_MIN_CALLS)
        for ts in (ts_labels if props_via_api else []):
            for tk in tks:
                progress.update(len(props_via_api))
                for prop in props_via_api:
                    is_vec = prop in vector_props
                    # vec_format="multiindex": scalars at interior point -1, interior points split
                    # right away into one column each (0..n-1), as the file-based path returns them.
                    key = (tk, prop, 0 if is_vec else -1) if multi else (tk, prop)
                    try:
                        value = self.GetResultfortimestamp(timestamp=ts, Tk=tk, property=prop)[0]
                        if value == "":
                            data_dict[key][ts] = place_holder_value
                        elif is_vec and multi:
                            for j, part in enumerate(str(value).split("\t")):
                                data_dict[(tk, prop, j)][ts] = float(part)
                        elif is_vec:
                            data_dict[key][ts] = str(value)
                        else:
                            try:
                                data_dict[key][ts] = float(value)
                            except (ValueError, TypeError):
                                data_dict[key][ts] = str(value)
                    except Exception as e:
                        logger.warning(f"[results] Failed to get result '{prop}' for tk '{tk}' at '{ts}': {e}")
        if n_calls:
            logger.info(f"[results] {n_calls:,} value(s) retrieved via GetResultfortimestamp() "
                        f"({time.perf_counter() - t_phase:.1f} s).")
        if data_dict:
            frames.append(self._cast_float_columns(pd.DataFrame(data_dict), self._MX_RESULT_DTYPE))

        if not frames:
            return pd.DataFrame()
        t_phase = time.perf_counter()
        for frame in frames:
            frame.columns.names = ["tk", "property", "interior points"][:frame.columns.nlevels]
        if bulk:
            df = frames[0]  # complete as read, see above
            if drop_full_place_holder_columns:
                logger.info(f"[results] {n_dropped} fully NaN columns dropped.")
        else:
            df = pd.concat(frames, axis=1) if len(frames) > 1 else frames[0]
            df = df.reindex(ts_labels)
            df = self._cast_float_columns(df.where(df.notna(), place_holder_value), self._MX_RESULT_DTYPE)

            # tk-major / property-minor column order
            df = self._mx_order_columns(df, tks, result_props)

            if drop_full_place_holder_columns:
                mask_placeholder_all = df.eq(place_holder_value).all()
                amount_of_dropped_cols = int(mask_placeholder_all.sum())
                df = df.loc[:, ~mask_placeholder_all]
                logger.info(f"[results] {amount_of_dropped_cols} fully NaN columns dropped.")
        df.index.name = "timestamp"
        logger.info(f"[results] DataFrame assembled ({time.perf_counter() - t_phase:.1f} s).")

        # --- Add Name and End Nodes to column MultiIndex ---
        label_by_tk = None
        if include_name_and_end_nodes:
            end_nodes_available = self.__is_get_endnodes_applicable(element_type=element_type)
            label_by_tk = self._result_column_labels(df.columns.get_level_values(0).unique(), end_nodes_available)
        df = self._add_name_and_end_node_levels(df, label_by_tk, result_props)

        logger.info(f"[results] Done. Shape: {df.shape} ({time.perf_counter() - t_start:.1f} s in total)")
        return df

    @staticmethod
    def _column_value_lists(df: pd.DataFrame) -> List[list]:
        """
        Every column's values as a Python list (for building tuples). float32 values become the Python
        float of their shortest decimal representation (0.01343678 instead of 0.01343678031116724, the
        exact binary value of the float32 written out as float64) - the same number at float32
        precision, just printed the way it was calculated/returned. Other values are returned as they are.
        """
        values: List[list] = [None] * df.shape[1]
        kinds = np.array([dtype == np.float32 for dtype in df.dtypes])
        if kinds.any():
            positions = np.flatnonzero(kinds)
            block = df.iloc[:, positions].to_numpy(np.float32)
            unique, inverse = np.unique(block, return_inverse=True)  # results repeat a lot: format each value once
            short = unique.astype(str).astype(np.float64)[inverse.reshape(-1)].reshape(block.shape)
            for pos, col_values in zip(positions, short.T.tolist()):
                values[pos] = col_values
        if (~kinds).any():
            positions = np.flatnonzero(~kinds)
            for pos, col_values in zip(positions, df.iloc[:, positions].to_numpy(object).T.tolist()):
                values[pos] = col_values
        return values

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
        
        rows_as_lists = self._column_value_lists(df)
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
    ) -> pd.DataFrame | gpd.GeoDataFrame:

        """
        Generates a comprehensive DataFrame containing model_data and static result values for all requested elements of the given type. Result values are written in the df as tuple of floats (or tuple (time) of tuple (interior point) of floats for pipe interior points) with each entry corresponding to a simulations timestamp. 
        Geometry and end-node tks are always included. All model_data and result values (self.GetResultProperties_from_elementType(onlySelectedVectors=False)) for are included.
        The tks of end nodes are included (fkKI, fkKK). Geometry information is also included.
        If you want to include non-static timestamps, explicitly provide them via the `timestamps` parameter.

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
            place_holder_value = 99999.0
            df_results = self.generate_element_results_dataframe(element_type=element_type
                                                                        ,tks=tks
                                                                        ,properties=None if bulk else result_values_to_obtain
                                                                        ,timestamps=timestamps
                                                                        ,place_holder_value=place_holder_value
                                                                        ,bulk=bulk
                                                                        ,vec_format="multiindex"
                                                                        ,include_name_and_end_nodes=False  # merged on tk only
            )
            if df_results.empty:
                logger.error(f"[generate_element_dataframe] Obtained results dataframe is empty.")
                return pd.DataFrame(), dict()

            logger.info(f"[generate_element_dataframe] Merging df_model_data with df_results for element type: {element_type} ...")
            df_merged = self.merge_model_data_and_results(df_model_data, df_results, place_holder_value)
            timestamp_to_tuple_index = {str(ts): pos for pos, ts in enumerate(df_results.index.tolist())}

            return df_merged, timestamp_to_tuple_index
        
        except Exception as e:
            logger.error(f"[generate_element_dataframe] Error Generating df for element type: {element_type}: {e}")
            return pd.DataFrame(), dict()
        
    @staticmethod
    def _results_to_element_rows(df_results: pd.DataFrame, place_holder_value: float) -> Tuple[pd.DataFrame, dict]:
        """
        One row per element from a vec_format="multiindex" results DataFrame (rows: timestamps; columns:
        tk, name, end_nodes, property, interior points), for generate_element_dataframe(): every scalar
        property becomes one tuple over the timestamps; every interior-point (VEC) property becomes
        <prop>_start / <prop>_end (tuples over the timestamps of the first/last interior point) and
        <prop>_sequence (tuple over the timestamps of tuples over the interior points). Timestamps where a
        VEC property is missing (all place_holder_value) give None / None / ().

        :return: (DataFrame indexed by tk, columns sorted by name; {timestamp: tuple position})
        :rtype: Tuple[pd.DataFrame, dict]
        """
        timestamp_to_tuple_index = {str(ts): pos for pos, ts in enumerate(df_results.index.tolist())}
        columns = df_results.columns
        tk_level = columns.get_level_values("tk")
        prop_level = columns.get_level_values("property")
        point_level = np.asarray(columns.get_level_values("interior points"))

        # Every column's values over the timestamps as a Python list (float32 in its shortest representation).
        values = SIR3S_Model_Dataframes._column_value_lists(df_results)

        # Group the columns of each (tk, property), in column order (interior points ascending).
        groups: Dict[Tuple[str, str], List[int]] = {}
        for pos, key in enumerate(zip(tk_level, prop_level)):
            groups.setdefault(key, []).append(pos)

        rows: Dict[str, Dict[str, object]] = {}
        for (tk, prop), positions in groups.items():
            row = rows.setdefault(tk, {})
            if len(positions) == 1 and point_level[positions[0]] == -1:
                row[prop] = tuple(values[positions[0]])
                continue
            per_timestamp = list(zip(*(values[p] for p in positions)))
            starts, ends, sequences = [], [], []
            for points in per_timestamp:
                if all(v == place_holder_value for v in points):
                    starts.append(None)
                    ends.append(None)
                    sequences.append(())
                else:
                    starts.append(points[0])
                    ends.append(points[-1])
                    sequences.append(tuple(points))
            row[f"{prop}_start"] = tuple(starts)
            row[f"{prop}_end"] = tuple(ends)
            row[f"{prop}_sequence"] = tuple(sequences)

        df = pd.DataFrame.from_dict(rows, orient="index")
        df = df.reindex(columns=sorted(df.columns)).sort_index()
        df.index.name = "tk"
        return df, timestamp_to_tuple_index

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
                # Keep scalar property untouched (as array, so float32 stays float32)
                new_cols[key if is_multi else key[0]] = df_results[col_key].to_numpy()

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

                    place_holder_value = 99999.0
                    df_results = self.generate_element_results_dataframe(
                        element_type=em,
                        properties=result_properties,
                        timestamps=timestamps,
                        tks=tks_to_use,
                        place_holder_value=place_holder_value,
                        vec_format="multiindex",
                        include_name_and_end_nodes=False,  # merged on tk only
                    )
                    if df_results.empty or df_results.shape[1] == 0:
                        df = df_model.copy()
                    else:
                        df = self.merge_model_data_and_results(df_model, df_results, place_holder_value)
                        timestamp_to_tuple_index = {str(ts): pos for pos, ts in enumerate(df_results.index.tolist())}
                    
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

    def get_result_file_properties(
        self,
        element_type: Optional[Enum] = None,
        output_factor: Optional[int] = None,
    ) -> pd.DataFrame:
        """
        List the result properties stored in the open model's result file, i.e. what
        generate_element_results_dataframe(bulk=True) can read from it - only the file's metadata is
        read, no result values.

        :param element_type: Only this element type (e.g. self.ObjectTypes.Pipe). Default: None (all
                        element types in the file).
        :type element_type: Enum, optional
        :param output_factor: Which result file, as in generate_element_results_dataframe(bulk=True):
                        None (default) - the file without an output factor in its name if it exists,
                        otherwise the DTFAK_GROSS file of the most recent calculation; a factor - the
                        file of that factor.
        :type output_factor: int, optional
        :return: One row per (element type, property) with columns
                - element_type: name in self.ObjectTypes (empty if the file's object type has none)
                - objtype: object type code in the result file (e.g. "ROHR")
                - property: result property name
                - unit, description: as stored in the result file (descriptions are in German)
                - stored_for: "all elements" (one value per element of the type), "single elements"
                  (only for individual elements, e.g. selected as time curves) or "not splittable"
                  (stored, but the values can't be assigned per element - bulk=True leaves these out)
                - result_file, n_timestamps: the file read and its number of timestamps
        :rtype: pd.DataFrame
        """
        mx_file = self._mx_get_file(self._mx_resolve_mx1(output_factor))
        if element_type is not None:
            objtypes = [self._mx_objtype(element_type)]
        else:
            objtypes = sorted({c.objtype for c in mx_file.channels.values() if c.objtype != "ALLG"})
        name_by_objtype = {}
        for member in self.ObjectTypes:
            code = mapping_for_groups.get(member.name)
            if code and code != -1:
                name_by_objtype.setdefault(code, member.name)
        meta = mx_file.mx1_df.drop_duplicates(["OBJTYPE", "ATTRTYPE"]).set_index(["OBJTYPE", "ATTRTYPE"])
        n_timestamps = len(self._mx_timeline_records(mx_file))

        rows = []
        for objtype in objtypes:
            layout = self._mx_object_layout(mx_file, objtype)
            groups = [("all elements", list(layout.scalar_channels) + list(layout.vector_channels)),
                      ("single elements", list(layout.single_channels)),
                      ("not splittable", layout.unresolvable_vector_props + layout.skipped_props)]
            for stored_for, props in groups:
                for prop in props:
                    info = meta.loc[(objtype, prop)] if (objtype, prop) in meta.index else {}
                    rows.append({"element_type": name_by_objtype.get(objtype, ""), "objtype": objtype,
                                 "property": prop, "unit": info.get("UNIT", ""), "description": info.get("TITLE", ""),
                                 "stored_for": stored_for})
        df = pd.DataFrame(rows, columns=["element_type", "objtype", "property", "unit", "description", "stored_for"])
        df["result_file"] = os.path.basename(mx_file.mx1_path)
        df["n_timestamps"] = n_timestamps
        logger.info(f"[results] {self._mx_describe_file(mx_file.mx1_path, output_factor)}: {len(df)} result properties of "
                    f"{df['objtype'].nunique()} element type(s), {n_timestamps} timestamps.")
        return df

    def merge_model_data_and_results(self, df_model_data, df_results, place_holder_value: float = 99999.0):
        """
        Merge model data with results into one row per element (on "tk").

        :param df_model_data: From generate_element_model_data_dataframe() (needs a "tk" column).
        :type df_model_data: pd.DataFrame
        :param df_results: Either
                - straight from generate_element_results_dataframe(vec_format="multiindex"), any number
                  of timestamps: merged directly; or
                - vec_format="str" results, prepared with add_interior_points_to_start_end_sequence()
                  and convert_rows_to_single_tuple_row() (one row).
                Either way, every result property becomes a tuple over the timestamps, and interior-point
                (VEC) properties become <prop>_start, <prop>_end and <prop>_sequence. Results with or
                without the name/end_nodes column levels (include_name_and_end_nodes) are accepted; df_results
                itself isn't modified.
        :type df_results: pd.DataFrame
        :param place_holder_value: Only for vec_format="multiindex" results: the place_holder_value they were
                generated with (timestamps where an interior-point property is missing give None / ()).
                Default: 99999.0
        :type place_holder_value: float, optional
        :return: Merged DataFrame (empty on error).
        :rtype: pd.DataFrame
        """
        try:
            if df_results is None or df_results.empty or len(df_results.columns) == 0:
                return df_model_data.copy()

            if "interior points" in (df_results.columns.names or []):
                df_element_results, _ = self._results_to_element_rows(df_results, place_holder_value)
                return df_model_data.merge(on="tk", how="outer", right=df_element_results)

            if not df_results.empty and df_results.index.nunique() > 1:
                logger.error( "[merge] Aborting merge: df_results contains multiple timestamps.Please provide a single timestamp.")
                return pd.DataFrame()

            # name/end_nodes levels only exist with include_name_and_end_nodes=True; shallow copy so the
            # caller's DataFrame keeps its columns
            df_results = df_results.copy(deep=False)
            drop_levels = [level for level in ("name", "end_nodes") if level in (df_results.columns.names or [])]
            if drop_levels:
                df_results.columns = df_results.columns.droplevel(drop_levels)
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
        if "tk" not in df.columns:
            if df.index.name == "tk":
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
    