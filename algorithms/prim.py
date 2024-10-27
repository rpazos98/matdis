import heapq

from implementations.adj_matrix_weighted import WeightedAdjacencyMatrixGraph
from implementations.weighted_graph import WeightedGraph


def prim_algorithm(graph: WeightedGraph, start_vertex):
    mst_edges = []
    visited = set()
    min_heap = []

    visited.add(start_vertex)
    for neighbor, weight in graph.get_adjacency_list(start_vertex):
        heapq.heappush(min_heap, (weight, start_vertex, neighbor))

    while min_heap and len(visited) < graph.order():
        weight, u, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        mst_edges.append((u, v, weight))
        visited.add(v)

        for neighbor, edge_weight in graph.get_adjacency_list(v):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return mst_edges


graph = WeightedAdjacencyMatrixGraph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 3)

mst = prim_algorithm(graph, 'A')

print("Árbol de Expansión Mínima:")
for u, v, weight in mst:
    print(f"{u} - {v} (peso: {weight})")