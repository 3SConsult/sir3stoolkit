import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import LineString, Point


def test_plot_node_layer_returns_color_legend_patches_and_draws_points(s3s_model_plotting_instance):
    fig, ax = plt.subplots()
    gdf = pd.DataFrame(
        {
            "geometry": [Point(0, 0), Point(1, 1)],
            "P": [5.0, 7.0],
            "size_val": [1.0, 2.0],
        }
    )

    patches = s3s_model_plotting_instance.plot_node_layer(
        ax=ax,
        gdf=gdf,
        size_scaling_col="size_val",
        color_mixing_col="P",
    )

    assert patches is not None
    assert len(patches) == 5
    assert len(ax.collections) >= 1


def test_plot_pipe_layer_returns_color_legend_patches_and_draws_segments(s3s_model_plotting_instance):
    fig, ax = plt.subplots()
    gdf = pd.DataFrame(
        {
            "geometry": [LineString([(0, 0), (1, 1)]), LineString([(1, 1), (2, 1)])],
            "diameter": [100.0, 120.0],
            "temperature": [70.0, 80.0],
        }
    )

    patches = s3s_model_plotting_instance.plot_pipe_layer(
        ax=ax,
        gdf=gdf,
        width_scaling_col="diameter",
        color_mixing_col="temperature",
    )

    assert patches is not None
    assert len(patches) == 5
    assert len(ax.collections) >= 1


def test_plot_node_layer_returns_none_for_missing_geometry_column(s3s_model_plotting_instance):
    fig, ax = plt.subplots()
    gdf = pd.DataFrame({"P": [1.0, 2.0]})

    patches = s3s_model_plotting_instance.plot_node_layer(
        ax=ax,
        gdf=gdf,
        color_mixing_col="P",
    )

    assert patches is None


def test_plot_pipe_layer_returns_none_for_invalid_width_column(s3s_model_plotting_instance):
    fig, ax = plt.subplots()
    gdf = pd.DataFrame(
        {
            "geometry": [LineString([(0, 0), (1, 1)])],
            "temperature": [70.0],
        }
    )

    patches = s3s_model_plotting_instance.plot_pipe_layer(
        ax=ax,
        gdf=gdf,
        width_scaling_col="missing_width",
        color_mixing_col="temperature",
    )

    assert patches is None
