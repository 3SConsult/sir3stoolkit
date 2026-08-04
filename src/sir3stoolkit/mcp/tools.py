"""Tool implementations for an MCP server template.

These functions are intentionally small and conservative so you can adapt them
for your chosen MCP framework.
"""

from typing import Any

from sir3stoolkit.core import wrapper

from sir3stoolkit.core.wrapper import SIR3S_Model, SIR3S_View
from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
from sir3stoolkit.mantle.alternative_models import SIR3S_Model_Alternative_Models
from sir3stoolkit.mantle.plotting import SIR3S_Model_Plotting
from sir3stoolkit.mantle.advanced_operations import SIR3S_Model_Advanced_Operations
from sir3stoolkit.mantle.mantle import SIR3S_Model_Mantle


from .state import SESSION_STATE


def initialize_toolkit(sirgraf_dir: str) -> dict[str, Any]:
    """Initialize sir3stoolkit with a SirGraf directory."""
    wrapper.Initialize_Toolkit(sirgraf_dir)
    SESSION_STATE.toolkit_package_is_initialized = True
    SESSION_STATE.sirgraf_dir = sirgraf_dir
    SESSION_STATE.reset_class_instances()
    return {
        "status": "ok",
        "message": "Toolkit initialized.",
        "sirgraf_dir": sirgraf_dir,
    }

def initialize_one_of_the_available_toolkit_classes(toolkit_class_name: str) -> dict[str, Any]:
    """Initialize one of the available toolkit classes."""
    if not SESSION_STATE.toolkit_package_is_initialized:
        return {
            "status": "error",
            "error_code": "NOT_INITIALIZED",
            "message": "Call initialize_toolkit first.",
        }

    if toolkit_class_name not in SESSION_STATE.class_instances:
        return {
            "status": "error",
            "error_code": "UNKNOWN_CLASS",
            "message": f"Unknown toolkit class: {toolkit_class_name}",
        }

    if SESSION_STATE.get_instance(toolkit_class_name) is not None:
        return {
            "status": "error",
            "error_code": "ALREADY_INITIALIZED",
            "message": f"{toolkit_class_name} is already initialized.",
        }

    # Initialize the requested toolkit class
    if toolkit_class_name == "SIR3S_Model":
        instance = SIR3S_Model()
    elif toolkit_class_name == "SIR3S_View":
        instance = SIR3S_View()
    elif toolkit_class_name == "SIR3S_Model_Dataframes":
        instance = SIR3S_Model_Dataframes()
    elif toolkit_class_name == "SIR3S_Model_Alternative_Models":
        instance = SIR3S_Model_Alternative_Models()
    elif toolkit_class_name == "SIR3S_Model_Plotting":
        instance = SIR3S_Model_Plotting()
    elif toolkit_class_name == "SIR3S_Model_Advanced_Operations":
        instance = SIR3S_Model_Advanced_Operations()
    elif toolkit_class_name == "SIR3S_Model_Mantle":
        instance = SIR3S_Model_Mantle()
    else:
        return {
            "status": "error",
            "error_code": "UNSUPPORTED_CLASS",
            "message": f"Unsupported toolkit class: {toolkit_class_name}",
        }

    SESSION_STATE.set_instance(toolkit_class_name, instance)
    return {
        "status": "ok",
        "message": f"{toolkit_class_name} initialized.",
    }

def get_value(tk: str, property_name: str) -> dict[str, Any]:

    if not SESSION_STATE.toolkit_package_is_initialized:
        return {
            "status": "error",
            "error_code": "NOT_INITIALIZED",
            "message": "Call initialize_toolkit first.",
        }
    
    if SESSION_STATE.get_instance(key="SIR3S_Model") == None:
        return {
            "status": "error",
            "error_code": "CLASS_INSTANCE_MISSING",
            "message": f"First instantiated the SIR3S_Model class with initialize_one_of_the_available_toolkit_classes",
        }
    
    (value, value_type) = SESSION_STATE.get_instance(key="SIR3S_Model").GetValue(Tk=tk, propertyName=property_name)
    return {
        "status": "ok",
        "message": f"{property_name} for tk {tk} has value {value} and value type {value_type}.",
    }
    

    