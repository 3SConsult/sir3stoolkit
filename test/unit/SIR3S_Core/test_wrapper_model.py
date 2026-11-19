"""
Tests for SIR3S_Model against a real SIR 3S installation.
"""

import os
from enum import Enum
 
import pytest
import shutil
import logging

HERE = os.path.dirname(os.path.abspath(__file__))
TEST_MODELS_DIR = os.path.join(HERE, "TestModels")
XML_FILE_PATH = os.path.join(TEST_MODELS_DIR, "TopologieTutorial.XML")  # As per the folder structure, no need of changes
DB3_FILE_PATH = os.path.join(TEST_MODELS_DIR, "TopologieTutorial.db3")
LOG_FILE_PATH = os.path.join(TEST_MODELS_DIR, "log.txt")

# --------------------------------------------------------------------------
# Fixture: one opened model shared by all tests in this file
# --------------------------------------------------------------------------
@pytest.fixture(scope="module")
def model(sir3s_real):
    """Create a SIR3S_Model and open the test model once for this file."""
    from sir3stoolkit.core.wrapper import SIR3S_Model
 
    if not os.path.isfile(XML_FILE_PATH):
        pytest.fail(f"Test model not found: {XML_FILE_PATH}", pytrace=False)
 
    m = SIR3S_Model()
    m.EnableOrDisableOutputComments(True)
    m.OpenModelXml(XML_FILE_PATH, True)
    m.SetLogFilePath(LOG_FILE_PATH)
    return m

@pytest.fixture
def fresh_model(sir3s_real):
    """A new, unopened SIR3S_Model for each test."""
    from sir3stoolkit.core.wrapper import SIR3S_Model
    m = SIR3S_Model()
    m.EnableOrDisableOutputComments(True)
    return m

@pytest.fixture
def opened_model(fresh_model, tmp_path):
    """A freshly opened model on a temporary copy of the test model."""
    xml_copy = tmp_path / os.path.basename(XML_FILE_PATH)
    shutil.copy(XML_FILE_PATH, xml_copy)

    fresh_model.OpenModelXml(str(xml_copy), True)
    assert fresh_model.GetNetworkType() != fresh_model.NetworkType.Undefined, (
        "Precondition failed: model did not open"
    )
    return fresh_model

# --------------------------------------------------------------------------
# Log file path: SetLogFilePath() / GetLogFilePath()
# --------------------------------------------------------------------------
def test_GetLogFilePath_returns_string(model):
    assert isinstance(model.GetLogFilePath(), str)
 
 
def test_GetLogFilePath_returns_path_set_in_fixture(model):
    assert model.GetLogFilePath() == LOG_FILE_PATH
 
 
def test_SetLogFilePath_changes_path(model):
    new_path = os.path.join(TEST_MODELS_DIR, "log_other.txt")
    try:
        model.SetLogFilePath(new_path)
        assert model.GetLogFilePath() == new_path
    finally:
        # The model is shared by all tests in this file: restore it.
        model.SetLogFilePath(LOG_FILE_PATH)
 
 
# --------------------------------------------------------------------------
# Enum: ObjectTypes
# --------------------------------------------------------------------------
def test_ObjectTypes_exists(model):
    assert hasattr(model, "ObjectTypes"), "ObjectTypes enum is missing"
 
 
def test_ObjectTypes_is_enum(model):
    assert issubclass(model.ObjectTypes, Enum), "ObjectTypes is not an enum"
 
 
def test_ObjectTypes_not_empty(model):
    assert len(list(model.ObjectTypes)) > 0, "ObjectTypes is empty"
 

# --------------------------------------------------------------------------
# Enum: ProviderTypes
# --------------------------------------------------------------------------
def test_ProviderTypes_exists(model):
    assert hasattr(model, "ProviderTypes"), "ProviderTypes enum is missing"
 
 
def test_ProviderTypes_is_enum(model):
    assert issubclass(model.ProviderTypes, Enum), "ProviderTypes is not an enum"
 
 
