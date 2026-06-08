from types import SimpleNamespace

import networkx as nx
import pandas as pd
from shapely.geometry import LineString


class DummyObjectTypes:
    Node = "Node"
    Pipe = "Pipe"


def test_sir3s_to_nx_graph_builds_nodes_and_edges(s3s_model_alternative_models_instance):
    s3s_model_alternative_models_instance.ObjectTypes = DummyObjectTypes()

    s3s_model_alternative_models_instance.generate_element_model_data_dataframe = lambda element_type, properties, geometry: pd.DataFrame(
        [
            {"tk": "1", "Fkcont": "C1", "geometry": "POINT (0 0)"},
            {"tk": "2", "Fkcont": "C1", "geometry": "POINT (1 1)"},
        ]
    )

    s3s_model_alternative_models_instance.generate_edge_dataframe = lambda: (
        pd.DataFrame(
            [
                {
                    "tk": "10",
                    "fkKI": 1,
                    "fkKK": 2,
                    "element type": "Pipe",
                    "geometry": "LINESTRING (0 0, 1 1)",
                }
            ]
        ),
        {},
    )

    graph = s3s_model_alternative_models_instance.SIR_3S_to_nx_graph()

    assert isinstance(graph, nx.DiGraph)
    assert graph.number_of_nodes() == 2
    assert graph.number_of_edges() == 1
    assert set(graph.nodes()) == {1, 2}
    assert graph.edges[(1, 2)]["tk"] == 10
    assert isinstance(graph.edges[(1, 2)]["geometry"], LineString)


def test_sir3s_to_nx_graph_returns_empty_graph_on_node_dataframe_error(s3s_model_alternative_models_instance):
    s3s_model_alternative_models_instance.ObjectTypes = DummyObjectTypes()

    def _raise(*args, **kwargs):
        raise RuntimeError("node retrieval failed")

    s3s_model_alternative_models_instance.generate_element_model_data_dataframe = _raise

    graph = s3s_model_alternative_models_instance.SIR_3S_to_nx_graph()

    assert isinstance(graph, nx.DiGraph)
    assert graph.number_of_nodes() == 0
    assert graph.number_of_edges() == 0


def test_add_properties_to_graph_updates_edge_attributes_for_pipe(s3s_model_alternative_models_instance):
    s3s_model_alternative_models_instance.ObjectTypes = DummyObjectTypes()

    s3s_model_alternative_models_instance.GetPropertiesofElementType = lambda ElementType: ["L"]
    s3s_model_alternative_models_instance.GetResultProperties_from_elementType = (
        lambda elementType, onlySelectedVectors=False: ["DTTR"]
    )
    s3s_model_alternative_models_instance.GetTksofElementType = lambda ElementType: [10]
    s3s_model_alternative_models_instance.GetTimeStamps = lambda: (["TS1"], "STAT", "TS1", "TS1")

    s3s_model_alternative_models_instance.generate_element_model_data_dataframe = (
        lambda element_type, properties, element_type_col, geometry, end_nodes: pd.DataFrame(
            [{"tk": 10, "L": 120.0}]
        )
    )

    cols = pd.MultiIndex.from_tuples(
        [(10, "Pipe 10", "('N1', 'N2', '-1', '-1')", "DTTR")],
        names=["tk", "name", "end_nodes", "property"],
    )
    s3s_model_alternative_models_instance.generate_element_results_dataframe = (
        lambda element_type, properties, timestamps: pd.DataFrame([[15.5]], index=["STAT"], columns=cols)
    )

    graph = nx.DiGraph()
    graph.add_edge(1, 2, tk=10, **{"element type": "Pipe"})

    enriched = s3s_model_alternative_models_instance.add_properties_to_graph(
        G=graph,
        element_type="Pipe",
        properties=["L", "DTTR"],
        timestamp="TS1",
    )

    assert enriched.edges[(1, 2)]["L"] == 120.0
    assert enriched.edges[(1, 2)]["DTTR"] == 15.5
