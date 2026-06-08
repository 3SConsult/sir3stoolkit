from enum import Enum
import logging


class DummyObjectTypes(Enum):
    Node = "Node"
    Pipe = "Pipe"


def _configure_results_dataframe_stubs(s3s_model_dataframes_instance, end_nodes_applicable=True):
    calls = {
        "resolve_timestamps": [],
    }

    def fake_resolve_given_timestamps(timestamps):
        calls["resolve_timestamps"].append(timestamps)
        return ["TS1", "TS2"]

    s3s_model_dataframes_instance._resolve_given_timestamps = fake_resolve_given_timestamps
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__resolve_given_tks = (
        lambda element_type, tks, filter_container_tks: tks if tks else ["P1", "P2"]
    )
    s3s_model_dataframes_instance.GetPropertiesofElementType = lambda ElementType: ["Name", "Code"]
    s3s_model_dataframes_instance.GetResultProperties_from_elementType = (
        lambda elementType, onlySelectedVectors=False: ["DTTR", "PHR", "MVEC"]
    )
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__is_get_endnodes_applicable = (
        lambda element_type: end_nodes_applicable
    )

    result_values = {
        ("TS1", "P1", "DTTR"): ("12.5",),
        ("TS1", "P2", "DTTR"): ("13.5",),
        ("TS2", "P1", "DTTR"): ("14.5",),
        ("TS2", "P2", "DTTR"): ("15.5",),
        ("TS1", "P1", "PHR"): ("",),
        ("TS1", "P2", "PHR"): ("",),
        ("TS2", "P1", "PHR"): ("",),
        ("TS2", "P2", "PHR"): ("",),
        ("TS1", "P1", "MVEC"): ("1\t2\t3",),
        ("TS1", "P2", "MVEC"): ("4\t5\t6",),
        ("TS2", "P1", "MVEC"): ("7\t8\t9",),
        ("TS2", "P2", "MVEC"): ("10\t11\t12",),
    }
    s3s_model_dataframes_instance.GetResultfortimestamp = (
        lambda timestamp, Tk, property: result_values[(timestamp, Tk, property)]
    )
    s3s_model_dataframes_instance.GetValue = lambda Tk, propertyName: (f"name_{Tk}",)
    s3s_model_dataframes_instance.GetEndNodes = lambda Tk: ("N1", "N2", "-1", "-1")

    return calls


def test_generate_element_results_dataframe_all_properties_for_given_timestamps(s3s_model_dataframes_instance):
    calls = _configure_results_dataframe_stubs(s3s_model_dataframes_instance, end_nodes_applicable=True)

    df = s3s_model_dataframes_instance.generate_element_results_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=None,
        timestamps=["TS1", "TS2"],
    )

    assert list(df.index) == ["TS1", "TS2"]
    assert df.columns.names == ["tk", "name", "end_nodes", "property"]
    assert "DTTR" in set(df.columns.get_level_values("property"))
    assert "MVEC" in set(df.columns.get_level_values("property"))
    assert df.loc["TS1", ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "DTTR")] == 12.5
    assert df.loc["TS2", ("P2", "name_P2", "('N1', 'N2', '-1', '-1')", "MVEC")] == "10\t11\t12"
    assert calls["resolve_timestamps"][0] == ["TS1", "TS2"]


def test_generate_element_results_dataframe_excludes_model_data_property(s3s_model_dataframes_instance, caplog):
    _configure_results_dataframe_stubs(s3s_model_dataframes_instance, end_nodes_applicable=False)

    with caplog.at_level(logging.WARNING):
        df = s3s_model_dataframes_instance.generate_element_results_dataframe(
            element_type=DummyObjectTypes.Node,
            properties=["Name", "DTTR"],
            timestamps=["TS1"],
        )

    assert "is a model_data property; excluded from results" in caplog.text
    assert set(df.columns.get_level_values("property")) == {"DTTR"}
    assert set(df.columns.get_level_values("end_nodes")) == {"No end nodes on element type"}


def test_generate_element_results_dataframe_drops_placeholder_columns_by_default(s3s_model_dataframes_instance):
    _configure_results_dataframe_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_results_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=["PHR", "DTTR"],
        timestamps=["TS1", "TS2"],
    )

    assert "PHR" not in set(df.columns.get_level_values("property"))
    assert "DTTR" in set(df.columns.get_level_values("property"))


def test_generate_element_results_dataframe_keeps_placeholder_columns_when_requested(s3s_model_dataframes_instance):
    _configure_results_dataframe_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_results_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=["PHR"],
        timestamps=["TS1", "TS2"],
        drop_full_place_holder_columns=False,
    )

    assert set(df.columns.get_level_values("property")) == {"PHR"}
    assert df.loc["TS1", ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "PHR")] == 99999.0
    assert df.loc["TS2", ("P2", "name_P2", "('N1', 'N2', '-1', '-1')", "PHR")] == 99999.0


def test_generate_element_results_dataframe_returns_empty_if_no_valid_timestamps(s3s_model_dataframes_instance):
    _configure_results_dataframe_stubs(s3s_model_dataframes_instance)
    s3s_model_dataframes_instance._resolve_given_timestamps = lambda timestamps: []

    df = s3s_model_dataframes_instance.generate_element_results_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=["DTTR"],
        timestamps=["NOT_VALID"],
    )

    assert df.empty


def test_generate_element_results_dataframe_accepts_timestamp_indices_via_resolver(s3s_model_dataframes_instance):
    calls = _configure_results_dataframe_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_results_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=["DTTR"],
        timestamps=[0, 1],
    )

    assert not df.empty
    assert calls["resolve_timestamps"][0] == [0, 1]
    assert set(df.columns.get_level_values("property")) == {"DTTR"}


def test_generate_element_results_dataframe_excludes_unknown_property(s3s_model_dataframes_instance, caplog):
    _configure_results_dataframe_stubs(s3s_model_dataframes_instance)

    with caplog.at_level(logging.WARNING):
        df = s3s_model_dataframes_instance.generate_element_results_dataframe(
            element_type=DummyObjectTypes.Pipe,
            properties=["NOT_A_PROPERTY", "DTTR"],
            timestamps=["TS1"],
        )

    assert "not found in model_data or result properties" in caplog.text
    assert set(df.columns.get_level_values("property")) == {"DTTR"}
