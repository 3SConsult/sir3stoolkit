# Node - Pipe - Node - Valve - Node
s3s.OpenModel(dbName=r"Toolkit_Tutorial55_Model.db3",
              providerType=s3s.ProviderTypes.SQLite,
              Mid="M-1-0-1",
              saveCurrentlyOpenModel=False,
              namedInstance="",
              userID="",
              password="")
node1 = s3s.AddNewNode(tkCont=s3s.GetMainContainer()[0], name="NODE01", typ="PKON", x=0, y=0, z=0, qm_PH=5, symbolFactor=1, description="Upstream of valve", idRef="1", kvr=1)
node2 = s3s.AddNewNode(tkCont=s3s.GetMainContainer()[0], name="NODE02", typ="QKON", x=40, y=0, z=0, qm_PH=0, symbolFactor=1, description="Upstream of valve", idRef="2", kvr=1)
node3 = s3s.AddNewNode(tkCont=s3s.GetMainContainer()[0], name="NODE03", typ="QKON", x=80, y=0, z=0, qm_PH=-4, symbolFactor=1, description="Downstream of valve", idRef="3", kvr=1)
pipe = s3s.AddNewPipe(tkCont=s3s.GetMainContainer()[0], tkFrom=node1, tkTo=node2, L=10, linestring="LINESTRING(0 0, 40, 0)", material="STDROHR", dn="32", roughness=0.25, idRef="3", description="Pipe from node 1 to node 2", kvr=1)
valve = s3s.AddNewConnectingElement(tkCont=s3s.GetMainContainer()[0], tkFrom=node2, tkTo=node3, x=60, y=0, z=0, elementType=s3s.ObjectTypes.Valve, dn=32, symbolFactor=1, angleDegree=0, idRef="4", description="control valve")
# SIR3S_View: valve = s3s.AddNewValveOnPipe(tkPipe=pipe, iSymbolType=3, position=0.5, name="Valve", description="control valve", isPostureStatic=s3s.NetValvePostures.STATIC_OPEN_CLOSE, openClose="True", idRef="4")
s3s.SetValue(Tk=valve, propertyName="bz.Phio", Value="100") # If open: 100%
s3s.SetValue(Tk=valve, propertyName="bz.Phig", Value="0") # If closed: 0%
s3s.CloseModel(True)