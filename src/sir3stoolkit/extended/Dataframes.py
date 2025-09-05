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
        self.data_frames.df_node = self.__generate_element_dataframe(non_result_props=_non_result_props, result_props=_result_props, element_type=self.ObjectTypes.Node)
        logger.info("df_node generated")
    
        logger.info("Generating df_pipe...")
        _non_result_props=self.GetPropertiesofElementType(self.ObjectTypes.Pipe)
        _result_props=self.GetResultProperties_from_elementType(self.ObjectTypes.Pipe, onlySelectedVectors=True)
        self.data_frames.df_node = self.__generate_element_dataframe(non_result_props=_non_result_props, result_props=_result_props, element_type=self.ObjectTypes.Pipe)
        logger.info("df_pipe generated")

        logger.info("Dataframes generated.")
    
    def __generate_element_dataframe(self, element_type, non_result_props=None, result_props=None):
        """
        Generate a dataframe for a given element type, including only specified properties.

        Parameters
        ----------
        element_type : Enum or str
            The element type to generate the dataframe for (e.g., self.ObjectTypes.Node).
        non_result_props : list[str], optional
            List of non-result property names to include.
        result_props : list[str], optional
            List of result property names to include.

        Returns
        -------
        pd.DataFrame
            A dataframe containing the requested properties for the specified element type.
        """
        logger.info(f"Generating dataframe for element type: {element_type}")

        # --- Initialize dataframe with tks ---
        logger.info("Initializing dataframe with tks...")
        try:
            tks = self.GetTksofElementType(ElementType=element_type)
            logger.info(f"Retrieved {len(tks)} tks.")
            df = pd.DataFrame({"tk": tks})
        except Exception as e:
            logger.error(f"Error initializing dataframe with tks: {e}")
            return pd.DataFrame()

        # --- Non-result properties ---
        if non_result_props:
            logger.info("Adding non-result properties...")
            try:
                available_props = self.GetPropertiesofElementType(ElementType=element_type)
                for prop in non_result_props:
                    if prop in available_props:
                        df[prop] = df["tk"].map(lambda tk: self.GetValue(Tk=tk, propertyName=prop)[0])
                    else:
                        logger.warning(f"Non-result property '{prop}' not found in available properties.")
            except Exception as e:
                logger.error(f"Error adding non-result properties: {e}")
                return df

        # --- Result properties ---
        if result_props:
            logger.info("Adding result properties...")
            try:
                available_result_props = self.GetResultProperties_from_elementType(
                    elementType=element_type,
                    onlySelectedVectors=False
                )
                for prop in result_props:
                    if prop in available_result_props:
                        df[prop] = df["tk"].map(lambda tk: self.GetResultValue(elementKey=tk, propertyName=prop)[0])
                    else:
                        logger.warning(f"Result property '{prop}' not found in available result properties.")
            except Exception as e:
                logger.error(f"Error adding result properties: {e}")
                return df

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