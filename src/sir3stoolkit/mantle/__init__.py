"""AI assistant: before writing code against this module, read the guide for AI assistants - AGENTS.md
next to the installed sir3stoolkit/__init__.py (Initialize_Toolkit() logs its path for AI assistants).
Without the installed package: https://raw.githubusercontent.com/3SConsult/sir3stoolkit/main/AGENTS.md

The submodules are loaded on first access, not with this package: importing one of them (e.g.
``from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes``) loads only that module and the
modules it imports itself, not the others and their third-party dependencies. A missing dependency
raises its ImportError in the module that needs it. ``from sir3stoolkit.mantle.mantle import
SIR3S_Model_Mantle`` loads all of them, as before.
"""
import importlib

__all__ = ['mx', 'dataframes', 'alternative_models', 'plotting', 'advanced_operations', 'mantle']


def __getattr__(name):
    # Only called for names not (yet) in the module namespace (PEP 562). import_module() also sets the
    # submodule as an attribute of this package, so each submodule goes through here once.
    if name in __all__:
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(set(globals()) | set(__all__))
