import pandas as pd


class _DummyObjectTypesMap:
    AGSN_HydraulicProfile = "AGSN_HydraulicProfile"
    Pipe = "Pipe"

    def __getitem__(self, key):
        return key


EDGE_ENUMS = ["Pipe", "Valve"]


def _configure_edge_dataframe_stubs(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__get_object_type_enums = (
        lambda names, enum_class: EDGE_ENUMS
    )

    calls = {
        "sort": [],
        "model": [],
        "results": [],
    }

    def fake_sort_properties(element_type, properties):
        calls["sort"].append({"element_type": element_type, "properties": list(properties)})
        return ["Kvr"], ["JV", "PVEC", "MVEC"], []

    def fake_model_df(element_type, properties, geometry, end_nodes, element_type_col, tks=None):
        calls["model"].append(
            {
                "element_type": element_type,
                "properties": list(properties),
                "geometry": geometry,
                "end_nodes": end_nodes,
                "element_type_col": element_type_col,
                "tks": None if tks is None else list(tks),
            }
        )
        if element_type == "Pipe":
            return pd.DataFrame(
                [
                    {
                        "tk": "P1",
                        "Kvr": "1",
                        "L": 10.0,
                        "Fkcont": "C1",
                        "element type": "Pipe",
                        "fkKI": "N1",
                        "fkKK": "N2",
                    }
                ]
            )
        return pd.DataFrame(
            [
                {
                    "tk": "V1",
                    "Kvr": "2",
                    "Fkcont": "C2",
                    "element type": "Valve",
                    "fkKI": "N3",
                    "fkKK": "N4",
                }
            ]
        )

    def fake_results_df(element_type, properties, timestamps, tks=None):
        calls["results"].append(
            {
                "element_type": element_type,
                "properties": list(properties),
                "timestamps": list(timestamps),
                "tks": None if tks is None else list(tks),
            }
        )
        if element_type == "Pipe":
            return pd.DataFrame([{"tk": "P1", "JV": 1.1, "PVEC": "1\t2", "MVEC": "3\t4"}])
        return pd.DataFrame([{"tk": "V1", "JV": 2.2, "PVEC": "5\t6", "MVEC": "7\t8"}])

    s3s_model_dataframes_instance.GetTksofElementType = (
        lambda ElementType: ["P1"] if ElementType == "Pipe" else ["V1"]
    )
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__sort_properties_into_model_data_and_results = (
        fake_sort_properties
    )
    s3s_model_dataframes_instance.generate_element_model_data_dataframe = fake_model_df
    s3s_model_dataframes_instance.generate_element_results_dataframe = fake_results_df
    def fake_merge(df_model_data, df_results):
        if df_results is None or df_results.empty:
            return df_model_data.copy()
        right = df_results.copy()
        if "tk" in right.columns:
            right["tk"] = right["tk"].map(
                lambda v: v[0] if isinstance(v, tuple) and len(v) == 1 else v
            )
        return df_model_data.merge(right, on="tk", how="outer")

    s3s_model_dataframes_instance.merge_model_data_and_results = fake_merge
    s3s_model_dataframes_instance.add_interior_points_to_start_end_sequence = lambda df: df

    return calls


def test_generate_longitudinal_section_dataframes_returns_supply_and_return_pairs(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()

    s3s_model_dataframes_instance.generate_element_model_data_dataframe = lambda element_type: pd.DataFrame(
        [{"tk": "AG1", "Lfdnr": 2, "Name": "Section 2"}]
    )

    class _HydraulicProfile:
        nrOfBranches = 0
        nodesVL = ["NVL1", "NVL2"]
        linksVL = ["PVL2", "PVL1"]
        xVL = [0.0, 20.0, 10.0]
        nodesRL = ["NRL1", "NRL2"]
        linksRL = ["PRL2", "PRL1"]
        xRL = [0.0, 30.0, 15.0]

    s3s_model_dataframes_instance.GetCourseOfHydraulicProfile = lambda tkAgsn, uid: _HydraulicProfile()
    s3s_model_dataframes_instance.generate_element_dataframe = (
        lambda element_type, tks=None, timestamps=None: (
            pd.DataFrame([{"tk": tk} for tk in tks]),
            {},
        )
    )

    dfs = s3s_model_dataframes_instance.generate_longitudinal_section_dataframes()

    assert len(dfs) == 1
    df_vl, df_rl = dfs[0]
    assert list(df_vl["tk"]) == ["PVL1", "PVL2"]
    assert list(df_rl["tk"]) == ["PRL1", "PRL2"]
    assert set(df_vl["AGSN_Lfdnr"].tolist()) == {2}
    assert set(df_vl["AGSN_Name"].tolist()) == {"Section 2"}


def test_generate_edge_dataframe_tutorial53_properties_with_timestamp_index(s3s_model_dataframes_instance):
    calls = _configure_edge_dataframe_stubs(s3s_model_dataframes_instance)

    df, timestamp_to_tuple_index = s3s_model_dataframes_instance.generate_edge_dataframe(
        properties=["Hal", "Kvr", "JV", "PVEC", "MVEC"],
        timestamps=[8],
    )

    assert not df.empty
    assert set(df["tk"].tolist()) == {"P1", "V1"}
    assert "JV" in df.columns
    assert "PVEC" in df.columns
    assert "MVEC" in df.columns
    assert isinstance(timestamp_to_tuple_index, dict)
    assert "Fkcont" in calls["model"][0]["properties"]
    assert all(call["timestamps"] == [8] for call in calls["results"])


def test_generate_edge_dataframe_tutorial53_properties_with_timestamp_string(s3s_model_dataframes_instance):
    calls = _configure_edge_dataframe_stubs(s3s_model_dataframes_instance)

    timestamp_str = "2025-09-25 00:40:00.000 +02:00"
    s3s_model_dataframes_instance.generate_edge_dataframe(
        properties=["Hal", "Kvr", "JV", "PVEC", "MVEC"],
        timestamps=[timestamp_str],
    )

    assert all(call["timestamps"] == [timestamp_str] for call in calls["results"])
    assert all(call["properties"] == ["Hal", "Kvr", "JV", "PVEC", "MVEC"] for call in calls["sort"])


def test_generate_edge_dataframe_adds_default_l_and_aligns_columns(s3s_model_dataframes_instance):
    _configure_edge_dataframe_stubs(s3s_model_dataframes_instance)

    df, _ = s3s_model_dataframes_instance.generate_edge_dataframe(properties=["Kvr", "JV"], timestamps=[0])

    assert not df.empty
    assert "L" in df.columns
    pipe_row_l = float(df.loc[df["tk"] == "P1", "L"].iloc[0])
    valve_row_l = float(df.loc[df["tk"] == "V1", "L"].iloc[0])
    assert pipe_row_l == 10.0
    assert valve_row_l == 0.0


def test_generate_edge_dataframe_returns_empty_when_no_edge_tks_exist(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__get_object_type_enums = (
        lambda names, enum_class: EDGE_ENUMS
    )
    s3s_model_dataframes_instance.GetTksofElementType = lambda ElementType: []

    result = s3s_model_dataframes_instance.generate_edge_dataframe(properties=["Kvr", "JV"], timestamps=[0])

    # Defensive check: method currently returns pd.DataFrame() in this branch.
    if isinstance(result, tuple):
        df, _ = result
    else:
        df = result

    assert df.empty


def test_generate_edge_dataframe_tk_filter_does_not_expand_to_other_types(s3s_model_dataframes_instance):
    calls = _configure_edge_dataframe_stubs(s3s_model_dataframes_instance)

    df, _ = s3s_model_dataframes_instance.generate_edge_dataframe(
        properties=["Kvr", "JV"],
        timestamps=[0],
        tks=["P1"],
    )

    assert not df.empty
    assert set(df["tk"].tolist()) == {"P1"}

    model_calls_by_type = {c["element_type"]: c for c in calls["model"]}
    results_calls_by_type = {c["element_type"]: c for c in calls["results"]}

    assert model_calls_by_type["Pipe"]["tks"] == ["P1"]
    assert results_calls_by_type["Pipe"]["tks"] == ["P1"]
    assert "Valve" not in model_calls_by_type
    assert "Valve" not in results_calls_by_type
