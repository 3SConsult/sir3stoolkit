from enum import Enum

import pandas as pd


class DummyObjectTypes(Enum):
    Node = "Node"
    Pipe = "Pipe"


def _configure_element_dataframe_stubs(s3s_model_dataframes_instance):
    calls = {
        "model": [],
        "results": [],
    }

    model_df = pd.DataFrame(
        {
            "tk": ["P1", "P2"],
            "L": [100.0, 200.0],
        }
    )

    # vec_format="multiindex" results: scalars at interior point -1, interior points 0..n-1
    result_columns = pd.MultiIndex.from_tuples(
        [
            ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "DTTR", -1),
            ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "MVEC", 0),
            ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "MVEC", 1),
            ("P1", "name_P1", "('N1', 'N2', '-1', '-1')", "MVEC", 2),
            ("P2", "name_P2", "('N3', 'N4', '-1', '-1')", "DTTR", -1),
            ("P2", "name_P2", "('N3', 'N4', '-1', '-1')", "MVEC", 0),
            ("P2", "name_P2", "('N3', 'N4', '-1', '-1')", "MVEC", 1),
        ],
        names=["tk", "name", "end_nodes", "property", "interior points"],
    )
    results_df = pd.DataFrame(
        [[12.5, 1.0, 2.0, 3.0, 13.5, 4.0, 5.0],
         [12.0, 1.5, 2.5, 3.5, 13.0, 99999.0, 99999.0]],  # P2's MVEC missing at TS2
        index=["STATIC_TS", "TS2"],
        columns=result_columns,
    ).astype("float32")

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

    def fake_generate_results(element_type, tks, properties, timestamps, place_holder_value=99999.0, bulk=False,
                              vec_format="str", include_name_and_end_nodes=True):
        calls["results"].append(
            {
                "element_type": element_type,
                "tks": tks,
                "properties": properties,
                "timestamps": timestamps,
                "bulk": bulk,
                "vec_format": vec_format,
                "include_name_and_end_nodes": include_name_and_end_nodes,
            }
        )
        if timestamps == ["NOT_A_TIMESTAMP"]:
            return pd.DataFrame()
        df = results_df.copy()
        if not include_name_and_end_nodes:  # as the real function: no name/end_nodes levels
            df.columns = df.columns.droplevel(["name", "end_nodes"])
        return df

    s3s_model_dataframes_instance.generate_element_model_data_dataframe = fake_generate_model_data
    s3s_model_dataframes_instance.generate_element_results_dataframe = fake_generate_results
    s3s_model_dataframes_instance.GetResultProperties_from_elementType = lambda element_type, onlySelectedVectors=False: ["DTTR", "MVEC"]
    s3s_model_dataframes_instance.GetTimeStamps = lambda: (["TS1", "TS2"], "STATIC_TS", "TS1", "TS2")
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__is_get_endnodes_applicable = lambda element_type: True

    return calls


def test_generate_element_dataframe_uses_static_timestamp_by_default(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    df, timestamp_to_tuple_index = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe, tks=None)

    assert not df.empty
    assert list(df["tk"]) == ["P1", "P2"]
    assert "DTTR" in df.columns
    assert calls["results"][0]["timestamps"] == ["STATIC_TS"]
    assert calls["results"][0]["vec_format"] == "multiindex"
    assert calls["results"][0]["include_name_and_end_nodes"] is False  # no label lookups
    assert timestamp_to_tuple_index == {"STATIC_TS": 0, "TS2": 1}


def test_generate_element_dataframe_result_tuples(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    df, _ = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe, tks=None)
    rows = df.set_index("tk")
    p1, p2 = rows.loc["P1"], rows.loc["P2"]

    assert p1["DTTR"] == (12.5, 12.0)
    assert p1["MVEC_start"] == (1.0, 1.5) and p1["MVEC_end"] == (3.0, 3.5)
    assert p1["MVEC_sequence"] == ((1.0, 2.0, 3.0), (1.5, 2.5, 3.5))
    assert p2["MVEC_start"] == (4.0, None) and p2["MVEC_end"] == (5.0, None)
    assert p2["MVEC_sequence"] == ((4.0, 5.0), ())
    assert list(df.columns) == ["tk", "L", "DTTR", "MVEC_end", "MVEC_sequence", "MVEC_start"]


def test_generate_element_dataframe_uses_given_timestamp_index(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=None,
        timestamps=[1],
    )

    assert calls["results"][0]["timestamps"] == [1]


def test_generate_element_dataframe_uses_given_timestamp_string(s3s_model_dataframes_instance):
    calls = _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=None,
        timestamps=["TS1"],
    )

    assert calls["results"][0]["timestamps"] == ["TS1"]


def test_generate_element_dataframe_returns_empty_for_invalid_timestamp_string(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)

    df, timestamp_to_tuple_index = s3s_model_dataframes_instance.generate_element_dataframe(
        element_type=DummyObjectTypes.Pipe,
        tks=None,
        timestamps=["NOT_A_TIMESTAMP"],
    )

    assert df.empty
    assert timestamp_to_tuple_index == {}


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

    df, timestamp_to_tuple_index = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe)

    assert df.empty
    assert timestamp_to_tuple_index == {}


