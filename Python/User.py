class User:
    datasets = [{}, {}]
    def __init__(self, username, password="password"):
        self.username = username
        self.password = password
# import networkx as nx
# import matplotlib
# graph = nx.Graph()  # NODES ARE EXCLUISIVE
# graph.add_node("tom")
# print(nx.nodes(graph))