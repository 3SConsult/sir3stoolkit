# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 09:22:31 2025

@author: Jablonski
"""

from sir3stoolkit.core.wrapper import SIR3S_Model

import pandas as pd
import sys
import logging

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)
logger.info("Logging is configured.")

class PT3S_SIR3S_Model(SIR3S_Model):

    class Dx():
        """
        """
        """
        TODO:
            - data_frames
        """

    class Mx():
        """
        """
        """
        TODO:
            - result values
        """

    class DxWithMx():
    
        def __init__(self,dx,mx):
            """
            :param dx: a Dx object
            :type dx: Dx()
            :param mx: a Mx object
            :type mx: Mx()
            """
            """
            TODO 
            - Create V3_dfs:
                - V3_ROHR
                - V3_FWVB
                - V3_KNOT
                - V3_VBEL
                - V3_ROHRVEC
                - V3_AGSN
                - V3_AGSNVEC
            - gdfs: if possitble just inlcude geometry in dfs above
                - gdf_ROHR
                - gdf_FWVB
                - gdf_KNOT
            - Create Graphs:
                - G
                - GSig

            
            """

    def read_dx_mx(self):
        """
        Member function of PT3S_SIR3S_Model() class, can only be used while a model is open.
        """    
        if not self.__is_a_model_open():
                    logger.error("Attempted to read dx/mx while no model is open or network type is undefined.")
                    raise RuntimeError("Model must be open to read dx/mx and network type must be defined.")



    def __is_a_model_open(self):
        """
        Returns true if a model is open, false if no model is open or the NetworkType is undefined.
        """
        is_a_model_open = True
        if(self.GetNetworkType=="NetworkType.Undefined"):
            is_a_model_open = False
        return is_a_model_open