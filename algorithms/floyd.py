from implementations.adj_matrix_weighted import WeightedAdjacencyMatrixGraph


def floyd_warshall(graph):
    dist = {}
    next_vertex = {}

    for v in graph.vertex_list:
        dist[v] = {}
        next_vertex[v] = {}
        for u in graph.vertex_list:
            if v == u:
                dist[v][u] = 0
            elif graph.exists_edge(v, u):
                dist[v][u] = graph.adjacency_matrix[graph.vertex_list.index(v)][graph.vertex_list.index(u)]
                next_vertex[v][u] = u
            else:
                dist[v][u] = float('inf')
                next_vertex[v][u] = None

    for k in graph.vertex_list:
        for i in graph.vertex_list:
            for j in graph.vertex_list:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex

g = WeightedAdjacencyMatrixGraph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 5)
g.add_edge('D', 'E', 1)

distancias, next_vertex = floyd_warshall(g)

for v in distancias.keys():
    print(v, distancias[v], next_vertex[v])