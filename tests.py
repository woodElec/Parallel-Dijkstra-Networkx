import networkx as nx
import voronoi_module as vor

G = nx.Graph()

e = [(0, 1, 4), (2, 5, 4), (0, 7, 8), (3, 5, 14), (1, 2, 8), (3, 4, 9), (1, 7, 11), (4, 5, 10), (2, 8, 2),
     (5, 6, 2), (2, 3, 7), (6, 8, 6), (6, 7, 1), (7, 8, 7), (9, 0, 6), (10, 3, 1), (10, 4, 1), (11, 12, 1),
     (12, 13, 1), (11, 13, 1), (11, 3, 20), (13, 3, 20)]

#e = [(1, 2, 1), (2, 3, 1), (4, 2, 1), (4, 5, 1)]

G.add_weighted_edges_from(e)
pos = nx.spring_layout(G)
