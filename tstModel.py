from model.model import Model

m = Model()
m.buildGraph(500)

print(f"num nodi {m.getNumNodes()}")
print(f"num archi {m.getNumEdges()}")