import networkx as nx
import matplotlib
import os.path
graph = nx.Graph()  # NODES ARE EXCLUISIVE

graph.add_node("tom")
print(nx.nodes(graph))

def save_to_file(filename="demofile"):
    save_path = 'GraphTheory'
    completeName = os.path.join(save_path, filename + ".csv")