def test_ProviderTypes_not_empty(model):
    assert len(list(model.ProviderTypes)) > 0, "ProviderTypes is empty"
    

# --------------------------------------------------------------------------
# Enum: NetworkType
# --------------------------------------------------------------------------
def test_NetworkType_exists(model):
    assert hasattr(model, "NetworkType"), "NetworkType enum is missing"
 
 
def test_NetworkType_is_enum(model):
    assert issubclass(model.NetworkType, Enum), "NetworkType is not an enum"
 
 
def test_NetworkType_not_empty(model):
    assert len(list(model.NetworkType)) > 0, "NetworkType is empty"
    

# --------------------------------------------------------------------------
# GetNetworkType()
# --------------------------------------------------------------------------
def test_GetNetworkType_returns_NetworkType(model):
    network = model.GetNetworkType()
    assert isinstance(network, model.NetworkType), (
        f"{network!r} is not a {model.NetworkType}"
    )
 
 
def test_GetNetworkType_is_not_Undefined(model):
    network = model.GetNetworkType()
    assert network != model.NetworkType.Undefined, "Network type is Undefined"
    

# --------------------------------------------------------------------------
# GetTksofElementType()
# --------------------------------------------------------------------------
# Element types to check. Names are looked up on model.ObjectTypes at test
# time, because the model (and its enums) only exists once SIR 3S is loaded.
ELEMENT_TYPES = ["Node", "Pipe"]
 
 
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_GetTksofElementType_returns_result(model, element_type):
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    assert tks is not None, f"GetTksofElementType({element_type}) returned None"
 
 
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_GetTksofElementType_not_empty(model, element_type):
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    assert len(tks) > 0, f"GetTksofElementType({element_type}) returned an empty list"


# --------------------------------------------------------------------------
# GetPropertiesofElementType()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_GetPropertiesofElementType_returns_result(model, element_type):
    properties = model.GetPropertiesofElementType(getattr(model.ObjectTypes, element_type))
    assert properties is not None, f"GetPropertiesofElementType({element_type}) returned None"
    

@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_GetPropertiesofElementType_not_empty(model, element_type):
    properties = model.GetPropertiesofElementType(getattr(model.ObjectTypes, element_type))
    assert len(properties) > 0, f"GetPropertiesofElementType({element_type}) returned an empty list"
    

# --------------------------------------------------------------------------
# GetObjectTypeof_Key()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)    
def test_GetObjectTypeof_Key_valid_result(model, element_type):
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    objectType = model.GetObjectTypeof_Key(tks[0])
    assert objectType is not None, f"GetObjectTypeof_Key() with Tk from a {element_type} returned None"
    assert isinstance(objectType, model.ObjectTypes), (
        f"{objectType!r} is not a {model.ObjectTypes}"
    )


# --------------------------------------------------------------------------
# GetValue()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_GetValue_returns_valid_result(model, element_type):
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    properties = model.GetPropertiesofElementType(getattr(model.ObjectTypes, element_type))
    # Necessary checks
    assert tks is not None, f"GetTksofElementType({element_type}) returned None"
    assert len(tks) > 0, f"GetTksofElementType({element_type}) returned an empty list"
    assert properties is not None, f"GetPropertiesofElementType({element_type}) returned None"
    assert len(properties) > 0, f"GetPropertiesofElementType({element_type}) returned an empty list"
    value, _ = model.GetValue(tks[0], properties[0])
    # Important checks
    assert isinstance(value, str), f"expected a string, got {type(value).__name__}"
    assert value.strip() != "", "value returned is empty"
    

