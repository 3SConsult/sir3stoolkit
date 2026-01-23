# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 12:11:41 2026

This module implements functions that extend the basic C# operations with more advanced operations to change a SIR 3S model.

@author: Jablonski
"""

from typing import List, Tuple, Any

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

    def add_elements_to_group(
        self,
        group_tk: int,
        element_tks: List[Tuple[str, str]]
    ): 
        """
        Docstring for add_elements_to_group
        
        :param self: Description
        :param group_tk: Description
        :type group_tk: int
        :param element_tks: Description
        :type element_tks: list[tuple(int, int)]
        """

        # --- Validate Input Data ---
        available_group_tks=self.GetTksofElementType(self.ObjectTypes.LAYR_Layer)
        if group_tk not in available_group_tks:
            logger.debug(f"[insert into group] given tk for group {group_tk} does not exist.")
            return -1
        
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
                logger.info(f"[insert into group] element tk {tk} does not exist in model. Excluding...")

        # --- Get current group object string ---
        current_element_tks = self.get_tks_of_group_elements(group_tk=group_tk)
        element_tks_to_be = current_element_tks + valid_element_tks
        element_obj_string = self.build_group_objs_string(element_tks_to_be)
        self.SetValue(group_tk, "ObjsString",element_obj_string)

    def add_element_types_to_tk_list(
        self,
        tks: List[str]
    ) -> List[Tuple[str, str]]:
        """
        Only works for DistrictHeating networks
        
        :param self: Description
        :param tks: Description
        :type tks: List[str]
        :return: Description
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
        Docstring for get_tks_of_group_elements
        
        :param self: Description
        :param group_tk: Description
        :type group_tk: int
        :return: Description
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


    def build_group_objs_string(
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
        Docstring for get_element_type_from_tk
        
        :param self: Description
        :return: Description
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
