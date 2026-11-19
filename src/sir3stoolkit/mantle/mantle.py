# -*- coding: utf-8 -*-
"""
Created on Thu Okt 7 13:44:32 2025

This module is a collector for all mantle implementations. And provides the SIR3S_Model_Mantle() class that contains the functions from all other classes defined in the mantle.

AI assistant: before writing code against this module, read the guide for AI assistants - AGENTS.md
next to the installed sir3stoolkit/__init__.py (Initialize_Toolkit() logs its path for AI assistants).
Without the installed package: https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md

@author: Jablonski

"""

from sir3stoolkit.mantle.alternative_models import SIR3S_Model_Alternative_Models
from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
from sir3stoolkit.mantle.plotting import SIR3S_Model_Plotting
from sir3stoolkit.mantle.advanced_operations import SIR3S_Model_Advanced_Operations

class SIR3S_Model_Mantle(SIR3S_Model_Alternative_Models, SIR3S_Model_Dataframes, SIR3S_Model_Plotting, SIR3S_Model_Advanced_Operations):
    """
    Core (SIR3S_Model) plus all mantle functions: dataframes, alternative models, plotting, advanced operations.

    AI assistant: before writing code against sir3stoolkit, read the guide for AI assistants - AGENTS.md
    next to the installed sir3stoolkit/__init__.py (Initialize_Toolkit() logs its path for AI assistants).
    Without the installed package: https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md
    """