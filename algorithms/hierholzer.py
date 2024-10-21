import copy
import timeit

from implementations.adj_list import AdjacencyListGraph
from implementations.utils import create_random_graph, generate_connected_even_degree_graph


def hierholzer_algorithm(graph, start):

    graph_copy = copy.deepcopy(graph)

    stack = [start]
    circuit = []

    while stack:
        current_vertex = stack[-1]
        if graph_copy.get_adjacency_list(current_vertex):
            neighbor = graph_copy.get_adjacency_list(current_vertex)[0]
            graph_copy.delete_edge(current_vertex, neighbor)
            stack.append(neighbor)
        else:
            circuit.append(stack.pop())

    return circuit[::-1]


# g = AdjacencyListGraph()
# for v in range(4):
#     g.add_vertex(v)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 3)
# g.add_edge(3, 0)
#
# print(hierholzer_algorithm(g, 0))


def run_random_hierholzer_algorithm(num_vertices=10, num_edges=50):
    g = generate_connected_even_degree_graph(num_vertices, num_edges)
    hierholzer_algorithm(g, 0)


print(timeit.timeit(stmt=lambda: run_random_hierholzer_algorithm(10, 12), number=1))
print(timeit.timeit(stmt=lambda: run_random_hierholzer_algorithm(50, 100), number=10))
print(timeit.timeit(stmt=lambda: run_random_hierholzer_algorithm(1000, 1500), number=10))
# print(timeit.timeit(stmt=lambda: run_random_hierholzer_algorithm(2000, 1500), number=10))
print(timeit.timeit(stmt=lambda: run_random_hierholzer_algorithm(1000, 2000), number=10))
print(timeit.timeit(stmt=lambda: run_random_hierholzer_algorithm(500, int((500 * 499) / 2)), number=1))