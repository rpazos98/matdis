import heapq

from implementations.adj_matrix_weighted import WeightedAdjacencyMatrixGraph


def dijkstra(graph, start):
    dist = {v: float('inf') for v in (graph.vertex_list)}
    dist[start] = 0

    prev = {v: None for v in (graph.vertex_list)}

    priority_queue = [(0, start)]  # (distancia, nodo)

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph.get_adjacency_list(current_node):
            alternative_dist = current_dist + weight

            if alternative_dist < dist[neighbor]:
                dist[neighbor] = alternative_dist
                prev[neighbor] = current_node
                heapq.heappush(priority_queue, (alternative_dist, neighbor))

    return dist, prev


g = WeightedAdjacencyMatrixGraph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)

g.add_edge(1,5, 100)
g.add_edge(1,2, 10)
g.add_edge(2,3, 50)
g.add_edge(3,4, 20)
g.add_edge(1,4, 30)
g.add_edge(3,5, 10)
g.add_edge(4,5, 50)

distancias, caminos = dijkstra(g, 1)

print("Distancias más cortas desde A:")
print(distancias)

print("Nodo previo en el camino optimo:")
for nodo, camino in caminos.items():
    print(f"{nodo}: {camino}")
