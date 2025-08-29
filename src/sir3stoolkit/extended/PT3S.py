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

    class dxWithMx():
    
        def __init__(self,dx,mx,crs=None):
            """
            :param dx: a Dx object
            :type dx: Dx.Dx()
            :param mx: a Mx object
            :type mx: Mx.Mx()
            """
            


    def readDxAndMx()