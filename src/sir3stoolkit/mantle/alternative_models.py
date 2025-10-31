# -*- coding: utf-8 -*-
"""
Created on Weg Sep 01 14:04:43 2025

This module implements the generation of SIR 3S models in alternative model formats such as pandapipes or nx-Graphs.

@author: Jablonski
"""

import pandapipes as pp
import pandas as pd
from shapely import wkt

import networkx as nx

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

from sir3stoolkit.mantle.dataframes import Dataframes_SIR3S_Model

class Alternative_Models_SIR3S_Model(Dataframes_SIR3S_Model):
    """
    This class is supposed to extend the Dataframes class that extends the general SIR3S_Model class with the possibility of using alternative District Heating models such as pandapipes.
    """
    def SIR_3S_to_pandapipes(self):
        """
        Converts the currently open SIR 3S network into a pandapipes network.

        This function creates a pandapipes network that mirrors the structure of the SIR 3S network,
        including junctions (nodes), pipes, and external sources/sinks. Only elements of type Node and Pipe
        are included; FWVB (district heating consumers) are excluded.

        Returns
        -------
        pandapipes.pandapipesNet
            A pandapipes network object containing:
            - Junctions with metadata and result values (pressure, temperature, flow).
            - Pipes with geometry and physical parameters.
            - External grids (sources) and sinks based on node type and flow direction.
        """
        net = pp.create_empty_network(fluid="water")

        # --- Nodes/Junctions ---
        df_nodes_metadata = self.generate_element_metadata_dataframe(self.ObjectTypes.Node, ['Name', 'Zkor', 'QmEin', 'bz.PhEin', 'Ktyp'], geometry=True)
        df_nodes_results = self.generate_element_results_dataframe(self.ObjectTypes.Node, ['PH', 'T', 'QM'], self.GetTimeStamps()[0])
        df_nodes = pd.merge(df_nodes_metadata, df_nodes_results, on='tk', how='inner')

        js = {}

        for idx, row in df_nodes.iterrows():
            geom = wkt.loads(row["geometry"])
            x, y = geom.x, geom.y

            j = pp.create_junction(
                net,
                pn_bar=float(row['PH']),
                tfluid_k=273.15 + float(row['T']),
                height_m=float(row['Zkor']),
                name=f"{row['Name']}~{row['tk']}"
            )

            # Assign geodata to junction_geodata table
            net.junction_geodata.at[j, "x"] = x
            net.junction_geodata.at[j, "y"] = y

            js[row['tk']] = j

        # --- Pipes ---
        df_pipes_metadata = self.generate_element_metadata_dataframe(self.ObjectTypes.Pipe, ['L', 'Di', 'Rau', 'Name'], end_nodes=True, geometry=True)
        
        for idx,row in df_pipes_metadata.iterrows():
            raw_value = row["Rau"]
            row["Rau"] = float(str(raw_value).replace(",", "."))

        ps = {}

        for idx, row in df_pipes_metadata.iterrows():
            geom = wkt.loads(row["geometry"])  
            coords = list(geom.coords)        

            # Create pipe
            p = pp.create_pipe_from_parameters(
                net,
                from_junction=js[row['fkKI']],
                to_junction=js[row['fkKK']],
                length_km=float(row['L']) / 1000.,
                diameter_m=float(row['Di']) / 1000.,
                k_mm=float(row['Rau']),
                name=f"{row['Name']}~{row['tk']}"
            )
            ps[row['tk']] = p

            net.pipe_geodata.at[p, "coords"] = coords

        # --- Source/Sinks ---
        for idx, row in df_nodes.iterrows():
            ktyp = (row.get("Ktyp"))
            tk = row.get("tk")

            # Create source if Ktyp is PKON and PH > 0
            if ktyp == "PKON" and float(row.get("PH", 0)) > 0:
                pp.create_ext_grid(
                    net,
                    junction=js[tk],
                    p_bar=float(row["PH"]),
                    t_k=273.15 + float(row["T"]),
                    name=f"Src: {row['Name']}~{tk}"
                )

            # Create sink if Ktyp is QKON and QM < 0
            elif ktyp == "QKON" and float(row.get("QM", 0)) < 0:
                pp.create_sink(
                    net,
                    junction=js[tk],
                    mdot_kg_per_s=abs(float(row["QM"])),
                    name=f"Snk: {row['Name']}~{tk}"
                )

        return net
    
    def SIR_3S_to_nx_graph(self):
        """
        Build a directed NetworkX graph from SIR 3S model.

        Parameters
        ----------

        Returns
        -------
        nx.DiGraph
            Directed graph with nodes and edges populated from SIR 3S model.
        """
        logger.info("[graph] Building nx graph...")

        # --- Nodes ---
        try:
            df_nodes = self.generate_element_metadata_dataframe(
                element_type=self.ObjectTypes.Node,
                geometry=True
            )
            logger.info(f"[graph] Retrieved {len(df_nodes)} nodes.")
        except Exception as e:
            logger.error(f"[graph] Failed to retrieve node metadata: {e}")
            return nx.DiGraph()

        # --- Edges ---
        edge_types = [
            'Pipe', 'Valve', 'SafetyValve', 'PressureRegulator', 'DifferentialRegulator',
            'FlapValve', 'PhaseSeparation', 'FlowControlUnit', 'ControlValve', 'Pump',
            'DistrictHeatingConsumer', 'DistrictHeatingFeeder', 'Compressor', 'HeaterCooler',
            'HeatExchanger', 'HeatFeederConsumerStation', 'RART_ControlMode'
        ]

        try:
            enum_members = self.__get_object_type_enums(edge_types, self.ObjectTypes)
            dfs = []
            for em in enum_members:
                df = self.generate_element_metadata_dataframe(
                    element_type=em,
                    geometry=True,
                    end_nodes=True,
                    element_type_col=True
                )
                dfs.append(df)
            df_edges = pd.concat(dfs, ignore_index=True)
            logger.info(f"[graph] Retrieved {len(df_edges)} edges from {len(enum_members)} element types.")
        except Exception as e:
            logger.error(f"[graph] Failed to retrieve edge metadata: {e}")
            return nx.DiGraph()

        # --- Build graph ---
        G = nx.DiGraph()

        # Add nodes with attributes
        logger.info("[graph] Adding nodes to graph...")
        for _, row in df_nodes.iterrows():
            try:
                attr = row.to_dict()
                attr['geometry'] = wkt.loads(row['geometry'])  # Ensure geometry is parsed
                G.add_node(row['tk'], **attr)
            except Exception as e:
                logger.warning(f"[graph] Failed to add node '{row['tk']}': {e}")

        # Add edges with attributes
        logger.info("[graph] Adding edges to graph...")
        for _, row in df_edges.iterrows():
            try:
                attr = row.to_dict()
                attr['geometry'] = wkt.loads(row['geometry'])  # Ensure geometry is parsed
                G.add_edge(row['fkKI'], row['fkKK'], **attr)
            except Exception as e:
                logger.warning(f"[graph] Failed to add edge from '{row['fkKI']}' to '{row['fkKK']}': {e}")

        logger.info(f"[graph] Graph construction complete. Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
        return G
    
    def __get_object_type_enums(self, names, enum_class):
                    return [getattr(enum_class, name) for name in names if hasattr(enum_class, name)]