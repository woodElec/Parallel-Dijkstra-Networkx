import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time
import random
import heapq

G = nx.Graph()
G.add_nodes_from(range(0, 9))
pos = nx.spring_layout(G)

e = np.array([[0, 1, 4], [2, 5, 4], [0, 7, 8], [3, 5, 14], [1, 2, 8], [3, 4, 9], [1, 7, 11], [4, 5, 10], [2, 8, 2],
               [5, 6, 2], [2, 3, 7], [6, 8, 6], [6, 7, 1], [7, 8, 7]])
K = [0, 8, 4]

G.add_weighted_edges_from(e)

# **********************************************************
# ************* Start of The Algorithm *********************
# **********************************************************

# Assing the attributes to each node in the graph
nx.set_node_attributes(G, 'Dv', 1000)
nx.set_node_attributes(G, 'V', 'N')
nx.set_node_attributes(G, 'visit', 0)

start = time.time()
i = 0                    # Identify the Voronoi Nodes
Q = []
while i < len(K):
     if K[i] in G:
          G.node[K[i]]['Dv'] = 0
          G.node[K[i]]['V'] = 'V'+str(i)
          heapq.heappush(Q, (0, K[i]))
          i += 1

# Node Expansion: First find the lowest value and check not visited node
t = 0
while len(Q) != 0:
     v = heapq.heappop(Q)
     print(v[1])
     G.node[v[1]]['visit'] = 1        # Mark the node as visited

     # Visit all the neigbors of the node to be expanded
     for nbr in G.neighbors(v[1]):
          if G.node[nbr]['visit'] == 0:
               delta = G.node[v[1]]['Dv'] + (G.get_edge_data(v[1], nbr))['weight']

               if G.node[nbr]['Dv'] == 1000:
                    G.node[nbr]['Dv'] = delta
                    G.node[nbr]['V'] = G.node[v[1]]['V']
                    heapq.heappush(Q, (delta, nbr))

               if (G.node[nbr]['Dv'] < 1000) and (delta < G.node[nbr]['Dv']):
                    G.node[nbr]['V'] = G.node[v[1]]['V']
                    G.node[nbr]['Dv'] = delta

print("--- %s seconds ---" % (time.time() - start))
print(nx.get_node_attributes(G, 'V'))
nx.draw(G)
plt.show()