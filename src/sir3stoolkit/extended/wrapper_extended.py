# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 17:34:49 2025

@author: Jablonski
"""

from sir3stoolkit.core.wrapper import SIR3S_Model

import pandas as pd
import sys
import logging

logger = logging.getLogger(__name__)

class ExtendedSIR3S_Model(SIR3S_Model):
    def insert_dfPipes(self, dfPipes):
        """
        Takes a dataframe with each row representing one pipe and adds it to the model.
        The dataframe needs minimum of cols: geometry (LINESTRING), MATERIAL (str), DN (int), KVR (int)
        """
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")

        climbing_index = 0
        for idx in range(len(dfPipes)):
            dfPipes.at[idx, 'nodeKI_id'] = climbing_index
            dfPipes.at[idx, 'nodeKK_id'] = climbing_index + 1
            climbing_index += 2

        self.StartEditSession(SessionName="AddNodesAndPipes")

        def AddNodesAndPipes(dfXL, node_counter):
            supplementary_nodes = pd.DataFrame(columns=['id', 'tk', 'x', 'y'])
            for i in range(len(dfXL)):
                nodeKI_id = dfXL.loc[i, 'nodeKI_id']
                if nodeKI_id not in supplementary_nodes['id'].values:
                    x_ki, y_ki = dfXL.loc[i, 'geometry'].coords[0]
                    tk_ki = self.AddNewNode("-1", f"Node{i}KI {self.VL_or_RL(int(dfXL.loc[i, 'KVR']))}", f"Node{i}", x_ki, y_ki, 1.0, 0.1, 2.0, f"Node{i}KI", f'ID{node_counter}', int(dfXL.loc[i, 'KVR']))
                    supplementary_nodes.loc[len(supplementary_nodes)] = [nodeKI_id, tk_ki, x_ki, y_ki]
                    dfXL.loc[i, 'nodeKI'] = tk_ki
                    node_counter += 1
                else:
                    tk_ki = supplementary_nodes.loc[supplementary_nodes['id'] == nodeKI_id, 'tk'].values[0]
                    dfXL.loc[i, 'nodeKI'] = tk_ki

                nodeKK_id = dfXL.loc[i, 'nodeKK_id']
                if nodeKK_id not in supplementary_nodes['id'].values:
                    x_kk, y_kk = dfXL.loc[i, 'geometry'].coords[-1]
                    tk_kk = self.AddNewNode("-1", f"Node{i}KK {self.VL_or_RL(int(dfXL.loc[i, 'KVR']))}", f"Node{i}", x_kk, y_kk, 1.0, 0.1, 2.0, f"Node{i}KK", f'ID{node_counter}', int(dfXL.loc[i, 'KVR']))
                    supplementary_nodes.loc[len(supplementary_nodes)] = [nodeKK_id, tk_kk, x_kk, y_kk]
                    dfXL.loc[i, 'nodeKK'] = tk_kk
                    node_counter += 1
                else:
                    tk_kk = supplementary_nodes.loc[supplementary_nodes['id'] == nodeKK_id, 'tk'].values[0]
                    dfXL.loc[i, 'nodeKK'] = tk_kk

                tk_pipe = self.AddNewPipe("-1", tk_ki, tk_kk, dfXL.loc[i, 'geometry'].length, str(dfXL.loc[i, 'geometry']), str(dfXL.loc[i, 'MATERIAL']), str(dfXL.loc[i, 'DN']), 1.5, f'ID{i}', f'Pipe {i}', int(dfXL.loc[i, 'KVR']))
                dfXL.loc[i, 'tk'] = tk_pipe

            return dfXL, supplementary_nodes, node_counter

        dfPipes['KVR'] = dfPipes['KVR'].astype(str).str.strip()
        dfVL = dfPipes[dfPipes['KVR'] == '1'].reset_index(drop=True)
        dfRL = dfPipes[dfPipes['KVR'] == '2'].reset_index(drop=True)

        dfVL, dfVL_nodes, node_counter_VL = AddNodesAndPipes(dfVL, 0)
        dfRL, dfRL_nodes, node_counter_RL = AddNodesAndPipes(dfRL, node_counter_VL)

        dfPipes = pd.concat([dfVL, dfRL], ignore_index=True)
        dfNodes = pd.concat([dfVL_nodes, dfRL_nodes], ignore_index=True)

        if '2LROHR' not in dfPipes.columns:
            dfPipes['2LROHR'] = None

        if 'BAUJAHR' in dfPipes.columns:
            try:
                self.SetValue('Baujahr', str(dfPipes.loc[i, 'BAUJAHR']))
            except:
                logger.debug("Baujahr not added as property")

        if 'HAL' in dfPipes.columns:
            try:
                self.SetValue('Hal', str(dfPipes.loc[i, 'HAL']))
            except:
                logger.debug("Hal not added as property")

        self.EndEditSession()
        self.SaveChanges()
        self.RefreshViews()

        return dfPipes, dfNodes, node_counter_VL + node_counter_RL

    def Node_on_Node(self):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")
        # Implementation goes here

    def Merge_Nodes(self, tk1, tk2):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")
        # Implementation goes here

    def Get_Node_Tks_From_Pipe(self, pipe_tk):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")

        from_node_name = self.GetValue(pipe_tk, 'FromNode.Name')[0]
        to_node_name = self.GetValue(pipe_tk, 'ToNode.Name')[0]

        from_node_tk = None
        to_node_tk = None

        for node_tk in self.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Node):
            node_name = self.GetValue(node_tk, 'Name')[0]
            if node_name == from_node_name:
                from_node_tk = node_tk
            if node_name == to_node_name:
                to_node_tk = node_tk

        return from_node_tk, to_node_tk

    def Get_Pipe_Tk_From_Nodes(self, fkKI, fkKK, Order=True):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")

        from_node_name = self.GetValue(fkKI, 'Name')[0]
        to_node_name = self.GetValue(fkKK, 'Name')[0]

        pipe_tk_ret = None

        if Order:
            for pipe_tk in self.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Pipe):
                if (self.GetValue(pipe_tk, 'FromNode.Name')[0] == from_node_name and 
                    self.GetValue(pipe_tk, 'ToNode.Name')[0] == to_node_name):
                    pipe_tk_ret = pipe_tk
                    break
        else:
            for pipe_tk in self.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Pipe):
                from_name = self.GetValue(pipe_tk, 'FromNode.Name')[0]
                to_name = self.GetValue(pipe_tk, 'ToNode.Name')[0]
                if ((from_name == from_node_name and to_name == to_node_name) or 
                    (from_name == to_node_name and to_name == from_node_name)):
                    pipe_tk_ret = pipe_tk
                    break

        return pipe_tk_ret

    def VL_or_RL(self, KVR):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")
        if KVR == 1:
            return 'VL'
        elif KVR == 2:
            return 'RL'
        else:
            return 'Unknown'

    def Check_Node_Name_Duplicates(self, name):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")

        tks = []
        for node_tk in self.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Node):
            current_name = self.GetValue(node_tk, 'Name')[0]
            if current_name == name:
                tks.append(node_tk)

        if len(tks) == 1:
            print(f'Only the node with tk {tks[0]} has the name {name}')
        else:
            print(f'The nodes of the following tks have the same name ({name}):')
            for tk in tks:
                print(f'{tk}')

        return tks

    def Resolve_Node_Name_Duplicates(self):
        func_name = sys._getframe().f_code.co_name
        logger.debug(f"{func_name}: Start.")
        logger.info(f"{func_name}: Not implemented")
        pass
