import timeit

import matplotlib.pyplot as plt

from implementations.utils import generate_connected_even_degree_graph


def is_bridge(graph, u, v):
    initial_count = dfs_count(graph, u)
    graph.delete_edge(u, v)
    new_count = dfs_count(graph, u)
    graph.add_edge(u, v)
    return initial_count > new_count


# recursive
# def dfs_count(graph, v, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(v)
#     count = 1
#     for neighbor in graph.get_adjacency_list(v):
#         if neighbor not in visited:
#             count += dfs_count(graph, neighbor, visited)
#     return count


# iterative
def dfs_count(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    count = 0

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            count += 1
            for neighbor in graph.get_adjacency_list(vertex):
                if neighbor not in visited:
                    stack.append(neighbor)

    return count


def fleury_algorithm(graph, start):
    path = [start]
    current_vertex = start

    while graph.edge_count() > 0:
        for neighbor in graph.get_adjacency_list(current_vertex):
            if len(graph.get_adjacency_list(current_vertex)) == 1 or not is_bridge(
                    graph, current_vertex, neighbor
            ):
                path.append(neighbor)
                graph.delete_edge(current_vertex, neighbor)
                current_vertex = neighbor
                break
        else:
            break

    return path


# g = AdjacencyListGraph()
# for v in range(4):
#     g.add_vertex(v)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 0)
#
# print(fleury_algorithm(g, 0))


def run_random_fleury_algorithm(num_vertices=10, num_edges=50):
    g = generate_connected_even_degree_graph(num_vertices, num_edges)
    fleury_algorithm(g, 0)


print(timeit.timeit(stmt=lambda: run_random_fleury_algorithm(10, 12), number=10))
print(timeit.timeit(stmt=lambda: run_random_fleury_algorithm(50, 100), number=10))
print(timeit.timeit(stmt=lambda: run_random_fleury_algorithm(1000, 1500), number=10))
print(timeit.timeit(stmt=lambda: run_random_fleury_algorithm(500, int((500*499)/2)), number=1))