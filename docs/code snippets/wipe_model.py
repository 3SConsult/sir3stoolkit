from sir3stoolkit.core import wrapper
wrapper.Initialize_Toolkit()
s3s = wrapper.SIR3S_Model()

object_types = [item for item in dir(s3s.ObjectTypes) if not (item.startswith('__') and item.endswith('__'))]
object_types = ["Node", "Pipe"] # Limit, otherwise model becomes unusable
for obj_type in object_types:
    tks = s3s.GetTksofElementType(s3s.ObjectTypes[obj_type])
    for tk in tks:
        s3s.DeleteElement(Tk=tk)