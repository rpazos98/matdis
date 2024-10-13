import copy

from implementations.adj_matrix import AdjacencyMatrixGraph


def show_graph(graph: AdjacencyMatrixGraph):
    edge_list = []
    matrix_size = len(graph.adjacency_matrix)
    for i in range(matrix_size):
        for j in range(i, matrix_size):
            i_to_j = graph.adjacency_matrix[i][j]
            if i_to_j:
                edge_list.append((graph.vertex_list[i], graph.vertex_list[j]))
    return f"Graph: Vertex List: {graph.vertex_list} Edge List: {edge_list}"


def calc_lassos(graph: AdjacencyMatrixGraph):
    result = 0
    for i in range(len(graph.vertex_list)):
        if graph.adjacency_matrix[i][i]:
            result += 1
    return result


def calc_lassos(graph: AdjacencyMatrixGraph):
    result = 0
    for i in range(len(graph.vertex_list)):
        if graph.adjacency_matrix[i][i]:
            result += 1
    return result


def get_vertices_lassos(graph: AdjacencyMatrixGraph):
    result = []
    for i in range(len(graph.vertex_list)):
        if graph.adjacency_matrix[i][i]:
            result.append(graph.vertex_list[i])
    return result


def is_isolated(vertex, graph: AdjacencyMatrixGraph):
    idx = graph.vertex_list.index(vertex)
    row = graph.adjacency_matrix[idx]
    return not any(row)


def calc_isolated(graph: AdjacencyMatrixGraph):
    result = 0
    for i in range(len(graph.vertex_list)):
        row = graph.adjacency_matrix[i]
        if not any(row):
            result += 1
    return result


def get_isolated(graph: AdjacencyMatrixGraph):
    result = []
    for i in range(len(graph.vertex_list)):
        row = graph.adjacency_matrix[i]
        if not any(row):
            result.append(graph.vertex_list[i])
    return result


def remove_lassos_and_isolated_vertices(graph: AdjacencyMatrixGraph):
    g2 = copy.deepcopy(graph)
    for i in range(len(g2.vertex_list)):
        g2.adjacency_matrix[i][i] = False
    remove_vertices = []
    for i in range(len(g2.vertex_list)):
        row = graph.adjacency_matrix[i]
        if not any(row):
            remove_vertices.append(g2.vertex_list[i])
    for remove_vertex in remove_vertices:
        g2.delete_vertex(remove_vertex)
    return g2


if __name__ == "__main__":
    graph = AdjacencyMatrixGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "A")
    graph.add_edge("B", "B")
    graph.add_edge("A", "B")

    print(show_graph(graph))
    print(calc_lassos(graph))
    print(get_vertices_lassos(graph))
    print(is_isolated("A", graph))
    print(is_isolated("C", graph))
    print(calc_isolated(graph))
    print(get_isolated(graph))
    print(show_graph(remove_lassos_and_isolated_vertices(graph)))