def test_generate_element_dataframe_returns_empty_when_results_dataframe_is_empty(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)
    s3s_model_dataframes_instance.generate_element_results_dataframe = lambda **kwargs: pd.DataFrame()

    df, timestamp_to_tuple_index = s3s_model_dataframes_instance.generate_element_dataframe(element_type=DummyObjectTypes.Pipe)

    assert df.empty
    assert timestamp_to_tuple_index == {}


def test_merge_model_data_and_results_accepts_multiindex_results(s3s_model_dataframes_instance):
    _configure_element_dataframe_stubs(s3s_model_dataframes_instance)
    results = s3s_model_dataframes_instance.generate_element_results_dataframe(
        element_type=DummyObjectTypes.Pipe, tks=None, properties=None, timestamps=None, vec_format="multiindex")
    model = pd.DataFrame({"tk": ["P1", "P2"], "L": [100.0, 200.0]})

    df = s3s_model_dataframes_instance.merge_model_data_and_results(model, results)

    rows = df.set_index("tk")
    assert list(df.columns) == ["tk", "L", "DTTR", "MVEC_end", "MVEC_sequence", "MVEC_start"]
    assert rows.loc["P1", "MVEC_sequence"] == ((1.0, 2.0, 3.0), (1.5, 2.5, 3.5))
    assert rows.loc["P2", "MVEC_start"] == (4.0, None)


def test_name_and_end_node_levels_keep_column_index_lexsorted():
    import warnings
    from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
    # tk-major / property-minor order, deliberately not alphabetical
    cols = pd.MultiIndex.from_tuples([("T9", "QMAV", -1), ("T9", "PVEC", 0), ("T9", "PVEC", 1),
                                      ("T1", "QMAV", -1), ("T1", "PVEC", 0)],
                                     names=["tk", "property", "interior points"])
    df = pd.DataFrame([[1.0, 2.0, 3.0, 4.0, 5.0]], index=["ts"], columns=cols)
    labels = {"T9": ("Zeta", "e9"), "T1": ("Alpha", "e1")}
    df = SIR3S_Model_Dataframes._add_name_and_end_node_levels(df, labels, ["QMAV", "PVEC"])
    assert list(df.columns)[0] == ("T9", "Zeta", "e9", "QMAV", -1)
    df.columns = df.columns.droplevel(["name", "end_nodes"])
    assert df.columns._lexsort_depth == 3
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert df.loc["ts", ("T9", "PVEC")].tolist() == [2.0, 3.0]


def test_tuples_show_float32_values_in_shortest_representation(s3s_model_dataframes_instance):
    import numpy as np
    df = pd.DataFrame({"a": np.array([0.01343678, 4.2914047], dtype=np.float32), "b": ["x", "y"]}, index=["t1", "t2"])
    out, mapping = s3s_model_dataframes_instance.convert_rows_to_single_tuple_row(df)
    assert out["a"].iloc[0] == (0.01343678, 4.2914047)
    assert all(np.float32(v) == w for v, w in zip(out["a"].iloc[0], df["a"]))  # same float32 values
    assert out["b"].iloc[0] == ("x", "y") and mapping == {"t1": 0, "t2": 1}


def test_name_and_end_node_levels_per_element_mapping_matches_per_column_labels():
    from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
    cols = pd.MultiIndex.from_tuples([("T9", "QMAV", -1), ("T9", "PVEC", 0), ("T1", "QMAV", -1),
                                      ("T5", "QMAV", -1), ("T5", "PVEC", 0), ("T5", "PVEC", 1)],
                                     names=["tk", "property", "interior points"])
    df = pd.DataFrame([range(6)], index=["ts"], columns=cols, dtype=float)
    labels = {"T9": ("Same", "e9"), "T1": ("Other", "e1"), "T5": ("Same", "e5")}  # two tks share a name
    out = SIR3S_Model_Dataframes._add_name_and_end_node_levels(df.copy(), labels, ["QMAV", "PVEC"])
    assert list(out.columns) == [(tk, labels[tk][0], labels[tk][1], p, ip) for tk, p, ip in cols]
    assert list(out.columns.levels[1]) == ["Same", "Other"]  # one level entry per distinct name, in column order
    assert out.columns._lexsort_depth == out.columns.nlevels  # codes sorted: fast selection, no PerformanceWarning


def test_name_and_end_node_levels_none_keeps_tk_property_levels_lexsorted():
    from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
    cols = pd.MultiIndex.from_tuples([("T9", "QMAV", -1), ("T9", "PVEC", 0), ("T1", "QMAV", -1)],
                                     names=["tk", "property", "interior points"])
    df = pd.DataFrame([[1.0, 2.0, 3.0]], index=["ts"], columns=cols)
    out = SIR3S_Model_Dataframes._add_name_and_end_node_levels(df, None, ["QMAV", "PVEC"])
    assert out.columns.names == ["tk", "property", "interior points"]
    assert list(out.columns) == list(cols)
    assert out.columns._lexsort_depth == out.columns.nlevels  # codes sorted: fast selection, no PerformanceWarning
