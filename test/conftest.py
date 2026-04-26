from pathlib import Path
import sys

import pytest

# Allow running tests directly from repository root without installing the package.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from sir3stoolkit.core import wrapper
from sir3stoolkit.mantle.advanced_operations import SIR3S_Model_Advanced_Operations
from sir3stoolkit.mantle.alternative_models import SIR3S_Model_Alternative_Models
from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
from sir3stoolkit.mantle.mantle import SIR3S_Model_Mantle
from sir3stoolkit.mantle.plotting import SIR3S_Model_Plotting

def _create_class_instance_without_init(cls):
    """Build instances of cls without calling native-heavy __init__."""
    instance = cls.__new__(cls)
    instance.outputComments = True
    return instance

@pytest.fixture
def initialized_wrapper(monkeypatch, tmp_path):
    """Initialize wrapper state without loading real native assemblies."""
    resolved_dir = tmp_path / "sirgraf"
    resolved_dir.mkdir()

    add_reference_calls = []
    original_sys_path = list(wrapper.sys.path)
    original_sirgraf_dir = wrapper.SIR3S_SIRGRAF_DIR

    monkeypatch.setattr(wrapper, "_resolve_base_path", lambda _: str(resolved_dir))
    monkeypatch.setattr(wrapper.net, "AddReference", add_reference_calls.append)

    wrapper.Initialize_Toolkit(None)

    yield {
        "resolved_dir": resolved_dir,
        "add_reference_calls": add_reference_calls,
    }

    wrapper.sys.path[:] = original_sys_path
    wrapper.SIR3S_SIRGRAF_DIR = original_sirgraf_dir


@pytest.fixture
def s3s_model_instance(initialized_wrapper):
    return _create_class_instance_without_init(wrapper.SIR3S_Model)


@pytest.fixture
def s3s_view_instance(initialized_wrapper):
    return _create_class_instance_without_init(wrapper.SIR3S_View)


@pytest.fixture
def s3s_model_repair_instance(initialized_wrapper):
    return _create_class_instance_without_init(wrapper.SIR3S_ModelRepair)


@pytest.fixture
def s3s_model_dataframes_instance(initialized_wrapper):
    return _create_class_instance_without_init(SIR3S_Model_Dataframes)


@pytest.fixture
def s3s_model_alternative_models_instance(initialized_wrapper):
    return _create_class_instance_without_init(SIR3S_Model_Alternative_Models)


@pytest.fixture
def s3s_model_plotting_instance(initialized_wrapper):
    return _create_class_instance_without_init(SIR3S_Model_Plotting)


@pytest.fixture
def s3s_model_advanced_operations_instance(initialized_wrapper):
    return _create_class_instance_without_init(SIR3S_Model_Advanced_Operations)


@pytest.fixture
def s3s_model_mantle_instance(initialized_wrapper):
    return _create_class_instance_without_init(SIR3S_Model_Mantle)


@pytest.fixture
def s3s(s3s_model_instance):
    """Backward-compatible alias used by existing tests."""
    return s3s_model_instance

"""
@pytest.fixture
def opened_model(s3s):
    Provide a model instance where OpenModel has already succeeded.

    class FakeToolkit:
        def __init__(self):
            self.open_model_calls = []
            self.start_transaction_calls = []
            self.end_transaction_calls = 0
            self.is_model_open = False
            self.in_transaction = False

        def OpenModel(self, dbName, providerType, Mid, saveCurrentlyOpenModel, namedInstance, userID, password):
            self.open_model_calls.append(
                (dbName, providerType, Mid, saveCurrentlyOpenModel, namedInstance, userID, password)
            )
            self.is_model_open = True
            return True, ""

        def StartTransaction(self, session_name):
            self.start_transaction_calls.append(session_name)
            if not self.is_model_open:
                return False, "No model open"
            self.in_transaction = True
            return True, ""

        def EndTransaction(self):
            self.end_transaction_calls += 1
            if not self.in_transaction:
                return False, "No open transaction"
            self.in_transaction = False
            return True, ""

    toolkit = FakeToolkit()
    s3s.toolkit = toolkit
    s3s.to_dotnet_enum = lambda provider_type: f"dotnet:{provider_type}"

    params = {
        "db_name": "C:/tmp/model.db3",
        "provider_type": "SQLITE",
        "mid": "M-1-0-1",
        "save_currently_open_model": False,
        "named_instance": "",
        "user_id": "",
        "password": "",
    }

    s3s.OpenModel(
        params["db_name"],
        params["provider_type"],
        params["mid"],
        params["save_currently_open_model"],
        params["named_instance"],
        params["user_id"],
        params["password"],
    )

    return {
        "model": s3s,
        "model class instance": s3s,
        "toolkit": toolkit,
        "params": params,
    }

@pytest.fixture
def s3s(initialized_wrapper):
        Create SIR3S_Model instance without executing __init__ native imports.
    model = wrapper.SIR3S_Model.__new__(wrapper.SIR3S_Model)
    model.outputComments = True
    return model
"""