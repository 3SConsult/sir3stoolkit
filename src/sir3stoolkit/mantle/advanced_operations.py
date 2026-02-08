# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 12:11:41 2026

This module implements functions that extend the basic C# operations with more advanced operations to change a SIR 3S model.

@author: Jablonski
"""

from typing import List, Tuple, Any
import pandas as pd
from datetime import datetime
import numpy as np

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

from sir3stoolkit.core.wrapper import SIR3S_Model

class SIR3S_Model_Advanced_Operations(SIR3S_Model):
    """
    This class implements functions that extend the basic C# operations with more advanced operations to change a SIR 3S model.
    """

    def set_group_elements(
        self,
        group_tk: int,
        element_tks: List[Tuple[str, str]]
    ) -> None | int:
        """
        Overwrites elements in a group with a new list of elements.

        :param self:
        :param group_tk: Tk of the group the elements should be set for.
        :type group_tk: int
        :param element_tks: Tks of elements that should be set for the group.
            Eg. [('KNOT', '5428054456958551597'),
                ('KNOT', '5099111544186125239')]
        :type element_tks: list[tuple[str, str]]
        """
        
        # --- Validate Input Data ---
        valid_group_tk = -1
        available_group_tks=self.GetTksofElementType(self.ObjectTypes.LAYR_Layer)
        if group_tk not in available_group_tks:
            logger.error(f"[validate_group_changes_data] given tk for group {group_tk} does not exist.")
            return -1
        else:
            valid_group_tk = group_tk
            
        object_types = [item for item in dir(self.ObjectTypes) if not (item.startswith('__') and item.endswith('__'))]
        available_tks = []
        for object_type in object_types:
            for tk in self.GetTksofElementType(self.ObjectTypes[object_type]):
                available_tks.append(tk)

        valid_element_tks = []
        for idx, (_, tk) in enumerate(element_tks):
            if tk in available_tks:
                valid_element_tks.append(element_tks[idx])
            else:
                logger.info(f"validate_group_changes_data] element tk {tk} does not exist in model. Excluding...")

        # --- Set ---
        element_obj_string = self._build_group_objs_string(valid_element_tks)
        self.SetValue(valid_group_tk, "ObjsString",element_obj_string)

        
        # --- Check ---
        if len(self.get_tks_of_group_elements(group_tk=valid_group_tk)) == len(valid_element_tks):
            logger.info(f"[set elements for group] Check successful")
        else:
            logger.info(f"[set elements for group] Check unsuccessful. Mismatch in amount of elements in edited group and intended amount.")

    def add_elements_to_group(
        self,
        group_tk: int,
        element_tks: List[Tuple[str, str]]
    ) -> None | int:
        """
        Adds elements to a group with a list of elements.

        :param self:
        :param group_tk: Tk of the group the elements should be added to.
        :type group_tk: int
        :param element_tks: Tks of elements that should be added to the group.
            Eg. [('KNOT', '5428054456958551597'),
                ('KNOT', '5099111544186125239')]
        :type element_tks: list[tuple[str, str]]
        """


        # --- Validate Input Data ---
        valid_group_tk, valid_element_tks = self._validate_group_changes_data(group_tk, element_tks, False)

        if valid_group_tk == -1 or len(valid_element_tks) == 0:
            logger.error(f"[add elements to group] invalid input data")
            return -1
        
        # --- Get current group object string ---
        current_element_tks = self.get_tks_of_group_elements(group_tk=group_tk)
        element_tks_to_be = current_element_tks + valid_element_tks
        element_obj_string = self._build_group_objs_string(element_tks_to_be)

        # --- Add --
        self.SetValue(valid_group_tk, "ObjsString",element_obj_string)

        # --- Check ---
        if len(self.get_tks_of_group_elements(group_tk=valid_group_tk)) == len(element_tks_to_be):
            logger.info(f"[add elements to group] Check successful")
        else:
            logger.info(f"[add elements to group] Check unsuccessful. Mismatch in amount of elements in edited group and intended amount.")

    def remove_elements_from_group(
        self,
        group_tk: int,
        element_tks: List[Tuple[str, str]]
    ) -> None | int:
        """
        Removes elements from a group with a list of elements.

        :param self:
        :param group_tk: Tk of the group the elements should be removed from.
        :type group_tk: int
        :param element_tks: Tks of elements that should be removed from the group.
            Eg. [('KNOT', '5428054456958551597'),
                ('KNOT', '5099111544186125239')]
        :type element_tks: list[tuple[str, str]]
        """


        # --- Validate Input Data ---
        valid_group_tk, valid_element_tks = self._validate_group_changes_data(group_tk, element_tks, True)

        if valid_group_tk == -1 or len(valid_element_tks) == 0:
            logger.info(f"[remove elements from group] invalid input data")
            return -1
        
        # --- Get current group object string ---
        current_element_tks = self.get_tks_of_group_elements(group_tk=group_tk)
        remove = set(valid_element_tks) 
        element_tks_to_be = [tk for tk in current_element_tks if tk not in remove]
        element_obj_string = self._build_group_objs_string(element_tks_to_be)
        
        # --- Add --
        self.SetValue(valid_group_tk, "ObjsString",element_obj_string)

        # --- Check ---
        if len(self.get_tks_of_group_elements(group_tk=valid_group_tk)) == len(element_tks_to_be):
            logger.info(f"[remove elements from group] Check successful")
        else:
            logger.info(f"[remove elements from group] Check unsuccessful. Mismatch in amount of elements in edited group and intended amount.")

    def _validate_group_changes_data(
        self,
        group_tk: int,
        element_tks: List[Tuple[str, str]],
        remove_or_add: bool, # True for remove, False for add
    ) -> Tuple[int, List[Tuple[str, str]]]:
        """
        Needed for remove_elements_from_group() and add_elements_to_group(). validates inputs for them.
        
        :param self:
        :param group_tk: Tk of the group that should be validated
        :type group_tk: int
        :param element_tks: Tks of elements, that should be validated. Eg. [('KNOT', '5428054456958551597'), ('KNOT', '5099111544186125239')]
        :type element_tks: list[tuple(str, str)]
        :param remove_or_add: True for remove, False for add
        :type remove_or_add: bool
        """
        # --- Group tk ---
        valid_group_tk = -1
        available_group_tks=self.GetTksofElementType(self.ObjectTypes.LAYR_Layer)
        if group_tk not in available_group_tks:
            logger.info(f"[validate_group_changes_data] given tk for group {group_tk} does not exist.")
        else:
            valid_group_tk = group_tk
        
        # --- Element tks ---
        object_types = [item for item in dir(self.ObjectTypes) if not (item.startswith('__') and item.endswith('__'))]
        available_tks = []
        for object_type in object_types:
            for tk in self.GetTksofElementType(self.ObjectTypes[object_type]):
                available_tks.append(tk)
        available_elements_in_group = self.get_tks_of_group_elements(group_tk=group_tk)
        available_tks_in_group = [element[1] for element in available_elements_in_group]

        valid_element_tks = []
        for idx, (_, tk) in enumerate(element_tks):
            if tk in available_tks:
                if remove_or_add:
                    if tk in available_tks_in_group:
                        valid_element_tks.append(element_tks[idx])
                    else:
                        logger.info(f"validate_group_changes_data] element tk {tk} does not lie in group {group_tk}. Excluding...")
                else:
                    if tk not in available_tks_in_group:
                        valid_element_tks.append(element_tks[idx])
                    else:
                        logger.info(f"validate_group_changes_data] element tk {tk} already lies in group {group_tk}. Excluding...")
            else:
                logger.info(f"validate_group_changes_data] element tk {tk} does not exist in model. Excluding...")

        return valid_group_tk, valid_element_tks

    def add_element_types_to_tk_list(
        self,
        tks: List[str]
    ) -> List[Tuple[str, str]]:
        """
        Turns list of tks into list of tuples with element type and tk. Only works for DistrictHeating networks. For other mappings we need an additional mapping. see sir3stoolkit/docs/code snippets/mapping_for_groups.ipynb
        
        :param self: 
        :param tks: List of tks of elements like ['5428054456958551597', '50736424189751239']
        :type tks: List[str]
        :return: [('KNOT', '5428054456958551597'), ('ROHR', '50736424189751239')]
        :rtype: List[Tuple[str, str]]
        """

        element_type_alternative_names = []
        for tk in tks:
            element_type = self.get_element_type_from_tk(tk)
            element_type_alternative_name = mapping_for_groups[element_type]
            element_type_alternative_names.append(element_type_alternative_name)

        element_types_with_tks = list(zip(element_type_alternative_names, tks))
        return element_types_with_tks

    
    def get_tks_of_group_elements(
            self,
            group_tk: int
    ) -> List[Tuple[str, str]]:
        """
        Returns list of tuples with element type and tk of elements that are part of specific group.
        
        :param self: 
        :param group_tk: Tk of group for element tk retrival
        :type group_tk: int
        :return: List of tuples with element type and tk of elements of group.
        :rtype: Any
        """

        # --- Validate Input Data ---
        available_group_tks=self.GetTksofElementType(self.ObjectTypes.LAYR_Layer)
        if group_tk not in available_group_tks:
            logger.error(f"[get group tks] given tk for group {group_tk} does not exist.")
            return -1

        # --- Get group object string
        ObjStr = self.GetValue(group_tk, "ObjsString")[0]
        current_group_tks = []
        for element in ObjStr.split('\t'):
            if element: 
                obj_type, obj_tk = element.split('~')
                current_group_tks.append((obj_type, obj_tk))

        return current_group_tks


    def _build_group_objs_string(
        self,
        group_tks: List[Tuple[str, int | str]]
    ) -> str:
        """
        Build an ObjStr from a list of (object_type, object_tk) tuples.

        Format:
        "TYPE~tk\tTYPE~tk\t..."
        """

        return "\t".join(f"{obj_type}~{obj_tk}" for obj_type, obj_tk in group_tks) + "\t"

    def get_element_type_from_tk(
        self,
        tk: str
    ) -> str:
        """
        Return element type for given tk.
        
        :param self:
        :param tk: Tk of element
        :type tk: int
        :return: element type
        :rtype: str
        """

        object_types = [item for item in dir(self.ObjectTypes) if not (item.startswith('__') and item.endswith('__'))]
        for object_type in object_types:
            tks=self.GetTksofElementType(self.ObjectTypes[object_type])
            if tk in tks:
                return object_type

        # If tk is not found     
        return -1

    # time Table
    def insert_dataframe_into_time_table(
        self,
        time_table_tk: str,
        dataframe: pd.DataFrame,
        reference_time_stamp = None,
        date_col: str = "TAG",
        time_col: str = "UHRZEIT",
        value_col: str = "WERT",
        dt_format: str = "%Y-%m-%d %H:%M:%S.%f",
    ) -> None:
        """
        Sets (overwrites previous) time-value pairs for time table based on provided dataframe.

        :param self:
        :param time_table_tk: Tk of time table (["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable"]) to set time-value pairs for.
        :type time_table_tk: int
        :param dataframe: Pandas dataframe with date_col, time_col, value_col
        :type dataframe: pd.Dataframe
        :param reference_time_stamp: "0-timestamp" - the difference to this timestamp will be calculated for each timestamp in the dataframe and used in the time table, default=self.GetTimeStamps()[0][0] - first simulation timestamp, values like "%Y-%m-%d %H:%M:%S.%f"
        :type reference_time_stamp: str
        :param date_col: Name of date col in dataframe, default = "TAG", values like "2026-01-01", "%Y-%m-%d"
        :type date_col: str
        :param time_col: Name of time col in dataframe, default = "UHRZEIT", values like "00:00:20.000000", "%H:%M:%S.%f"
        :type time_col: str
        :param value_col: Name of value col in dataframe, default = "WERT", values like 83 or 1.2
        :type value_col: str
        """

        # --- Input data validation ---
        logger.info("[insert dataframe into time table] Validating input data ...")
        available_time_table_tks=[]

        for type in ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable"]:
            tks = self.GetTksofElementType(self.ObjectTypes[type])
            available_time_table_tks.extend(tks)

        if time_table_tk not in available_time_table_tks:
            logger.error(f"[insert dataframe into time table] Time table with tk {time_table_tk} does not exist.")
            return -1
        
        if dataframe.empty:
            logger.error(f"[insert dataframe into time table] Dataframe is empty.")
            return -1
        
        available_dataframe_columns = dataframe.columns
        if date_col not in available_dataframe_columns:
            logger.error(f"[insert dataframe into time table] Date col {date_col} not in dataframe columns.")
            return -1
        if time_col not in available_dataframe_columns:
            logger.error(f"[insert dataframe into time table] Time col {time_col} not in dataframe columns.")
            return -1
        if value_col not in available_dataframe_columns:
            logger.error(f"[insert dataframe into time table] Value col {value_col} not in dataframe columns.")
            return -1
    
        if reference_time_stamp:
            used_reference_time_stamp = reference_time_stamp
        elif self.GetTimeStamps()[0][0]:
            s = self.GetTimeStamps()[0][0]
            used_reference_time_stamp = s.split()[0] + " " + s.split()[1]
        else:
            logger.error(f"[insert dataframe into time table] No valid simulation timestamp in model, nor reference time stamp given.")
            return -1
        used_reference_time_stamp_as_datetime = datetime.strptime(used_reference_time_stamp, "%Y-%m-%d %H:%M:%S.%f")

        df = dataframe[[date_col, time_col, value_col]].copy()
        logger.info("[insert dataframe into time table] Successfully validated input data.")

        # --- From timestamp to simulation time ---
        ts_series = pd.to_datetime(
            df[date_col].astype(str) + " " + df[time_col].astype(str),
            format="%Y-%m-%d %H:%M:%S.%f",
            errors="coerce"     
        )

        delta_sec = (ts_series - used_reference_time_stamp_as_datetime).dt.total_seconds()
        df["delta_time_col"] = delta_sec

        property_name, _ = self._get_time_table_col_name_from_tk(time_table_tk=time_table_tk)

        # --- Inserting value pairs into model ---
        logger.info("[insert dataframe into time table] Inserting value pairs ...")
        try:
            for id, row in df.iterrows():
                t = row["delta_time_col"]
                v = row[value_col]
                tk_new_row = self.AddTableRow(tablePkTk=time_table_tk)[0]
                self.SetValue(Tk=tk_new_row, propertyName="Zeit", Value=str(t))
                self.SetValue(Tk=tk_new_row, propertyName=property_name, Value=str(v))
        except Exception as e:
            logger.error(f"[insert dataframe into time table] Error inserting value pairs into model: {e}")
        
        logger.info("[insert dataframe into time table] Successfully inserted value pairs")

    def get_dataframes_from_time_table_type(
        self,
        time_table_type: str,
    ) -> List[pd.DataFrame]:
        """
        Get DataFrames for all time tables of a given type and a joint horizontally concatenated DataFrame.

        This function:
        1) Validates the requested time table type.
        2) Retrieves all table tokens (TKs) for that type.
        3) Builds one DataFrame per TK via ``self.get_dataframe_from_time_table(...)`` with the
            table's Name property used as the value column name.
        4) If more than one table exists, horizontally concatenates them (column-wise) aligned on
            their row indexes using an **outer join**, then sorts the index ascending.
            Otherwise, returns the single DataFrame as-is.
        5) Returns the joint DataFrame, the per-TK DataFrames mapping, and the ordered list of TKs.

        :param self:
        :param time_table_type: The time table type to extract. Must be one of:
                                ["VarPressureTable", "VarFlowTable", "ValveLiftTable",
                                "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable"].
        :type time_table_type: str
        :return: A tuple containing:
                - df_h: The joint DataFrame. If multiple tables are found, this is a column-wise
                        concatenation (``axis=1``, ``join='outer'``) of all per-TK DataFrames with
                        the index sorted ascending. If only one table exists, it is returned directly.
                - dfs: A dictionary mapping each TK to its corresponding DataFrame
                        (key: TK, value: DataFrame).
                - tks_of_time_table_type: The list of TKs for the requested time table type, in the
                        order returned by ``GetTksofElementType``.
        :rtype: tuple[pd.DataFrame, dict[Any, pd.DataFrame], list[Any]]
        """
        logger.info(f"[get dataframes from time table type] ...")
        # --- Validate input ---
        
        if time_table_type not in ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable"]:
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
            df_h = pd.concat(dfs.values(), axis=1, join='outer')
            df_h = df_h.sort_index(ascending=True)
        else:
            df_h = dfs[tks_of_time_table_type[0]]

        logger.info(f"[get dataframes from time table type] Successful")

        return df_h, dfs, tks_of_time_table_type
        

    def get_dataframe_from_time_table(
        self,
        time_table_tk: str,
        value_col_name: str = None,
        time_col: str = "Zeit [s]"
    ) -> None:
        """
        Obtain time variable table (tables = ["VarPressureTable", "VarFlowTable", "ValveLiftTable", "PumpSpeedTable", "MeasuredVariableTable", "LoadFactorTable"]) in format of a pandas dataframe with time and value column.
        
        :param self: 
        :param time_table_tk: Tk of time table to get time-value pairs from.
        :type time_table_tk: str
        :param value_col: Name given to the value column
        :type value_col: str
        :param time_col: Name given to the time column, Default = "Zeit"
        :type time_col: str
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

        data = {}
        for tk in row_tks:
            time = self.GetValue(tk, "Zeit")[0]
            time = float(time)
            value = self.GetValue(tk, value_name)[0]
            value = float(value)
            data[time] = value

        if data == {}:
            logger.info("[get dataframe from time table] time table is empty.")
            df = pd.DataFrame(data=[[np.nan]], index=[0.0], columns=[value_name])
        else:
            df = pd.DataFrame.from_dict(data, orient='index', columns=[value_col_name_to_use])
            df.index.name = time_col
            logger.info("[get dataframe from time table] Successfully built dataframe.")

        return df

    def _get_time_table_col_name_from_tk(
        self,
        time_table_tk: str        
    ) -> str:
        
        if time_table_tk in self.GetTksofElementType(self.ObjectTypes.VarPressureTable):
            value_name = 'Ph'                                                                    # needed to retrieve numeric value from row
            _value_col_name = 'Druck p [bar]'                                                     # needed to name column in output df
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
        else:
            logger.error(f"[_get_time_table_col_name_from_tk] No time table with tk {time_table_tk}")
            return -1, -1
        
        return value_name, _value_col_name
         

