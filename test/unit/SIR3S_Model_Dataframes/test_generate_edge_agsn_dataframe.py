import pandas as pd


class _DummyObjectTypesMap:
    AGSN_HydraulicProfile = "AGSN_HydraulicProfile"
    Pipe = "Pipe"

    def __getitem__(self, key):
        return key


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
    s3s_model_dataframes_instance.generate_element_dataframe = lambda element_type, tks=None, timestamp=None: pd.DataFrame(
        [{"tk": tk} for tk in tks]
    )

    dfs = s3s_model_dataframes_instance.generate_longitudinal_section_dataframes()

    assert len(dfs) == 1
    df_vl, df_rl = dfs[0]
    assert list(df_vl["tk"]) == ["PVL1", "PVL2"]
    assert list(df_rl["tk"]) == ["PRL1", "PRL2"]
    assert set(df_vl["AGSN_Lfdnr"].tolist()) == {2}
    assert set(df_vl["AGSN_Name"].tolist()) == {"Section 2"}


def test_generate_edge_dataframe_adds_fkcont_and_returns_combined_dataframe(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.ObjectTypes = _DummyObjectTypesMap()
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__get_object_type_enums = lambda names, enum_class: ["Pipe", "Valve"]

    calls = {"model_properties": []}

    s3s_model_dataframes_instance.GetTksofElementType = lambda ElementType: ["P1"] if ElementType == "Pipe" else []
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__sort_properties_into_model_data_and_results = (
        lambda element_type, properties: (["L"], ["DTTR"], [])
    )

    def fake_model_df(element_type, properties, geometry, end_nodes, element_type_col):
        calls["model_properties"].append(list(properties))
        return pd.DataFrame([{"tk": "P1", "L": 123.0}])

    s3s_model_dataframes_instance.generate_element_model_data_dataframe = fake_model_df
    s3s_model_dataframes_instance.generate_element_results_dataframe = (
        lambda element_type, properties, timestamps: pd.DataFrame([{"tk": "P1", "DTTR": 12.5}])
    )
    s3s_model_dataframes_instance.merge_model_data_and_results = (
        lambda df_model_data, df_results: df_model_data.merge(df_results, on="tk", how="outer")
    )
    s3s_model_dataframes_instance.add_interior_points_to_start_end_sequence = lambda df: df

    df = s3s_model_dataframes_instance.generate_edge_dataframe(properties=[], timestamps=[0])

    assert not df.empty
    assert list(df["tk"]) == ["P1"]
    assert "DTTR" in df.columns
    assert "Fkcont" in calls["model_properties"][0]
