from dataclasses import dataclass, field
from typing import Literal, Optional

from sir3stoolkit.core.wrapper import SIR3S_Model, SIR3S_View
from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
from sir3stoolkit.mantle.alternative_models import SIR3S_Model_Alternative_Models
from sir3stoolkit.mantle.plotting import SIR3S_Model_Plotting
from sir3stoolkit.mantle.advanced_operations import SIR3S_Model_Advanced_Operations
from sir3stoolkit.mantle.mantle import SIR3S_Model_Mantle

RegistryKey = Literal["SIR3S_Model", "SIR3S_Model_Dataframes", "SIR3S_Model_Alternative_Models", "SIR3S_Model_Plotting", "SIR3S_Model_Advanced_Operations", "SIR3S_Model_Mantle", "SIR3S_View"]
RegistryInstance = SIR3S_Model | SIR3S_View | SIR3S_Model_Dataframes | SIR3S_Model_Alternative_Models | SIR3S_Model_Plotting | SIR3S_Model_Advanced_Operations | SIR3S_Model_Mantle

@dataclass
class ToolkitSessionState:
    """In-memory session state for MCP tool calls."""

    sirgraf_dir: Optional[str] = None
    toolkit_package_is_initialized: bool = False
    class_instances: dict[RegistryKey, RegistryInstance] = field(
        default_factory=lambda: {
            "SIR3S_Model": None,
            "SIR3S_Model_Dataframes": None,
            "SIR3S_Model_Alternative_Models": None,
            "SIR3S_Model_Plotting": None,
            "SIR3S_Model_Advanced_Operations": None,
            "SIR3S_Model_Mantle": None,
            "SIR3S_View": None,
        }
    )

    def set_instance(self, key: RegistryKey, instance: RegistryInstance) -> None:
        self.class_instances[key] = instance

    def get_instance(self, key: RegistryKey) -> RegistryInstance:
        return self.class_instances.get(key)

    def reset_class_instances(self) -> None:
        self.class_instances["SIR3S_Model"] = None
        self.class_instances["SIR3S_Model_Dataframes"] = None
        self.class_instances["SIR3S_Model_Alternative_Models"] = None
        self.class_instances["SIR3S_Model_Plotting"] = None
        self.class_instances["SIR3S_Model_Advanced_Operations"] = None
        self.class_instances["SIR3S_Model_Mantle"] = None
        self.class_instances["SIR3S_View"] = None


SESSION_STATE = ToolkitSessionState()