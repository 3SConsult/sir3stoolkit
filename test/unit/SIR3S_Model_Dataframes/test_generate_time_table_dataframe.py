import pandas as pd


class _DummyObjectTypesMap:
    VarPressureTable = "VarPressureTable"
    VarFlowTable = "VarFlowTable"
    ValveLiftTable = "ValveLiftTable"
    PumpSpeedTable = "PumpSpeedTable"
    MeasuredVariableTable = "MeasuredVariableTable"
    LoadFactorTable = "LoadFactorTable"
    ThermalOutputTable = "ThermalOutputTable"
    TemperatureTable = "TemperatureTable"

    def __getitem__(self, key):
        return key


def test_insert_dataframe_into_time_table_validates_and_writes_rows(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()

    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["2026-01-01 00:00:00.000000 +00:00"], "STAT", "MIN", "MAX")
    s3s_model_dataframes_instance._get_time_table_col_name_from_tk = lambda time_table_tk: ("W", "Sollwert")
    s3s_model_dataframes_instance.get_dataframe_from_time_table = lambda time_table_tk, value_col_name: pd.DataFrame(
        {"tk": [None], "WERT": [float("nan")]}, index=[float("nan")]
    )

    deleted = []
    s3s_model_dataframes_instance.DeleteElement = lambda tk: deleted.append(tk)

    created_rows = []

    def _add_table_row(tablePkTk):
        new_tk = f"ROW_NEW_{len(created_rows)}"
        created_rows.append(new_tk)
        return (new_tk,)

    s3s_model_dataframes_instance.AddTableRow = _add_table_row

    set_calls = []
    s3s_model_dataframes_instance.SetValue = lambda Tk, propertyName, Value: set_calls.append((Tk, propertyName, Value))

    df = pd.DataFrame(
        {
            "TAG": ["2026-01-01", "2026-01-01"],
            "UHRZEIT": ["00:00:00.000000", "00:00:10.000000"],
            "WERT": [1.5, 2.5],
        }
    )

    result = s3s_model_dataframes_instance.insert_dataframe_into_time_table(time_table_tk="TT1", dataframe=df)

    assert result is None
    assert deleted == []
    assert ("ROW_NEW_0", "Zeit", "0,000000") in set_calls
    assert ("ROW_NEW_1", "Zeit", "10,000000") in set_calls
    assert ("ROW_NEW_0", "W", "1.5") in set_calls
    assert ("ROW_NEW_1", "W", "2.5") in set_calls


def test_insert_dataframe_into_time_table_overwrite_true_replaces_existing_rows(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()

    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["2026-01-01 00:00:00.000000 +00:00"], "STAT", "MIN", "MAX")
    s3s_model_dataframes_instance._get_time_table_col_name_from_tk = lambda time_table_tk: ("W", "Sollwert")
    s3s_model_dataframes_instance.get_dataframe_from_time_table = lambda time_table_tk, value_col_name: pd.DataFrame(
        {"tk": ["ROW_OLD_1", "ROW_OLD_2"], "WERT": [1.0, 2.0]}, index=[0.0, 10.0]
    )

    deleted = []
    s3s_model_dataframes_instance.DeleteElement = lambda tk: deleted.append(tk)

    created_rows = []

    def _add_table_row(tablePkTk):
        new_tk = f"ROW_NEW_{len(created_rows)}"
        created_rows.append(new_tk)
        return (new_tk,)

    s3s_model_dataframes_instance.AddTableRow = _add_table_row

    set_calls = []
    s3s_model_dataframes_instance.SetValue = lambda Tk, propertyName, Value: set_calls.append((Tk, propertyName, Value))

    df = pd.DataFrame(
        {
            "TAG": ["2026-01-01", "2026-01-01"],
            "UHRZEIT": ["00:00:00.000000", "00:00:10.000000"],
            "WERT": [3.5, 4.5],
        }
    )

    result = s3s_model_dataframes_instance.insert_dataframe_into_time_table(
        time_table_tk="TT1", dataframe=df, overwrite=True
    )

    assert result is None
    assert deleted == ["ROW_OLD_1", "ROW_OLD_2"]
    assert ("ROW_NEW_0", "Zeit", "0,000000") in set_calls
    assert ("ROW_NEW_1", "Zeit", "10,000000") in set_calls
    assert ("ROW_NEW_0", "W", "3.5") in set_calls
    assert ("ROW_NEW_1", "W", "4.5") in set_calls


def test_insert_dataframe_into_time_table_returns_minus_one_for_missing_required_column(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []

    df_missing = pd.DataFrame({"TAG": ["2026-01-01"], "WERT": [1.5]})
    result = s3s_model_dataframes_instance.insert_dataframe_into_time_table(time_table_tk="TT1", dataframe=df_missing)

    assert result == -1


def test_get_dataframes_from_time_table_type_returns_joint_and_individual_dataframes(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1", "TT2"] if element_type == "MeasuredVariableTable" else []
    s3s_model_dataframes_instance._get_time_table_col_name_from_tk = lambda time_table_tk: ("W", "Sollwert")
    s3s_model_dataframes_instance.GetValue = lambda Tk, propertyName: ("Table A",) if Tk == "TT1" else ("Table B",)

    s3s_model_dataframes_instance.get_dataframe_from_time_table = lambda time_table_tk, value_col_name: (
        pd.DataFrame({value_col_name: [1.0]}, index=[10.0])
        if time_table_tk == "TT1"
        else pd.DataFrame({value_col_name: [2.0]}, index=[20.0])
    )

    df_h, dfs, tks = s3s_model_dataframes_instance.get_dataframes_from_time_table_type("MeasuredVariableTable")

    assert tks == ["TT1", "TT2"]
    assert set(dfs.keys()) == {"TT1", "TT2"}
    assert list(df_h.columns) == ["Table A", "Table B"]
    assert list(df_h.index) == [10.0, 20.0]
