import pytest
from enum import Enum
import logging
import pandas as pd
from shapely.geometry import Point

from sir3stoolkit.mantle import dataframes

class DummyObjectTypes(Enum):
    Node = "Node"
    Pipe = "Pipe"


def _configure_base_stubs(s3s_model_dataframes_instance):
    s3s_model_dataframes_instance.GetTksofElementType = lambda ElementType: ["N1", "N2"]
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__resolve_given_tks = (
        lambda element_type, tks, filter_container_tks: tks if tks else ["N1", "N2"]
    )
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__resolve_given_model_data_properties = (
        lambda element_type, properties: ["Name", "Code"] if properties is None else properties
    )
    s3s_model_dataframes_instance._SIR3S_Model_Dataframes__is_get_endnodes_applicable = (
        lambda element_type: element_type.name in {"Pipe"}
    )
    s3s_model_dataframes_instance.GetValue = (
        lambda Tk, propertyName: {
            ("N1", "Name"): ("Node 1",),
            ("N1", "Code"): ("101",),
            ("N1", "FkdtroRowd"): ("row_1",),
            ("N2", "Name"): ("Node 2",),
            ("N2", "Code"): ("102",),
            ("N2", "FkdtroRowd"): ("row_2",),
        }[(Tk, propertyName)]
    )
    s3s_model_dataframes_instance.GetGeometryInformation = lambda Tk: "POINT (7 52)"
    s3s_model_dataframes_instance.get_EPSG = lambda: ("0", None, None)
    s3s_model_dataframes_instance.GetEndNodes = lambda Tk: ("KI", "KK", "-1", "-1")


def test_generate_element_model_data_dataframe_defaults(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Node
    )

    assert list(df.columns) == ["tk", "Name", "Code"]
    assert list(df["tk"]) == ["N1", "N2"]
    assert df["Code"].tolist() == [101, 102]


def test_generate_element_model_data_dataframe_with_tks_filter(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Node,
        tks=["N2"]
    )

    assert list(df["tk"]) == ["N2"]


def test_generate_element_model_data_dataframe_with_empty_properties(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Node,
        properties=[]
    )

    assert list(df.columns) == ["tk"]


def test_generate_element_model_data_dataframe_with_geometry(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Node,
        properties=[],
        geometry=True
    )

    assert "geometry" in df.columns
    assert isinstance(df.loc[0, "geometry"], Point)


def test_generate_element_model_data_dataframe_with_end_nodes_requested_for_node(s3s_model_dataframes_instance, caplog):
    _configure_base_stubs(s3s_model_dataframes_instance)

    with caplog.at_level(logging.WARNING):
        df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
            element_type=DummyObjectTypes.Node,
            properties=[],
            end_nodes=True
        )

    assert "End nodes are not defined for element type" in caplog.text
    assert "fkKI" not in df.columns
    assert "fkKK" not in df.columns
    assert "fkKI2" not in df.columns
    assert "fkKK2" not in df.columns


def test_generate_element_model_data_dataframe_with_end_nodes_for_pipe(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=[],
        end_nodes=True
    )

    assert "fkKI" in df.columns
    assert "fkKK" in df.columns
    assert "fkKI2" not in df.columns
    assert "fkKK2" not in df.columns


def test_generate_element_model_data_dataframe_with_element_type_column(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Node,
        properties=[],
        element_type_col=True
    )

    assert "element type" in df.columns
    assert set(df["element type"].tolist()) == {"Node"}


def test_generate_element_model_data_dataframe_with_resolve_references(s3s_model_dataframes_instance):
    _configure_base_stubs(s3s_model_dataframes_instance)
    s3s_model_dataframes_instance.get_dataframes_from_nominal_diameter_tables = (
        lambda: (pd.DataFrame([{"tk_merge": "row_1", "D": 80}, {"tk_merge": "row_2", "D": 100}]), None, None)
    )

    df = s3s_model_dataframes_instance.generate_element_model_data_dataframe(
        element_type=DummyObjectTypes.Pipe,
        properties=["FkdtroRowd"],
        resolve_references=True
    )

    assert "PipeTable: D" in df.columns
    assert "tk_merge" not in df.columns
    assert df["PipeTable: D"].tolist() == [80, 100]
