from implementations.adj_list import AdjacencyListGraph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Procesar el nodo (por ejemplo, imprimirlo)

    for neighbor in graph.get_adjacency_list(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)  # Procesar el nodo (por ejemplo, imprimirlo)

        for neighbor in graph.get_adjacency_list(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Ejemplo de uso:
g = AdjacencyListGraph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

dfs(g, 'A')
bfs(g, 'A')