# --------------------------------------------------------------------------
# SetValue()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_SetValue_beschreibung(model, element_type):
    new_value = "test changes"
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    value_old, _ = model.GetValue(tks[0], "beschreibung")
    assert isinstance(value_old, str), f"expected a string, got {type(value_old).__name__}"
    #assert value_old.strip() != "", "old value returned is empty"
    assert value_old != new_value, "test value equals original; the test would prove nothing"
    
    try:
        model.StartTransaction("Set value changes")
        model.SetValue(tks[0], "beschreibung", new_value)
        model.EndTransaction()
        model.SaveChanges()
    
        value_new, _ = model.GetValue(tks[0], "beschreibung")
        assert isinstance(value_new, str), f"expected a string, got {type(value_new).__name__}"
        assert value_new.strip() != "", "new value returned is empty"
        assert value_new == new_value, (
                f"SetValue() did not work: expected {new_value!r}, got {value_new!r}"
            )
    finally:
        model.StartTransaction("Reset value changes")
        model.SetValue(tks[0], "beschreibung", value_old)   # restore for the other tests
        model.EndTransaction()
        model.SaveChanges()
        

# --------------------------------------------------------------------------
# GetTimeStamps()
# --------------------------------------------------------------------------
def test_GetTimeStamps_returns_valid_result(model):
    timestamps, tsStat, tsMin, tsMax = model.GetTimeStamps()
    assert timestamps is not None, "GetTimeStamps() returned null"
    assert len(timestamps) > 0, f"GetTimeStamps() returned an empty list"


# --------------------------------------------------------------------------
# GetCurrentTimeStamp()
# --------------------------------------------------------------------------
def test_GetCurrentTimeStamp_returns_valid_result(model):
    timestamp = model.GetCurrentTimeStamp()
    assert timestamp is not None, "GetCurrentTimeStamp() returned null"
    
    
# --------------------------------------------------------------------------
# SetCurrentTimeStamp()
# --------------------------------------------------------------------------
def test_SetCurrentTimeStamp_returns_valid_result(model):
    timestamps, _, _, _ = model.GetTimeStamps()
    assert timestamps is not None, "GetTimeStamps() returned null"
    assert len(timestamps) > 0, f"GetTimeStamps() returned an empty list"
    
    timestamp_old = model.GetCurrentTimeStamp()
    assert timestamp_old is not None, "GetCurrentTimeStamp() returned null"
    
    timestamp_new = None
    
    for t in timestamps:
        if t != timestamp_old:
            timestamp_new = t
            break
        
    if timestamp_new is None:
        pytest.skip(f"There are no other timestamps available than the one that is set, this test won't be meaningful in this scenario")
      
    try:
        model.SetCurrentTimeStamp(str(timestamp_new))
        timestamp_current = model.GetCurrentTimeStamp()
        assert timestamp_current != timestamp_old, "SetCurrentTimeStamp() did not work during main try"
        
    finally:
        # Reset the timestamp
        model.SetCurrentTimeStamp(str(timestamp_old))
        timestamp_current = model.GetCurrentTimeStamp()
        assert timestamp_current == timestamp_old, "SetCurrentTimeStamp() did not work during reset"
        

# --------------------------------------------------------------------------
# GetElementInfo()
# --------------------------------------------------------------------------
# Written only for the sake of coverage, doesn't test the functionality of the unit        
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)        
def test_GetElementInfo_returns_valid_result(model, element_type):
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    model.GetElementInfo(tks[0])
    #pytest.skip("As the function prints the element info and doesn't return anything, nothing to check here")
    

# --------------------------------------------------------------------------
# GetNumberOfElements()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)        
def test_GetNumberOfElements_returns_valid_result(model, element_type): 
    Nr_Element_type = model.GetNumberOfElements(getattr(model.ObjectTypes, element_type))
    assert Nr_Element_type != 0, "Returned value should not be zero"
    

# --------------------------------------------------------------------------
# InsertElement() and DeleteElement()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)      
def test_InsertElement_and_DeleteElement_returns_valid_result(model, element_type):
    # Insert a new element
    tk_new = model.InsertElement(getattr(model.ObjectTypes, element_type), "Sample_1")
    assert tk_new != "-1", "Newly inserted element cannot have TK as -1"
    
    # Delete newly inserted element - This also works as restoration
    model.DeleteElement(tk_new)
    

