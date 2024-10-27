from implementations.adj_matrix import AdjacencyMatrixGraph


def warshall(graph):
    n = graph.order()
    transitive_closure = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph.exists_edge(graph.vertex_list[i], graph.vertex_list[j]):
                transitive_closure[i][j] = True

    for k in range(n):
        for i in range(n):
            for j in range(n):
                transitive_closure[i][j] = transitive_closure[i][j] or (
                            transitive_closure[i][k] and transitive_closure[k][j])

    return transitive_closure


if __name__ == "__main__":
    g = AdjacencyMatrixGraph(directed=True)
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    closure = warshall(g)

    print("Transitive Closure:")
    for row in closure:
        print(row)

    g = AdjacencyMatrixGraph(directed=True)

    for vertex in ['A', 'B', 'C', 'D', 'E']:
        g.add_vertex(vertex)

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    closure = warshall(g)

    print("Transitive Closure:")
    for row in closure:
        print(row)
