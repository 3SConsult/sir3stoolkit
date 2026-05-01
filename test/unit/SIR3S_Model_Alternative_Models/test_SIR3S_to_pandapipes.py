from types import SimpleNamespace

import pandas as pd
from shapely.geometry import LineString, Point

import sir3stoolkit.mantle.alternative_models as alternative_models_module


class DummyObjectTypes:
    Node = "Node"
    Pipe = "Pipe"


class FakePP:
    def __init__(self):
        self.calls = {
            "junction": [],
            "pipe": [],
            "ext_grid": [],
            "sink": [],
        }

    def create_empty_network(self, fluid="water"):
        return SimpleNamespace(
            junction_geodata=pd.DataFrame(columns=["x", "y"]),
            pipe_geodata=pd.DataFrame(columns=["coords"]),
        )

    def create_junction(self, net, pn_bar, tfluid_k, height_m, name):
        idx = len(self.calls["junction"])
        self.calls["junction"].append(
            {
                "pn_bar": pn_bar,
                "tfluid_k": tfluid_k,
                "height_m": height_m,
                "name": name,
            }
        )
        net.junction_geodata.loc[idx, ["x", "y"]] = [None, None]
        return idx

    def create_pipe_from_parameters(self, net, from_junction, to_junction, length_km, diameter_m, k_mm, name):
        idx = len(self.calls["pipe"])
        self.calls["pipe"].append(
            {
                "from_junction": from_junction,
                "to_junction": to_junction,
                "length_km": length_km,
                "diameter_m": diameter_m,
                "k_mm": k_mm,
                "name": name,
            }
        )
        net.pipe_geodata.loc[idx, ["coords"]] = [None]
        return idx

    def create_ext_grid(self, net, junction, p_bar, t_k, name):
        self.calls["ext_grid"].append(
            {
                "junction": junction,
                "p_bar": p_bar,
                "t_k": t_k,
                "name": name,
            }
        )

    def create_sink(self, net, junction, mdot_kg_per_s, name):
        self.calls["sink"].append(
            {
                "junction": junction,
                "mdot_kg_per_s": mdot_kg_per_s,
                "name": name,
            }
        )


def test_sir3s_to_pandapipes_builds_network_elements(monkeypatch, s3s_model_alternative_models_instance):
    fake_pp = FakePP()
    monkeypatch.setattr(alternative_models_module, "pp", fake_pp)

    s3s_model_alternative_models_instance.ObjectTypes = DummyObjectTypes()
    s3s_model_alternative_models_instance.GetTimeStamps = lambda: (["TS1"], "STAT", "TS1", "TS1")

    def _model_df(element_type, properties, geometry=False, end_nodes=False):
        if element_type == "Node":
            return pd.DataFrame(
                [
                    {
                        "tk": "1",
                        "Name": "SourceNode",
                        "Zkor": "10",
                        "QmEin": "0",
                        "bz.PhEin": "0",
                        "Ktyp": "PKON",
                        "geometry": Point(0, 0),
                    },
                    {
                        "tk": "2",
                        "Name": "SinkNode",
                        "Zkor": "15",
                        "QmEin": "0",
                        "bz.PhEin": "0",
                        "Ktyp": "QKON",
                        "geometry": Point(1, 1),
                    },
                ]
            )
        return pd.DataFrame(
            [
                {
                    "tk": "10",
                    "fkKI": 1,
                    "fkKK": 2,
                    "L": "1000",
                    "Di": "100",
                    "Rau": "0.1",
                    "Name": "Pipe10",
                    "geometry": LineString([(0, 0), (1, 1)]),
                }
            ]
        )

    def _results_df(element_type, properties, timestamps):
        cols = pd.MultiIndex.from_tuples(
            [
                ("1", "SourceNode", "No end nodes on element type", "PH"),
                ("1", "SourceNode", "No end nodes on element type", "T"),
                ("1", "SourceNode", "No end nodes on element type", "QM"),
                ("2", "SinkNode", "No end nodes on element type", "PH"),
                ("2", "SinkNode", "No end nodes on element type", "T"),
                ("2", "SinkNode", "No end nodes on element type", "QM"),
            ],
            names=["tk", "name", "end_nodes", "property"],
        )
        return pd.DataFrame([[5.0, 80.0, 2.0, 4.0, 70.0, -1.5]], index=["TS1"], columns=cols)

    s3s_model_alternative_models_instance.generate_element_model_data_dataframe = _model_df
    s3s_model_alternative_models_instance.generate_element_results_dataframe = _results_df

    net = s3s_model_alternative_models_instance.SIR_3S_to_pandapipes()

    assert len(fake_pp.calls["junction"]) == 2
    assert len(fake_pp.calls["pipe"]) == 1
    assert len(fake_pp.calls["ext_grid"]) == 1
    assert len(fake_pp.calls["sink"]) == 1
    assert fake_pp.calls["pipe"][0]["from_junction"] == 0
    assert fake_pp.calls["pipe"][0]["to_junction"] == 1
    assert tuple(net.junction_geodata.loc[0, ["x", "y"]]) == (0.0, 0.0)
    assert tuple(net.junction_geodata.loc[1, ["x", "y"]]) == (1.0, 1.0)
