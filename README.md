# Parallel-Dijkstra-Networkx

This little code was made to compute the parallel dijkstra algorithm over a graph
the main idea of this is to define sub groups of nodes such that every node in the graph
is nearer to a breaking node than to every other breaking node in the graph.

The breaking nodes can be define by the user and the algorithm makes an expansion
of all this breaking nodes to find the shortest path from every breaking node to all
all the nodes in the graph.

The code was studied from the following paper:
"The Graph Voronoi Diagram with Applications"
Martin Erwig
FernUniversitat Hagen
Praktische Informatik IV
58084 Hagen, Germany
erwig@fernuni-hagen.de

The implementation is done in python using the networkx library
