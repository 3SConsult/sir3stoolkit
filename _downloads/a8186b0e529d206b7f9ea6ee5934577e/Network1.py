from sir3stoolkit.core import wrapper

SIR3S_SIRGRAF_DIR = r"C:\3S\SIR 3S Entwicklung\SirGraf-90-15-00-16_Quebec_x64"  # change to local path
wrapper.Initialize_Toolkit(SIR3S_SIRGRAF_DIR)

model = wrapper.SIR3S_Model()

# Abbreviations for ObjectTypes used
TNode = model.ObjectTypes.Node
TPipe = model.ObjectTypes.Pipe
TPump = model.ObjectTypes.Pump
TTank = model.ObjectTypes.OpenContainer

# Create Nodes and Pipes
model.StartEditSession("Insert Elements")

# Add nodes
node10 = model.AddNewNode("-1", "Node10", "QKON", 200, 700, 213, 0, 1, "DNODE 10", "RefNode 10", 0) 
node11 = model.AddNewNode("-1", "Node11", "QKON", 300, 700, 213, 0, 1, "DNODE 11", "RefNode 11", 0) 
node12 = model.AddNewNode("-1", "Node12", "QKON", 500, 700, 210, 0, 1, "DNODE 12", "RefNode 12", 0) 
node13 = model.AddNewNode("-1", "Node13", "QKON", 700, 700, 208.5, 0, 1, "DNODE 13", "RefNode 13", 0) 
node21 = model.AddNewNode("-1", "Node21", "QKON", 300, 400, 210, 0, 1, "DNODE 21", "RefNode 21", 0) 
node22 = model.AddNewNode("-1", "Node22", "QKON", 500, 400, 208.5, 0, 1, "DNODE 22", "RefNode 22", 0) 
node23 = model.AddNewNode("-1", "Node23", "QKON", 700, 400, 207, 0, 1, "DNODE 23", "RefNode 23", 0) 
node31 = model.AddNewNode("-1", "Node31", "QKON", 300, 100, 210, 0, 1, "DNODE 31", "RefNode 31", 0) 
node32 = model.AddNewNode("-1", "Node32", "QKON", 500, 100, 213, 0, 1, "DNODE 32", "RefNode 32", 0) 
node9 = model.AddNewNode("-1", "Node9", "PKON", 150, 700, 255, 0, 1, "PNODE 9", "RefNode 9", 0) 
node2 = model.AddNewNode("-1", "Node2", "QKON", 500, 850, 240, 0, 1, "Tank 2", "RefNode 2", 0) 

# Add pipes
model.AddNewPipe("-1", node10, node11, 3160, "LINESTRING(200 700, 300, 700)", "STDROHR", "450", 0.25, "Ref Pipe 10", "Pipe from Pump to network", 0)
model.AddNewPipe("-1", node11, node12, 1584, "LINESTRING(300 700, 500, 700)", "STDROHR", "350", 0.25, "Ref Pipe 11", "Pipe from 11 to 12", 0)
model.AddNewPipe("-1", node12, node13, 1584, "LINESTRING(500 700, 700, 700)", "STDROHR", "250", 0.25, "Ref Pipe 12", "Pipe from 12 to 13", 0)
model.AddNewPipe("-1", node21, node22, 1584, "LINESTRING(300 400, 500, 400)", "STDROHR", "250", 0.25, "Ref Pipe 21", "Pipe from 21 to 22", 0)
model.AddNewPipe("-1", node22, node23, 1584, "LINESTRING(500 400, 700, 400)", "STDROHR", "300", 0.25, "Ref Pipe 22", "Pipe from 22 to 23", 0)
model.AddNewPipe("-1", node31, node32, 1584, "LINESTRING(300 100, 500, 100)", "STDROHR", "150", 0.25, "Ref Pipe 31", "Pipe from 31 to 32", 0)
model.AddNewPipe("-1", node2, node12,  60, "LINESTRING(500 850, 500, 700)", "STDROHR", "450", 0.25, "Ref Pipe 110", "Pipe from Tank to network", 0)
model.AddNewPipe("-1", node11, node21, 1584, "LINESTRING(300 700, 300, 400)", "STDROHR", "250", 0.25, "Ref Pipee 111", "Pipe from 11 to 21", 0)
model.AddNewPipe("-1", node12, node22, 1584, "LINESTRING(500 700, 500, 400)", "STDROHR", "300", 0.25, "Ref Pipee 112", "Pipe from 12 to 22", 0)
model.AddNewPipe("-1", node13, node23, 1584, "LINESTRING(700 700, 700, 400)", "STDROHR", "200", 0.25, "Ref Pipee 113", "Pipe from 13 to 32", 0)
model.AddNewPipe("-1", node21, node31, 1584, "LINESTRING(300 400, 300, 100)", "STDROHR", "200", 0.25, "Ref Pipee 121", "Pipe from 21 to 31", 0)
model.AddNewPipe("-1", node22, node32, 1584, "LINESTRING(500 400, 500, 100)", "STDROHR", "150", 0.25, "Ref Pipee 122", "Pipe from 22 to 32", 0)

# Add pump
model.AddNewConnectingElement("-1", node9, node10, 175, 700, 0, TPump, 200, 1, 0, "Pumpe", "standard pump")

#add tank
model.AddNewBypassElement("-1", node2, 500, 850, 255, 1, TTank, "Tank", "Storage tank")

#Stop edit sesssion
model.EndEditSession();

#Add text
text = model.InsertElement(model.ObjectTypes.Text, "RefBspText")
model.SetGeometryInformation(text, "POINT(750 850 0)")
model.SetValue(text, "Graftext", "Network 1 createed by SIR 3S PythonToolkit")
model.SetElementColor_RGB(text, 255,0,0,True)       

# draw network in map
model.RefreshViews()                              

# run steady-state calculation
model.ExecCalculation(True);                      