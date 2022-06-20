import networkx as nx
import matplotlib

graph = nx.Graph()  # NODES ARE EXCLUISIVE

graph.add_node("tom")
print(nx.nodes(graph))
