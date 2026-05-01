from enum import Enum

import pandas as pd


class DummyObjectTypes(Enum):
    Node = "Node"
    Pipe = "Pipe"


def _configure_element_dataframe_stubs(s3s_model_dataframes_instance):
    calls = {
        "model": [],
        "results": [],
        "add_vectors": [],
    }

    model_df = pd.DataFrame(
        {
            "tk": ["P1", "P2"],
            "L": [100.0, 200.0],
        }
    )

    result_columns = pd.MultiIndex.from_tuples(
        [
            ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "DTTR"),
            ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "MVEC"),
            ("P2", "name_P2", "('N3', 'N4', '-1', '-1')", "DTTR"),
            ("P2", "name_P2", "('N3', 'N4', '-1', '-1')", "MVEC"),
        ],
        names=["tk", "name", "end_nodes", "property"],
    )
    results_df = pd.DataFrame(
        [[12.5, "1\t2\t3", 13.5, "4\t5\t6"]],
        index=["STATIC_TS"],
        columns=result_columns,
    )

    def fake_generate_model_data(element_type, tks, properties, geometry, end_nodes, element_type_col, resolve_references):
        calls["model"].append(
            {
                "element_type": element_type,
                "tks": tks,
                "properties": properties,
                "geometry": geometry,
                "end_nodes": end_nodes,
                "element_type_col": element_type_col,
                "resolve_references": resolve_references,
            }
        )
        return model_df.copy()

    def fake_generate_results(element_type, tks, properties, timestamps):
        calls["results"].append(
            {
                "element_type": element_type,
                "tks": tks,
                "properties": properties,
                "timestamps": timestamps,
            }
        )
        return results_df.copy()

    def fake_add_vectors(df):
        calls["add_vectors"].append(True)
        return df

    s3s_model_dataframes_instance.generate_element_model_data_dataframe = fake_generate_model_data
    s3s_model_dataframes_instance.generate_element_results_dataframe = fake_generate_results
    s3s_model_dataframes_instance.add_interior_points_to_start_end_sequence = fake_add_vectors
    s3s_model_dataframes_instance.GetResultProperties_from_elementType = lambda element_type, onlySelectedVectors=False: ["DTTR", "MVEC"]
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["TS1", "TS2"], "STATIC_TS", "TS1", "TS2")
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__is_get_endnodes_applicable = lambda element_type: True

    return calls


def test_generate_element_dataframe_uses_static_timestamp_by_default(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe, tks=None)

    assert not df.empty
    assert list(df["tk"]) == ["P1", "P2"]
    assert "DTTR" in df.columns
    assert calls["results"][0]["timestamps"] == ["STATIC_TS"]


def test_generate_element_dataframe_uses_given_timestamp_index(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=None,
        timestamp=1,
    )

    assert calls["results"][0]["timestamps"] == ["TS2"]


def test_generate_element_dataframe_uses_given_timestamp_string(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=None,
        timestamp="TS1",
    )

    assert calls["results"][0]["timestamps"] == ["TS1"]


def test_generate_element_dataframe_returns_empty_for_invalid_timestamp_string(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=None,
        timestamp="NOT_A_TIMESTAMP",
    )

    assert df.empty


def test_generate_element_dataframe_passes_tks_to_subcalls(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=["P2"],
    )

    assert calls["model"][0]["tks"] == ["P2"]
    assert calls["results"][0]["tks"] == ["P2"]


def test_generate_element_dataframe_returns_empty_when_model_dataframe_is_empty(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)
    s3s_model_dataframes_instance.generate_element_model_data_dataframe = lambda **kwargs: pd.DataFrame()

    df = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe)

    assert df.empty


def test_generate_element_dataframe_returns_empty_when_results_dataframe_is_empty(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)
    s3s_model_dataframes_instance.generate_element_results_dataframe = lambda **kwargs: pd.DataFrame()

    df = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe)

    assert df.empty