# --- Mappings ---

# Only for District Heating    
mapping_for_groups = {'AGSN_HydraulicProfile': -1,
'AirVessel': 'WIND',
'Arrow': 'ARRW',
'Atmosphere': -1,
'BlockConnectionNode': 'VKNO',
'CalcPari': -1,
'CharacteristicLossTable': -1,
'CharacteristicLossTable_Row': -1,
'Circle': 'CIRC',
'Compressor': -1,
'CompressorTable': -1,
'CompressorTable_Row': -1,
'ControlEngineeringNexus': 'CRGL',
'ControlMode': -1,
'ControlPointTable': -1,
'ControlPointTable_Row': -1,
'ControlValve': 'REGV',
'ControlVariableConverter': 'RSTN',
'ControlVariableConverterRSTE': 'RSTE',
'CrossSectionTable': -1,
'CrossSectionTable_Row': -1,
'DPGR_DPKT_DatapointDpgrConnection': -1,
'DPGR_DataPointGroup': -1,
'DPKT_Datapoint': -1,
'DamageRatesTable': -1,
'DamageRatesTable_Row': -1,
'DeadTimeElement': 'RTOT',
'Demand': 'VERB',
'DifferentialRegulator': 'DPRG',
'DirectionalArrow': 'RPFL',
'DistrictHeatingConsumer': 'FWVB',
'DistrictHeatingFeeder': 'FWES',
'Divider': 'RDIV',
'DriveEfficiencyTable': -1,
'DriveEfficiencyTable_Row': -1,
'DrivePowerTable': -1,
'DrivePowerTable_Row': -1,
'EBES_FeederGroups': -1,
'EfficiencyConverterTable': -1,
'EfficiencyConverterTable_Row': -1,
'ElementQuery': -1,
'EnergyRecoveryTable': -1,
'EnergyRecoveryTable_Row': -1,
'EnvironmentTemp': -1,
'FWBZ_DistrictHeatingReferenceValues': -1,
'FlapValve': 'KLAP',
'FlowControlUnit': 'MREG',
'FluidQualityParamSet': -1,
'FluidQualityParamSet_OS': -1,
'FluidThermalPropertyGroup': -1,
'FreeDuct': 'FKNL',
'FunctionGenerator': 'RFKT',
'FunctionTable': -1,
'FunctionTable_Row': -1,
'GasComponent': -1,
'GasMixture': -1,
'GeneralSection': -1,
'Gravitation': -1,
'HeatExchanger': 'FWWU',
'HeatFeederConsumerStation': 'FWEA',
'HeaterCooler': -1,
'Histeresis': 'RHYS',
'House': 'HAUS',
'Hydrant': -1,
'Integrator': 'RINT',
'LAYR_Layer': -1,
'LoadFactorTable': -1,
'LoadFactorTable_Row': -1,
'LogicalComparison': 'RLVG',
'LogicalStorage': 'RLSR',
'MeasuredVariableTable': -1,
'MeasuredVariableTable_Row': -1,
'MinMaxSelection': 'RMMA',
'Multiplier': 'RMUL',
'NetValve': 'NSCH',
'Node': 'KNOT',
'NonReturnValvesTable': -1,
'NonReturnValvesTable_Row': -1,
'NumericalDisplay': 'NRCV',
'ObjectContainerSymbol': 'CONT',
'OpenContainer': 'OBEH',
'Oval': 'OVAL',
'PARZ_TransientCalculationParameters': -1,
'PhaseSeparation': -1,
'PidController': 'RPID',
'Pipe': 'ROHR',
'PipeGroup': -1,
'PipeTable': -1,
'PipeTable_Row': -1,
'PipeVertex': -1,
'Polygon': 'PLYG',
'Polyline': 'POLY',
'PressureRegulator': 'PREG',
'PressureZone': -1,
'Pt1Controller': 'RPT1',
'Pump': 'PUMP',
'PumpCharTable': -1,
'PumpCharTable_Row': -1,
'PumpGroup': 'PGRP',
'PumpOfPumpGroup': -1,
'PumpSpeedTable': -1,
'PumpSpeedTable_Row': -1,
'RART_ControlMode': -1,
'REGP_ControlParameters': -1,
'RMES_DPTS_RmesInternalDataPoint': -1,
'Rectangle': 'RECT',
'RegulatorsTable': -1,
'RegulatorsTable_Row': -1,
'ReturnTemperaturTable': -1,
'ReturnTemperaturTable_Row': -1,
'RoundRectangle': 'RRCT',
'SIRGRAF': -1,
'SPLZ_TimeSeries': -1,
'SafetyValve': 'SIVE',
'SetpointDevice': 'RSLW',
'SolarCollector': -1,
'StandPipe': -1,
'Street': 'STRASSE',
'SummingPoint': 'RADD',
'SwitchInBlock': 'BREF',
'TemperatureTable': -1,
'TemperatureTable_Row': -1,
'Text': 'GTXT',
'ThermalOutputTable': -1,
'ThermalOutputTable_Row': -1,
'ThermophysPropTable': -1,
'ThermophysPropTable_Row': -1,
'TransitionSymbol': 'RUES',
'Transmitter': 'RMES',
'TransportVariable': -1,
'USCH_UserDefinedProperties': -1,
'Unknown': -1,
'VARA_ColorScale': -1,
'VARA_ROWS_WidthOrScale': -1,
'VRCT_ViewRectangle': -1,
'Valve': 'VENT',
'ValveLiftTable': -1,
'ValveLiftTable_Row': -1,
'VarFlowTable': -1,
'VarFlowTable_Row': -1,
'VarPressureTable': -1,
'VarPressureTable_Row': -1,
'VentOpenCloseTable': -1,
'VentOpenCloseTable_Row': -1,
'VentValve': -1,
'VentilatedPressureAirVessel': -1,
'WBLZ_ThermalBalance': -1,
'WeatherDataTable': -1,
'WeatherDataTable_Row': -1}
