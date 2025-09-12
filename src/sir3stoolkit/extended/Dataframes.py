# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 09:22:31 2025

@author: Jablonski
"""

from attrs import field
from pytoolconfig import dataclass
from sir3stoolkit.core.wrapper import SIR3S_Model

import pandas as pd
import sys
from dataclasses import dataclass, field

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class Dataframes_SIR3S_Model(SIR3S_Model):
    """
    This class is supposed to extend the general SIR3S_Model class with the possibility of using pandas dataframes when working with SIR 3S. Getting dataframes, inserting elements via dataframes, running algorithms on dataframes should be made possible.
    """

    @dataclass
    class DataFrames:
        df_node: pd.DataFrame = field(default_factory=pd.DataFrame)
        df_pipe: pd.DataFrame = field(default_factory=pd.DataFrame)

    def __init__(self):
        super().__init__()
        self.data_frames = self.DataFrames()

    def generate_dataframes(self):
        """
        Manually generate and populate all relevant dataframes.

        Inlcude optional param with ElemenTypes to only create certain dataframes
        """
        if not self.__is_a_model_open():
            logger.warning("No model is open. Cannot generate dataframes.")
            return

        logger.info("Generating dataframes...")
        
        logger.info("Generating df_node...")
        _non_result_props=self.GetPropertiesofElementType(self.ObjectTypes.Node)
        _result_props=self.GetResultProperties_from_elementType(self.ObjectTypes.Node, onlySelectedVectors=True)
        self.data_frames.df_node = self.generate_element_dataframe(non_result_props=_non_result_props, result_props=_result_props, element_type=self.ObjectTypes.Node)
        logger.info("df_node generated")
    
        logger.info("Generating df_pipe...")
        _non_result_props=self.GetPropertiesofElementType(self.ObjectTypes.Pipe)
        _result_props=self.GetResultProperties_from_elementType(self.ObjectTypes.Pipe, onlySelectedVectors=True)
        self.data_frames.df_pipe = self.generate_element_dataframe(non_result_props=_non_result_props, result_props=_result_props, element_type=self.ObjectTypes.Pipe)
        logger.info("df_pipe generated")

        logger.info("Dataframes generated.")
    
    def generate_element_dataframe(self, element_type, properties=None, timestamps=None):
        """
        Generate a dataframe for a given element type, including specified properties across timestamps.

        Parameters
        ----------
        element_type : Enum or str
            The element type to generate the dataframe for (e.g., self.ObjectTypes.Node).
        properties : list[str], optional
            List of property names to include. Will be internally sorted into result and non-result properties.
        timestamps : list[str], optional
            List of timestamps to include. Defaults to all simulations timestamps(self.GetTimeStamps()[0]) (if not available STAT timestamp(self.GetTimeStamps()[3])).

        Returns
        -------
        pd.DataFrame
            A dataframe containing the requested properties for the specified element type across timestamps.
        """

        logger.info(f"Generating dataframe for element type: {element_type}")

        # --- Default timestamp ---
        if timestamps is None:
            logger.info("No timestamps were given. Checking available simulation timestamps (SIR3S_Model.GetTimeStamps()).")
            try:
                simulation_timestamps, tsStat, tsMin, tsMax = self.GetTimeStamps() # tsMin and tsMax are retrived but not used, as there is no use for them this time of development
                if simulation_timestamps:
                    timestamps = simulation_timestamps
                    logger.info(f"{len(timestamps)} simulation timestamps will be used.")
                elif tsStat:
                    timestamps = [tsStat]
                    logger.info(f"No simulation timestamps found. Using stationary timestamp (STAT): {tsStat}")
                else:
                    logger.warning("No valid timestamps found. Dataframe will be empty.")
                    return pd.DataFrame()
            except Exception as e:
                logger.error(f"Error retrieving timestamps: {e}")
                return pd.DataFrame()


        # --- Check validity of given timestamps ---
        try:
            all_timestamps, tsStat, tsMin, tsMax = self.GetTimeStamps()
            available_timestamps = all_timestamps.copy()

            if tsStat and tsStat not in available_timestamps:
                available_timestamps.append(tsStat)

            valid_timestamps = []
            for timestamp in timestamps:
                if timestamp in available_timestamps:
                    valid_timestamps.append(timestamp)
                else:
                    logger.warning(
                        f"Dataframe is created without timestamp {timestamp} "
                        f"as it is not a valid timestamp (SIR3S_Model.GetTimeStamps())."
                    )
            timestamps = valid_timestamps
            logger.info(f"{len(timestamps)} valid timestamps will be used.")
        except Exception as e:
            logger.error(f"Error validating timestamps: {e}")
            return pd.DataFrame()

        # --- Initialize dataframe with tks ---
        try:
            tks = self.GetTksofElementType(ElementType=element_type)
            logger.info(f"Retrieved {len(tks)} tks.")
        except Exception as e:
            logger.error(f"Error retrieving tks: {e}")
            return pd.DataFrame()

        # --- Sort properties into non-result and result ---
        try:
            available_non_result_props = self.GetPropertiesofElementType(ElementType=element_type)
            available_result_props = self.GetResultProperties_from_elementType(
                elementType=element_type,
                onlySelectedVectors=False
            )

            non_result_props = []
            result_props = []

            if properties:
                for prop in properties:
                    if prop in available_non_result_props:
                        non_result_props.append(prop)
                    elif prop in available_result_props:
                        result_props.append(prop)
                    else:
                        logger.warning(
                            f"Property '{prop}' not found in either non-result (SIR3S_Model.GetPropertiesofElementType({element_type})) or result properties (SIR3S_Model.GetResultProperties_from_elementType({element_type}, onlySelectedVectors=False)) "
                            f"of element type {element_type}. It will be excluded."
                        )
            else:
                logger.info(f"No properties were given therefore dataframe is created with all available for properties for element type {element_type} (SIR3S_Model.GetPropertiesofElementType({element_type})+(SIR3S_Model.GetResultProperties_from_elementType({element_type}, onlySelectedVectors=False)).")
                non_result_props = available_non_result_props
                result_props = available_result_props

            logger.info(f"{len(non_result_props)} non-result properties and {len(result_props)} result properties will be used.")
        except Exception as e:
            logger.error(f"Error sorting properties: {e}")
            return pd.DataFrame()
        
        # --- Retrieve non-result properties ---
        logger.info("Retrieving non-result properties...")
        non_result_data = {}
        try:
            for tk in tks:
                row_data = {}
                for prop in non_result_props:
                    try:
                        row_data[prop] = self.GetValue(Tk=tk, propertyName=prop)[0]
                    except Exception as e:
                        logger.warning(f"Failed to get non-result property '{prop}' for tk '{tk}': {e}")
                non_result_data[tk] = row_data
            logger.info("Non-result properties retrieved successfully.")
        except Exception as e:
            logger.error(f"Error during non-result property precomputation: {e}")
        
        # --- Retrieve result properties ---
        data = []
        logger.info("Retrieving result properties...")
        
        for timestamp in map(str, timestamps):
            for tk in tks:
                row = {"timestamp": timestamp, "tk": tk}

                # Add precomputed non-result properties
                row.update(non_result_data.get(tk, {}))

                # Result properties
                try:
                    for prop in result_props:
                        row[prop] = self.GetResultfortimestamp(timestamp=timestamp, Tk=tk, property=prop)[0]
                except Exception as e:
                    logger.error(f"Error retrieving result properties for tk {tk} at timestamp {timestamp}: {e}")

                data.append(row)
        logger.info("Result properties retrieved successfully.")

        df = pd.DataFrame(data)
        logger.info(f"Dataframe generation for element type {element_type} completed.")
        return df


    def __is_a_model_open(self):
        """
        Returns true if a model is open, false if no model is open or the NetworkType is undefined.
        """
        is_a_model_open = True
        if(self.GetNetworkType=="NetworkType.Undefined"):
            is_a_model_open = False
        return is_a_model_open