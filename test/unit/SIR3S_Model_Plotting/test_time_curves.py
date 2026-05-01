import matplotlib
matplotlib.use("Agg")

import pandas as pd
import pytest


def _build_results_dataframe_for_time_curves():
    index = pd.to_datetime(["2026-01-01 00:00:00", "2026-01-01 01:00:00", "2026-01-01 02:00:00"])
    columns = pd.MultiIndex.from_tuples(
        [
            ("N1", "Node A", "No end nodes on element type", "PH"),
            ("N1", "Node A", "No end nodes on element type", "T"),
            ("N2", "Node B", "No end nodes on element type", "PH"),
            ("N2", "Node B", "No end nodes on element type", "T"),
        ],
        names=["tk", "name", "end_nodes", "property"],
    )
    return pd.DataFrame(
        [
            [5.0, 70.0, 4.5, 68.0],
            [5.2, 71.0, 4.7, 68.5],
            [5.1, 71.5, 4.6, 69.0],
        ],
        index=index,
        columns=columns,
    )


def test_plot_time_curves_returns_figure_axes_and_used_properties(s3s_model_plotting_instance):
    df = _build_results_dataframe_for_time_curves()

    fig, axes, used = s3s_model_plotting_instance.plot_time_curves(
        df=df,
        properties=["PH", "T"],
        start="2026-01-01 00:00:00",
        end="2026-01-01 02:00:00",
        legend=True,
    )

    assert fig is not None
    assert len(axes) == 2
    assert used == ["PH", "T"]
    assert axes[0].get_ylabel() != ""
    assert axes[1].get_ylabel() != ""


def test_plot_time_curves_respects_tks_per_property_filter(s3s_model_plotting_instance):
    df = _build_results_dataframe_for_time_curves()

    fig, axes, used = s3s_model_plotting_instance.plot_time_curves(
        df=df,
        properties=["PH"],
        tks_per_property=[["N1"]],
        legend=True,
    )

    assert fig is not None
    assert used == ["PH"]
    assert len(axes[0].lines) == 1
    assert "N1" in axes[0].lines[0].get_label() or "Node A" in axes[0].lines[0].get_label()


def test_plot_time_curves_raises_on_non_multiindex_columns(s3s_model_plotting_instance):
    df = pd.DataFrame({"PH": [1.0, 2.0, 3.0]}, index=pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-03"]))

    with pytest.raises(ValueError, match="MultiIndex"):
        s3s_model_plotting_instance.plot_time_curves(df=df)


def test_plot_time_curves_missing_property_policy_error(s3s_model_plotting_instance):
    df = _build_results_dataframe_for_time_curves()

    with pytest.raises(ValueError, match="missing or filtered out"):
        s3s_model_plotting_instance.plot_time_curves(
            df=df,
            properties=["NOT_PRESENT"],
            missing="error",
        )