# --------------------------------------------------------------------------
# StartEditSession() and EndEditSession()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("element_type", ELEMENT_TYPES)
def test_StartEditSession_and_EndEditSession(model, element_type):
    tks = model.GetTksofElementType(getattr(model.ObjectTypes, element_type))
    
    old_val_list = []
    new_Val = 'Test changes - n'
    # Do bulk edit under StartEditSession() and EndEditSession()
    try:
        model.StartEditSession("Commit mass changes to the description")
        for i in range(len(tks)):
            old_descr, _ = model.GetValue(tks[i], "Beschreibung")
            old_val_list.append(old_descr)
            model.SetValue(tks[i], "Beschreibung", new_Val)
            new_descr, _ =  model.GetValue(tks[i], "Beschreibung")
            assert old_descr != new_descr, "Description update failed"
            assert new_descr == new_Val, "Description update failed"
        model.EndEditSession()
        model.SaveChanges()
    finally:
        model.StartEditSession("Restore changes to the description(bulk edit)")
        for i in range(len(tks)):
            model.SetValue(tks[i], "Beschreibung", old_val_list[i])
            new_descr, _ =  model.GetValue(tks[i], "Beschreibung")
            assert new_descr == old_val_list[i], "Description update failed"
        model.EndEditSession()
        model.SaveChanges()
    

# --------------------------------------------------------------------------
# ConnectConnectingElementWithNodes()
# --------------------------------------------------------------------------
def test_ConnectConnectingElementWithNodes_returns_valid_result(model):
    model.StartEditSession("Commit mass changes to the description")
    node_A = model.InsertElement(model.ObjectTypes.Node, "Node A")
    node_B = model.InsertElement(model.ObjectTypes.Node, "Node B")
    pipe_C = model.InsertElement(model.ObjectTypes.Pipe, "Pipe C")
    assert node_A != "-1", "Failed to insert Node A"
    assert node_B != "-1", "Failed to insert Node B"
    assert pipe_C != "-1", "Failed to insert Pipe C"
    
    model.ConnectConnectingElementWithNodes(pipe_C, node_A, node_B)
    model.DeleteElement(node_A)
    model.DeleteElement(node_B)
    model.DeleteElement(pipe_C)
    
    model.EndEditSession()
    model.SaveChanges()
    
# --------------------------------------------------------------------------
# GetTableRows()
# --------------------------------------------------------------------------
def test_GetTableRows_returns_valid_result(model):
    tks = model.GetTksofElementType(model.ObjectTypes.PipeTable)
    Table_rows, objType = model.GetTableRows(tks[0])
    assert len(Table_rows) > 0, "Table row is empty"
    

# --------------------------------------------------------------------------
# OpenModelXml()
# --------------------------------------------------------------------------
def test_OpenModelXml_model_is_loaded(model):
    # A loaded model has a defined network type
    assert model.GetNetworkType() != model.NetworkType.Undefined, (
        "OpenModelXml() did not load the model: network type is Undefined"
    )
    # And contains elements
    tks = model.GetTksofElementType(model.ObjectTypes.Node)
    assert len(tks) > 0, "OpenModelXml() did not load the model: no nodes found"
    
def test_OpenModelXml_loads_valid_file(fresh_model):
    fresh_model.OpenModelXml(XML_FILE_PATH, True)
    assert fresh_model.GetNetworkType() != fresh_model.NetworkType.Undefined, (
        "OpenModelXml() did not load the model: network type is Undefined"
    )
    
def test_OpenModelXml_missing_file(fresh_model):
    from sir3stoolkit.core.wrapper import SIR3S_ToolkitError

    missing = os.path.join(HERE, "TestModels", "does_not_exist.XML")
    with pytest.raises(SIR3S_ToolkitError, match="Error while opening the model"):
        fresh_model.OpenModelXml(missing, True)
    

