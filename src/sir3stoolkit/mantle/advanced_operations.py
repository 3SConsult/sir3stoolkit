# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 12:11:41 2026

This module implements functions that extend the basic C# operations with more advanced operations to change a SIR 3S model.

AI assistant: see sir3stoolkit/__init__.py for orientation (architecture, API/property reference,
known gotchas) before writing code against this module.

@author: Jablonski
"""

from typing import List, Tuple, Any
from datetime import datetime

from sir3stoolkit.dependency_check import require_packages
require_packages(__name__, "pandas")

import pandas as pd
import numpy as np

from sir3stoolkit.logging_utils import get_logger

logger = get_logger(__name__)

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

# --- Mappings ---

# Maps every ObjectTypes .NET class name to its MX/SIR3S OBJTYPE (table) code, Generated from the toolkit's own
# self.ObjectTypes_TableNames / GetPropertiesofElementType() / GetResultProperties_from_elementType(). Equivalent to API Documentation 
mapping_for_groups = {'AGSN_HydraulicProfile': 'AGSN',
'AirVessel': 'WIND',
'Arrow': 'ARRW',
'Atmosphere': 'ATMO',
'BlockConnectionNode': 'VKNO',
'CalcPari': 'PARI',
'CharacteristicLossTable': 'ZEP2',
'CharacteristicLossTable_Row': 'ZEP2_ROWS',
'Circle': 'CIRC',
'Compressor': 'KOMP',
'CompressorTable': 'KOMK',
'CompressorTable_Row': 'KOMK_ROWS',
'ControlEngineeringNexus': 'CRGL',
'ControlMode': 'RART',
'ControlPointTable': 'RCPL',
'ControlPointTable_Row': 'RCPL_ROWT',
'ControlValve': 'REGV',
'ControlVariableConverter': 'RSTN',
'ControlVariableConverterRSTE': 'RSTE',
'CrossSectionTable': 'AVOS',
'CrossSectionTable_Row': 'AVOS_ROWS',
'DPGR_DPKT_DatapointDpgrConnection': 'DPGR_DPKT',
'DPGR_DataPointGroup': 'DPGR',
'DPKT_Datapoint': 'DPKT',
'DamageRatesTable': 'SRAT',
'DamageRatesTable_Row': 'SRAT_ROWS',
'DeadTimeElement': 'RTOT',
'Demand': 'VERB',
'DifferentialRegulator': 'DPRG',
'DirectionalArrow': 'RPFL',
'DistrictHeatingConsumer': 'FWVB',
'DistrictHeatingFeeder': 'FWES',
'Divider': 'RDIV',
'DriveEfficiencyTable': 'ETAM',
'DriveEfficiencyTable_Row': 'ETAM_ROWS',
'DrivePowerTable': 'ANTP',
'DrivePowerTable_Row': 'ANTP_ROWS',
'EBES_FeederGroups': 'EBES',
'EfficiencyConverterTable': 'ETAU',
'EfficiencyConverterTable_Row': 'ETAU_ROWS',
'ElementQuery': 'ELEMENTQUERY',
'EnergyRecoveryTable': 'ETAR',
'EnergyRecoveryTable_Row': 'ETAR_ROWS',
'EnvironmentTemp': 'UTMP',
'FWBZ_DistrictHeatingReferenceValues': 'FWBZ',
'FlapValve': 'KLAP',
'FlowControlUnit': 'MREG',
'FluidQualityParamSet': 'FQPS',
'FluidQualityParamSet_OS': 'FQPS_BZ',
'FluidThermalPropertyGroup': 'FSTF',
'FreeDuct': 'FKNL',
'FunctionGenerator': 'RFKT',
'FunctionTable': 'TFKT',
'FunctionTable_Row': 'TFKT_ROWS',
'GasComponent': 'GKMP',
'GasMixture': 'GMIX',
'GeneralSection': 'ALLG',
'Gravitation': 'GRAV',
'HeatExchanger': 'FWWU',
'HeatFeederConsumerStation': 'FWEA',
'HeaterCooler': 'GVWK',
'Histeresis': 'RHYS',
'House': 'HAUS',
'Hydrant': 'HYDR',
'Integrator': 'RINT',
'LAYR_Layer': 'LAYR',
'LoadFactorTable': 'LFKT',
'LoadFactorTable_Row': 'LFKT_ROWT',
'LogicalComparison': 'RLVG',
'LogicalStorage': 'RLSR',
'MeasuredVariableTable': 'SWVT',
'MeasuredVariableTable_Row': 'SWVT_ROWT',
'MinMaxSelection': 'RMMA',
'Multiplier': 'RMUL',
'NetValve': 'NSCH',
'Node': 'KNOT',
'NonReturnValvesTable': 'PHIV',
'NonReturnValvesTable_Row': 'PHIV_ROWS',
'NumericalDisplay': 'NRCV',
'ObjectContainerSymbol': 'CONT',
'OpenContainer': 'OBEH',
'Oval': 'OVAL',
'PARZ_TransientCalculationParameters': 'PARZ',
'PhaseSeparation': 'PHTR',
'PidController': 'RPID',
'Pipe': 'ROHR',
'PipeGroup': 'LTGR',
'PipeTable': 'DTRO',
'PipeTable_Row': 'DTRO_ROWD',
'PipeVertex': 'ROHR_VRTX',
'Polygon': 'PLYG',
'Polyline': 'POLY',
'PressureRegulator': 'PREG',
'PressureZone': 'PZON',
'Pt1Controller': 'RPT1',
'Pump': 'PUMP',
'PumpCharTable': 'PUMK',
'PumpCharTable_Row': 'PUMK_ROWS',
'PumpGroup': 'PGRP',
'PumpOfPumpGroup': 'PGRP_PUMP',
'PumpSpeedTable': 'PUMD',
'PumpSpeedTable_Row': 'PUMD_ROWT',
'RART_ControlMode': -1,
'REGP_ControlParameters': 'REGP',
'RMES_DPTS_RmesInternalDataPoint': 'RMES_DPTS',
'Rectangle': 'RECT',
'RegulatorsTable': 'ZEP1',
'RegulatorsTable_Row': 'ZEP1_ROWS',
'ReturnTemperaturTable': 'TRFT',
'ReturnTemperaturTable_Row': 'TRFT_ROWS',
'RoundRectangle': 'RRCT',
'SIRGRAF': -1,
'SPLZ_TimeSeries': 'SPLZ',
'SafetyValve': 'SIVE',
'SetpointDevice': 'RSLW',
'SolarCollector': 'SOKO',
'StandPipe': 'STRO',
'Street': 'STRASSE',
'SummingPoint': 'RADD',
'SwitchInBlock': 'BREF',
'TemperatureTable': 'TEVT',
'TemperatureTable_Row': 'TEVT_ROWT',
'Text': 'GTXT',
'ThermalOutputTable': 'WEVT',
'ThermalOutputTable_Row': 'WEVT_ROWT',
'ThermophysPropTable': 'STOF',
'ThermophysPropTable_Row': 'STOF_ROWS',
'TransitionSymbol': 'RUES',
'Transmitter': 'RMES',
'TransportVariable': 'TRVA',
'USCH_UserDefinedProperties': 'USCH',
'Unknown': -1,
'VARA_ColorScale': 'VARA',
'VARA_ROWS_WidthOrScale': 'VARA_ROWS',
'VRCT_ViewRectangle': 'VRCT',
'Valve': 'VENT',
'ValveLiftTable': 'PHI1',
'ValveLiftTable_Row': 'PHI1_ROWT',
'VarFlowTable': 'QVAR',
'VarFlowTable_Row': 'QVAR_ROWT',
'VarPressureTable': 'PVAR',
'VarPressureTable_Row': 'PVAR_ROWT',
'VentOpenCloseTable': 'PHI2',
'VentOpenCloseTable_Row': 'PHI2_ROWS',
'VentValve': 'BEVE',
'VentilatedPressureAirVessel': 'BEWI',
'WBLZ_ThermalBalance': 'WBLZ',
'WeatherDataTable': 'WTTR',
'WeatherDataTable_Row': 'WTTR_ROWT'}
