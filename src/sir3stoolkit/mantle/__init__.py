"""AI assistant: before writing code against this module, read the guide for AI assistants - AGENTS.md
next to the installed sir3stoolkit/__init__.py (Initialize_Toolkit() logs its path for AI assistants).
Without the installed package: https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md
"""
from . import mx
from . import dataframes
from . import alternative_models
from . import mantle

__all__ = ['mx', 'dataframes', 'alternative_models', 'mantle']