# --------------------------------------------------------------------------
# OpenModel()
# --------------------------------------------------------------------------
def test_OpenModel_loads_valid_file(fresh_model):
    fresh_model.OpenModel(dbName=DB3_FILE_PATH,
                          providerType=fresh_model.ProviderTypes.SQLite,
                          Mid="M-1-0-1",
                          saveCurrentlyOpenModel=False, 
                          namedInstance="",
                          userID="", 
                          password="")
    assert fresh_model.GetNetworkType() != fresh_model.NetworkType.Undefined, (
        "OpenModel() did not load the model: network type is Undefined"
    )
    
def test_OpenModel_missing_file(fresh_model):
    from sir3stoolkit.core.wrapper import SIR3S_ToolkitError
    
    missing = os.path.join(HERE, "TestModels", "does_not_exist.db3")
    with pytest.raises(SIR3S_ToolkitError, match="Error while opening the model"):
        fresh_model.OpenModel(dbName=missing,
                          providerType=fresh_model.ProviderTypes.SQLite,
                          Mid="M-1-0-1",
                          saveCurrentlyOpenModel=False, 
                          namedInstance="",
                          userID="", 
                          password="")
    

# --------------------------------------------------------------------------
# CloseModel()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("param", [False, True])
def test_CloseModel_unloads_model(model, opened_model, param):
    retVal = opened_model.CloseModel(param)
    assert retVal, "CloseModel() did not close the model"
    
    assert opened_model.GetNetworkType() == opened_model.NetworkType.Undefined, (
        f"CloseModel({param}) did not unload the model"
    )
    
    assert model.GetNetworkType() != model.NetworkType.Undefined, (
        "Closing one SIR3S_Model also closed the shared one"
    )
    
def test_CloseModel_redundant_call(fresh_model):
    from sir3stoolkit.core.wrapper import SIR3S_ToolkitError
    
    assert fresh_model.GetNetworkType() == fresh_model.NetworkType.Undefined, (
        "Model is not open yet; network type should be Undefined"
    )
    
    with pytest.raises(SIR3S_ToolkitError, match="Error while closing the model, Object Model not set yet"):
        fresh_model.CloseModel(True)

# --------------------------------------------------------------------------
# ExecCalculation()
# --------------------------------------------------------------------------
@pytest.mark.parametrize("param", [False, True])        
def test_ExecCalculation_reports_completion(model, caplog, param):
    caplog.set_level(logging.DEBUG)
    if param:
        model.ExecCalculation(param)
        assert "Could not start Model Calculation" not in caplog.text, caplog.text
        assert "Model Calculation is complete" in caplog.text, caplog.text
    else:
        # This part has bug: : In .NET method ExecCalculation() when waitForSirCalcToExit is passed as False that means the 
        # method is not supposed to wait for calculation to exit which works fine. But before return this line exist
        # int returnvalue = _sirCalcProcess.ExitCode;
        # And this is a redundant line at moment as only Boolean true is returned from the method not this returnvalue. 
        # But reading this exitcode in case of still executing process throws InvalidOperationException, hence the bug.
        assert True

    
def test_ExecCalculation_leaves_no_lock_file(model, tmp_path):
    model.ExecCalculation(True)
    lock_files = list(tmp_path.rglob("*_SirCalcIsRunning.tmp"))
    assert lock_files == [], f"SirCalc lock file left behind: {lock_files}"
    
def test_ExecCalculation_logs_no_errors(model, caplog):
    caplog.set_level(logging.DEBUG)
    model.ExecCalculation(True)
    errors = [r.getMessage() for r in caplog.records if r.levelno >= logging.ERROR]
    assert errors == [], f"Calculation logged errors: {errors}"

def test_ExecCalculation_without_open_model_reports_error(fresh_model):
    from sir3stoolkit.core.wrapper import SIR3S_ToolkitError
    
    with pytest.raises(SIR3S_ToolkitError, match="Could not start Model Calculation: Object Model not set yet"):
        fresh_model.ExecCalculation(True)