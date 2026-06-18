# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24, 2026

@author: Nischal Giriyan
"""

import clr as net
import os
import System
import enum
import wrapper
import networkx as nx
import matplotlib.pyplot as plt
from System.Reflection import Assembly
from shapely import wkt
from wrapper import SIR3S_Model

##########################################
# This Graph class can be used in 4 different combination of scenarios
# 1. In the context of SirGraf
#    a. With graph from an existing model
#    b. With new empty graph
# 2. In the context outside SirGraf(Like Jupyter notebook) 
#    c. With graph from an existing model
#    d. With new empty graph 


##########################################
class Graph_Model(SIR3S_Model):
    """
    Class definition of Graph_Model() wrapper to access functionalities provided by SIR3S software.
    This can be used independently or by using inside python console plugin to give better control
    over the graph of the object model for the users.
    """
    
    def __init__(self):
        
        # --- Runs init from SIR3S_Model ---
        super().__init__()
        
        # --- Additional setup specific to Graph_Model ---
        self.GraphCalcMode = wrapper.create_dotnet_enum("GraphCalcMode", "GraphCalcMode", "Sir3S_Repository.Interfaces.dll")
        
        self._dotnet_enum_type_GraphCalcMode = self._load_dotnet_enum("GraphCalcMode", "Sir3S_Repository.Interfaces.dll")

        # Create a registry of enums so that enums in parent class are also available through this class
        self._enum_map = {
        self.GraphCalcMode: self._dotnet_enum_type_GraphCalcMode,
    }
        
        if hasattr(self, "ObjectTypes"):
            self._enum_map[self.ObjectTypes] = self._load_dotnet_enum(
                "Sir3SObjectTypes", "Sir3S_Repository.Interfaces.dll"
            )
        
    def to_dotnet_enum(self, py_enum_member):
        # Extract the type of Enum
        enum_type = type(py_enum_member)
        
        # Check if it's an Enum member
        if not isinstance(py_enum_member, enum.Enum):
            raise TypeError(f"Expected Enum member, got {enum_type}")

        # Use the integer value of Python enum member to create .NET enum
        if enum_type in self._enum_map:
            return System.Enum.ToObject(
                self._enum_map[enum_type],
                py_enum_member.value
            )

        raise TypeError(f"Unknown enum type {enum_type}")
    
    def GetGraphFromObjectModel(self, clone:bool):
        """
        Fetches graph from the object model that is already open

        :param clone: Boolean parameter to understand whether to clone the graph before returning or give direct access to graph; Default value is True(to be cloned)
        :type clone: bool
        :return: Returns an Graph object of type IGraphOM
        :rtype: IGraphOM
        :description: This is a wrapper method for GetGraphFromObjectModel() from toolkit.
        """
        self.graph = self.toolkit.GetGraphFromObjectModel(clone)
        return self.graph
        
    def CreateNewGraph(self):
        """
        Creates a new empty graph

        :return: Returns an Graph object of type IGraphOM
        :rtype: IGraphOM
        :description: This is a wrapper method for CreateNewGraph() from toolkit.
        """
        self.graph = self.toolkit.CreateNewGraph()
        
    def CreateDecompositionParameters(self):
        """
        Creates a decomposition parameter for executing graph algorithms

        :return: Returns an decomposition parameters object of type decomposition_parameters_t
        :rtype: decomposition_parameters_t
        :description: This is a wrapper method for CreateDecompositionParameters() from toolkit.
        """
        decomp = self.toolkit.CreateDecompositionParameters()
        return decomp    

    def ExecuteAlgorithm(self, decomp, option):
        """
        This function executes graph algorithm as per the parameters set in decomposition object

        :param decomp: Decomposition parameters
        :type decomp: decomposition_parameters_t
        :param option: Object to inform which algorithm to execute(object type GraphCalcMode)
        :type option: GraphCalcMode
        :return: Returns an integer to indicate status of ExecuteAlgorithm()
        :rtype: int
        :description: This is a wrapper method for ExecuteAlgorithm() from toolkit.
        """
        if (self.graph is not None):
            GraphCalcMode_net = self.to_dotnet_enum(option)
            ret_value = self.toolkit.ExecuteAlgorithm(self.graph, decomp, GraphCalcMode_net)
        else:
            print("Graph is not set to execute algorithm")
            ret_value = -1

        return ret_value
    
    def AddNewGraphNode(self, name, GraphNode_type, kvr, iCont, weight):
        """
        This function adds a new node to the graph object

        :param name: Graph node name
        :type name: str
        :param GraphNode_type: Graph node type
        :type GraphNode_type: GraphNodeType
        :param kvr: SL/RL Flag. Should be 0 (undefined), 1 (SL) or 2 (RL)
        :type kvr: int
        :param iCont: iCont integer value
        :type iCont: int
        :param weight: Weight of the node
        :type weight: np.float64
        :return: Returns an integer to indicate status of AddNewGraphNode()
        :rtype: int
        :description: This is a wrapper method for AddNewGraphNode() from toolkit.
        """
        if (self.graph is not None):
            ret_value = self.toolkit.AddNewGraphNode(self.graph, name, GraphNode_type, kvr, iCont, weight)
        else:
            print("Graph is not valid to add any new node")
            ret_value = -1
        
        return ret_value
    
    def AddNewGraphLink(self, name, from_node, to_node, GraphLink_type, kvr, iCont, weight, status):
        """
        This function adds a new link to the graph object

        :param name: Graph link name
        :type name: str
        :param from_node: From node name of the link
        :type from_node: str
        :param to_node: To node name of the link
        :type to_node: str
        :param GraphLink_type: Graph link type
        :type GraphLink_type: GraphLinkType
        :param kvr: SL/RL Flag. Should be 0 (undefined), 1 (SL) or 2 (RL)
        :type kvr: int
        :param iCont: iCont integer value
        :type iCont: int
        :param weight: Weight of the link
        :type weight: np.float64
        :param status: Status of the function
        :type status: int
        :return: Returns an integer to indicate status of AddNewGraphLink()
        :rtype: int
        :description: This is a wrapper method for AddNewGraphLink() from toolkit.
        """
        if (self.graph is not None):
            ret_value = self.toolkit.AddNewGraphLink(self.graph, name, from_node, to_node, GraphLink_type, kvr, iCont, weight, status)
        else:
            print("Graph is not valid to add any new link")
            ret_value = -1
        
        return ret_value
    
    def DeleteGraphNode(self, node):
        """
        This function deletes a node from the graph object

        :param node: Node to be deleted
        :type node: ISNode
        :return: None
        :rtype: None
        :description: This is a wrapper method for DeleteGraphNode() from toolkit.
        """
        if (self.graph is not None):
            self.toolkit.DeleteGraphNode(self.graph, node)
        else:
            print("Graph is not valid to delete the node")
            
    def DeleteGraphLink(self, link):
        """
        This function deletes a link from the graph object

        :param link: Link to be deleted
        :type link: ISLink
        :return: None
        :rtype: None
        :description: This is a wrapper method for DeleteGraphLink() from toolkit.
        """
        if (self.graph is not None):
            self.toolkit.DeleteGraphLink(self.graph, link)
        else:
            print("Graph is not valid to delete the link")
        
    def GetMinimumSpanningITree(self):
        """
        This function executes minimum spanning tree algorithm on the graph

        :return: Returns minimum spanning tree of object type ITree
        :rtype: ITree
        :description: This is a wrapper method for GetMinimumSpanningITree() from toolkit.
        """
        if (self.graph is not None):
            tree = self.toolkit.GetMinimumSpanningITree(self.graph)
        else:
            print("Graph is not valid to calculate minimum spanning ITree")
            tree = None
            
        return tree
    
    def GetNumOfComponents(self):
        """
        This function calculates and returns number of components in the graph object

        :return: Returns number of components in the graph object
        :rtype: int
        :description: This is a wrapper method for GetNumOfComponents() from toolkit.
        """
        if (self.graph is not None):
            comp = self.toolkit.GetNumOfComponents(self.graph)
        else:
            print("Graph is not valid to fetch number of components")
            comp = -1
            
        return comp

    def Visualize_graph(self, show_ids=False, edge_color="gray", node_color="red"):
        """
        This function draws the graph network using matplotlib.pyplot

        :param show_ids: True if user wants the Tk of Node and Link to be displayed on top of them for reference. This might clutter the visualization; Default value is False
        :type show_ids: bool
        :param edge_color: Color in which links/edges to be represented in the plot; Default is Gray
        :type edge_color: str
        :param node_color: Color in which nodes to be represented in the plot; Default is Red
        :type node_color: str
        :return: Returns True if able to successfully visulize the graph, False otherwise
        :rtype: bool
        :description: This functon only exists in Python and not in .NET; This helps in quick visualization of the graph with their geometric properties
        """
        if self.graph is None:
            print("Graph is empty, nothing to visualize")
            return False
        
        data = self.toolkit.ExportGraph(self.graph)
        
        fig, ax = plt.subplots(figsize=(12, 10))
        
        # draw edges
        for edge in data.Edges:
            edge_id = edge.Item1
            from_id = edge.Item2
            to_id = edge.Item3
            weight = edge.Item4
            
            wkt_string_edge = self.GetGeometryInformation(edge_id)
            
            edge_geom = self.safe_load_wkt(wkt_string_edge)
            if edge_geom is None or edge_geom.is_empty:
                continue
            
            if edge_geom.geom_type == "LineString":
                x, y = edge_geom.xy
                ax.plot(x, y, linewidth=1.2, color=edge_color)
                
        # draw nodes
        for node_id in data.Nodes:
            wkt_string_node = self.GetGeometryInformation(node_id)
            node_geom = self.safe_load_wkt(wkt_string_node)    
            
            if node_geom is None or node_geom.is_empty:
                continue
        
            if node_geom.geom_type == "Point":
                ax.scatter(node_geom.x, node_geom.y, s=5, color=node_color, zorder=3)
                
                if show_ids:
                    ax.text(node_geom.x, node_geom.y, node_id, fontsize=8)
                    
        ax.set_title("Water Network (Real Geometry from WKT)")
        ax.set_aspect("equal")
        ax.grid(True)
        plt.tight_layout()
        plt.show()

        return True
    
    def export_Graph_Data(self):
        """
        Exports graph data(node and links) of existing graph under this class instance; This is helpful mainly for visualization

        :return: Returns graph data
        :rtype: GraphData
        :description: This is a wrapper method for ExportGraph() from toolkit.
        """
        if self.graph is None:
            print("Graph is empty, nothing to export")
            return None
        
        data = self.toolkit.ExportGraph(self.graph)
        return data

    def safe_load_wkt(self, wkt_string):
        """
        This function helps safe loading of geometry from a WKT string

        :param wkt_string: WKT string
        :type wkt_string: str
        :return: Returns geometry object if everything is okay, otherwise None
        :rtype: Geometry object
        :description: This is a helper function at Python level for visualization
        """
        if wkt_string is None:
            return None

        if not isinstance(wkt_string, str):
            return None

        wkt_string = wkt_string.strip()

        if wkt_string == "":
            return None

        try:
            return wkt.loads(wkt_string)
        except Exception:
            return None