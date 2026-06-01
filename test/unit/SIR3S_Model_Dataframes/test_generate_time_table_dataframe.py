import pandas as pd
import pytest


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


def _df_from_state(state, value_col_name, flag_mapping=None):
    rows = []
    for tk, row_data in state.items():
        rows.append(
            {
                "Zeit [s]": float(str(row_data["Zeit"]).replace(",", ".")),
                "tk": tk,
                value_col_name: float(str(row_data["W"]).replace(",", ".")),
            }
        )

    if not rows:
        df = pd.DataFrame({"tk": [None], value_col_name: [float("nan")]}, index=[float("nan")])
    else:
        df = pd.DataFrame(rows).set_index("Zeit [s]").sort_index()

    if flag_mapping is not None:
        df["operation_flag"] = df.index.map(flag_mapping).fillna("unmapped")

    return df


def test_insert_dataframe_into_time_table_validates_and_writes_rows(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()

    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["2026-01-01 00:00:00.000000 +00:00"], "STAT", "MIN", "MAX")
    s3s_model_dataframes_instance._get_time_table_col_name_from_tk = lambda time_table_tk: ("W", "Sollwert")
    s3s_model_dataframes_instance.get_dataframe_from_time_table = lambda time_table_tk, value_col_name, flag_mapping=None: pd.DataFrame(
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

    assert isinstance(result, pd.DataFrame)
    assert deleted == []
    assert ("ROW_NEW_0", "Zeit", "0,000000") in set_calls
    assert ("ROW_NEW_1", "Zeit", "10,000000") in set_calls
    assert ("ROW_NEW_0", "W", "1.5") in set_calls
    assert ("ROW_NEW_1", "W", "2.5") in set_calls


def test_insert_dataframe_into_time_table_overwrite_true_updates_existing_rows_in_place(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()

    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["2026-01-01 00:00:00.000000 +00:00"], "STAT", "MIN", "MAX")
    s3s_model_dataframes_instance._get_time_table_col_name_from_tk = lambda time_table_tk: ("W", "Sollwert")
    s3s_model_dataframes_instance.get_dataframe_from_time_table = lambda time_table_tk, value_col_name, flag_mapping=None: pd.DataFrame(
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

    assert isinstance(result, pd.DataFrame)
    assert deleted == []
    assert ("ROW_OLD_1", "W", "3.5") in set_calls
    assert ("ROW_OLD_2", "W", "4.5") in set_calls


@pytest.mark.parametrize(
    "overwrite,keep,expected_flags,expected_index,expected_deleted_count",
    [
        (
            True,
            True,
            {0.0: "kept", 10.0: "overwritten", 20.0: "inserted"},
            [0.0, 10.0, 20.0],
            0,
        ),
        (
            True,
            False,
            {10.0: "overwritten", 20.0: "inserted"},
            [10.0, 20.0],
            1,
        ),
        (
            False,
            True,
            {0.0: "kept", 10.0: "inserted", 20.0: "inserted"},
            [0.0, 10.0, 20.0],
            1,
        ),
        (
            False,
            False,
            {10.0: "inserted", 20.0: "inserted"},
            [10.0, 20.0],
            2,
        ),
    ],
)
def test_insert_dataframe_into_time_table_keep_overwrite_matrix(
    s3s_model_dataframes_instance,
    overwrite,
    keep,
    expected_flags,
    expected_index,
    expected_deleted_count,
):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["2026-01-01 00:00:00.000000 +00:00"], "STAT", "MIN", "MAX")
    s3s_model_dataframes_instance._get_time_table_col_name_from_tk = lambda time_table_tk: ("W", "Sollwert")

    table_state = {
        "ROW_OLD_1": {"Zeit": "0,000000", "W": "1.0"},
        "ROW_OLD_2": {"Zeit": "10,000000", "W": "2.0"},
    }

    deleted = []
    created_rows = []

    def _get_dataframe_from_time_table(time_table_tk, value_col_name, flag_mapping=None):
        return _df_from_state(table_state, value_col_name=value_col_name, flag_mapping=flag_mapping)

    def _delete_element(tk):
        deleted.append(tk)
        table_state.pop(tk, None)

    def _add_table_row(tablePkTk):
        new_tk = f"ROW_NEW_{len(created_rows)}"
        created_rows.append(new_tk)
        table_state[new_tk] = {"Zeit": "0,000000", "W": "0.0"}
        return (new_tk,)

    def _set_value(Tk, propertyName, Value):
        table_state[Tk][propertyName] = Value

    s3s_model_dataframes_instance.get_dataframe_from_time_table = _get_dataframe_from_time_table
    s3s_model_dataframes_instance.DeleteElement = _delete_element
    s3s_model_dataframes_instance.AddTableRow = _add_table_row
    s3s_model_dataframes_instance.SetValue = _set_value

    df = pd.DataFrame(
        {
            "TAG": ["2026-01-01", "2026-01-01"],
            "UHRZEIT": ["00:00:10.000000", "00:00:20.000000"],
            "WERT": [30.0, 40.0],
        }
    )

    result = s3s_model_dataframes_instance.insert_dataframe_into_time_table(
        time_table_tk="TT1",
        dataframe=df,
        overwrite=overwrite,
        keep=keep,
    )

    assert list(result.index) == expected_index
    assert result["operation_flag"].to_dict() == expected_flags
    assert float(result.loc[10.0, "WERT"]) == 30.0
    assert len(deleted) == expected_deleted_count


def test_insert_dataframe_into_time_table_returns_empty_dataframe_for_missing_required_column(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance.GetTksofElementType = lambda element_type: ["TT1"] if element_type == "MeasuredVariableTable" else []

    df_missing = pd.DataFrame({"TAG": ["2026-01-01"], "WERT": [1.5]})
    result = s3s_model_dataframes_instance.insert_dataframe_into_time_table(time_table_tk="TT1", dataframe=df_missing)

    assert isinstance(result, pd.DataFrame)
    assert result.empty


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
