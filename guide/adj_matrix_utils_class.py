import copy

from guide.adj_matrix import AdjacencyMatrixGraph


def show_matrix(x: AdjacencyMatrixGraph):
    aristas = []

    for i in range(len(x.vertex_list)):
        for j in range(i, len(x.vertex_list)):

            if x.adjacency_matrix[i][j]:
                aristas.append((x.vertex_list[i], x.vertex_list[j]))

    return f"La lista de vertices es {x.vertex_list} y la lista de aristas es {aristas}"


def count_lassos(x: AdjacencyMatrixGraph):
    counter = 0
    for i in range(len(x.vertex_list)):
        if x.adjacency_matrix[i][i]:
            counter += 1
    return counter


def is_isolated(x: AdjacencyMatrixGraph, v):
    y = x.vertex_list.index(v)
    return not any(x.adjacency_matrix[y])


def remove_lassos_and_isolated(x: AdjacencyMatrixGraph):
    g2 = copy.deepcopy(x)

    for i in range(len(g2.vertex_list)):
        g2.adjacency_matrix[i][i] = False

    remove_list = []
    for i in range(len(g2.vertex_list)):
        if not any(g2.adjacency_matrix[i]):
            remove_list.append(g2.vertex_list[i])

    for remove in remove_list:
        g2.delete_vertex(remove)

    return g2


matrix = AdjacencyMatrixGraph()
matrix.add_vertex("A")
matrix.add_vertex("B")
matrix.add_vertex("C")
matrix.add_vertex("D")
matrix.add_edge("A", "A")
matrix.add_edge("A", "B")
# matrix.add_edge("B", "C")
print(show_matrix(matrix))
# print(is_isolated(matrix, "A"))
print(show_matrix(remove_lassos_and_isolated(matrix)))
