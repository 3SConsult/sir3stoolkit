# -*- coding: utf-8 -*-
"""
Created on Thu Okt 7 13:39:13 2025

This module implements general plotting functions for SIR 3S applications. TODO: AGSN, Time Curves, Network Color Diagram

@author: Jablonski

"""
from __future__ import annotations

import pandas as pd
from typing import List, Optional, Union
import numpy as np
import pandas as pd
import geopandas as gpd
from typing import Optional, Dict, Any, Tuple, List
from shapely.geometry import LineString, MultiLineString
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

import re
from typing import Dict, Tuple, Optional

import logging

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

from sir3stoolkit.core.wrapper import SIR3S_Model

class Plotting_SIR3S_Model(SIR3S_Model):
    
    def create_pipe_layer(
        self,
        gdf: gpd.GeoDataFrame,
        geometry_col: Optional[str] = "geometry",
        width_scaling_col: Optional[str] = None,
        color_mixing_col: Optional[str] = None,
        *,
        min_width: float = 0.5,
        max_width: float = 6.0,
        default_color = (0.75, 0.75, 0.75, 1.0),
        cmap: str = "viridis",
        ax: Optional[plt.Axes] = None,
    ) -> Dict[str, Any]:
        """
        Create and plot a pipe layer from a GeoDataFrame.

        Parameters
        ----------
        gdf : GeoDataFrame
            Must contain LineString or MultiLineString geometries.
        geometry_col : str, optional
            Name of the geometry column. Defaults to 'geometry'.
        width_scaling_col : str, optional
            Numeric column to scale line width. If None, uses a constant width.
        color_mixing_col : str, optional
            Numeric column to color lines via colormap. If None, uses a constant color.
        min_width, max_width : float
            Minimum/maximum linewidth in points.
        cmap : str
            Matplotlib colormap name used when `color_mixing_col` is provided.
        ax : matplotlib.axes.Axes, optional
            Axes to draw on. If None, uses current axes.

        Returns
        -------
        layer : dict
            {
              'artist': LineCollection,
              'axes': Axes,
              'bbox': (xmin, ymin, xmax, ymax),
              'norm': matplotlib.colors.Normalize or None,
              'cmap': matplotlib Colormap or None,
              'value_ranges': {'width': (wmin, wmax), 'color': (cmin, cmax) or None},
              'n_segments': int
            }

        Notes
        -----
        - Efficiently packs all polylines into a single LineCollection.
        - If `color_mixing_col` is provided, the collection is "mappable" and
          you can add a colorbar upstream with: `plt.colorbar(layer['artist'], ax=ax)`.
        - If `width_scaling_col` or `color_mixing_col` have constant values, a safe
          mid-value normalization is used.
        """
        if not isinstance(gdf, gpd.GeoDataFrame):
            raise TypeError("gdf must be a GeoDataFrame")

        if geometry_col not in gdf.columns:
            raise ValueError(f"Geometry column '{geometry_col}' not found in gdf")

        # Work on a clean copy with positional index for consistent mapping
        gf = gdf.reset_index(drop=True).copy()

        # Extract segments and owner row indices
        segments, owners = self._explode_lines_to_segments(gf, geometry_col)
        if len(segments) == 0:
            raise ValueError("No valid LineString/MultiLineString geometries found to plot.")

        # ----- Widths -----
        if width_scaling_col is not None:
            if width_scaling_col not in gf.columns:
                raise ValueError(f"Width scaling column '{width_scaling_col}' not found in gdf")

            wvals = pd.to_numeric(gf[width_scaling_col], errors="coerce")
            wnorm, wmin, wmax = self._minmax_normalize(wvals)
            widths_per_row = min_width + wnorm * (max_width - min_width)
            widths = widths_per_row[np.array(owners)]
        else:
            # Constant width if no scaling column
            widths = np.full(len(segments), (min_width + max_width) * 0.5)
            wmin, wmax = np.nan, np.nan  # no scaling info
        # ----- Colors -----
        the_cmap = None
        norm = None
        array_for_colormap = None

        if color_mixing_col is not None:
            if color_mixing_col not in gf.columns:
                raise ValueError(f"Color mixing column '{color_mixing_col}' not found in gdf")

            cvals = pd.to_numeric(gf[color_mixing_col], errors="coerce")
            # We'll use Normalize directly (better for colorbar linkage)
            cmin = np.nanmin(cvals.values) if np.isfinite(cvals.values).any() else 0.0
            cmax = np.nanmax(cvals.values) if np.isfinite(cvals.values).any() else 1.0
            if not np.isfinite(cmin) or not np.isfinite(cmax) or cmin == cmax:
                # Fall back to a safe range
                cmin, cmax = 0.0, 1.0
            norm = Normalize(vmin=float(cmin), vmax=float(cmax), clip=True)
            the_cmap = get_cmap(cmap)
            # Per-segment values from per-row values via owners
            row_vals = cvals.to_numpy()
            array_for_colormap = row_vals[np.array(owners)]
            color_range = (float(cmin), float(cmax))
        else:
            color_range = None

        # ----- Build and add LineCollection -----
        if ax is None:
            ax = plt.gca()

        lc_kwargs = dict(
            segments=segments,
            linewidths=widths,
            capstyle="round",
            joinstyle="round",
            zorder=2,
        )

        if array_for_colormap is not None:
            lc = LineCollection(**lc_kwargs, cmap=the_cmap, norm=norm)
            lc.set_array(array_for_colormap)  # enables colorbar
        else:
            lc = LineCollection(**lc_kwargs, colors=[default_color])

        ax.add_collection(lc)

        # ----- Axes extent -----
        # Use GeoDataFrame bounds for stability; fall back to autoscale as needed.
        try:
            xmin, ymin, xmax, ymax = gpd.GeoSeries(gf[geometry_col]).total_bounds
            bbox = (xmin, ymin, xmax, ymax)
            if np.isfinite(xmin) and np.isfinite(ymin) and np.isfinite(xmax) and np.isfinite(ymax):
                ax.set_xlim(xmin, xmax)
                ax.set_ylim(ymin, ymax)
        except Exception:
            ax.autoscale_view()
            # Compute a loose bbox if needed
            xs = np.concatenate([seg[:, 0] for seg in segments])
            ys = np.concatenate([seg[:, 1] for seg in segments])
            bbox = (float(np.nanmin(xs)), float(np.nanmin(ys)),
                    float(np.nanmax(xs)), float(np.nanmax(ys)))

        # Keep aspect ratio square for networks
        try:
            ax.set_aspect("equal", adjustable="box")
        except Exception:
            pass

        layer = {
            "artist": lc,
            "axes": ax,
            "bbox": bbox,
            "norm": norm,
            "cmap": the_cmap,
            "value_ranges": {
                "width": (float(wmin), float(wmax)) if np.isfinite([wmin, wmax]).all() else None,
                "color": color_range,
            },
            "n_segments": len(segments),
            "kind": "pipes",
        }
        return layer

    # ---------------------------
    # Helpers
    # ---------------------------

    @staticmethod
    def _minmax_normalize(series: pd.Series) -> Tuple[np.ndarray, float, float]:
        """
        Min-max normalize numeric series to [0, 1], handling NaNs and constant vectors.

        Returns
        -------
        norm_values : np.ndarray
            Same length as series, NaNs become 0.5 (neutral midpoint).
        vmin, vmax : float
            The numeric min and max used. If constant/invalid, returns (0.0, 1.0).
        """
        vals = pd.to_numeric(series, errors="coerce").to_numpy(dtype=float)
        finite = np.isfinite(vals)

        if not finite.any():
            return np.full_like(vals, 0.5), 0.0, 1.0

        vmin = float(np.nanmin(vals[finite]))
        vmax = float(np.nanmax(vals[finite]))
        if vmin == vmax:
            # All equal → neutral 0.5
            norm = np.full_like(vals, 0.5)
            return norm, vmin, vmax

        norm = (vals - vmin) / (vmax - vmin)
        norm = np.clip(norm, 0.0, 1.0)
        # Replace NaNs with neutral midpoint
        norm[~finite] = 0.5
        return norm, vmin, vmax

    @staticmethod
    def _explode_lines_to_segments(
        gdf: gpd.GeoDataFrame, geometry_col: str
    ) -> Tuple[List[np.ndarray], List[int]]:
        """
        Convert LineString/MultiLineString geometries to a list of polyline segments.

        Returns
        -------
        segments : list of (N_i x 2) float arrays
            Each array is the sequence of [x, y] vertices for a line.
        owners : list of int
            Row index (positional in gdf.reset_index(drop=True)) that each segment came from.
        """
        segments: List[np.ndarray] = []
        owners: List[int] = []

        geoms = gdf[geometry_col]
        for i, geom in enumerate(geoms):
            if geom is None:
                continue
            if isinstance(geom, LineString):
                coords = np.asarray(geom.coords, dtype=float)
                if coords.shape[0] >= 2:
                    segments.append(coords)
                    owners.append(i)
            elif isinstance(geom, MultiLineString):
                for part in geom.geoms:
                    if isinstance(part, LineString):
                        coords = np.asarray(part.coords, dtype=float)
                        if coords.shape[0] >= 2:
                            segments.append(coords)
                            owners.append(i)
            else:
                # Non-line geometry: skip
                continue

        return segments, owners