from implementations.utils import create_random_graph, generate_connected_even_degree_graph


def hamiltonian_path(graph, path=None):
    if path is None:
        path = []

    if len(path) == graph.order():
        return path

    for vertex in graph.adjacency_list.keys():
        if vertex not in path:
            path.append(vertex)

            if hamiltonian_path_util(graph, path):
                return path

            path.pop()

    return None


def hamiltonian_path_util(graph, path):
    if len(path) == graph.order():
        return True

    last_vertex = path[-1]
    for neighbor in graph.get_adjacency_list(last_vertex):
        if neighbor not in path:
            path.append(neighbor)

            if hamiltonian_path_util(graph, path):
                return True

            path.pop()

    return False


def hamiltonian_cycle(graph, path=None):
    if path is None:
        path = []

    if len(path) == graph.order() + 1 and path[0] == path[-1]:
        return path

    for vertex in graph.adjacency_list.keys():
        if vertex not in path:
            path.append(vertex)

            if hamiltonian_cycle_util(graph, path):
                return path

            path.pop()

    return None


def hamiltonian_cycle_util(graph, path):
    if len(path) == graph.order() + 1 and path[0] == path[-1]:
        return True

    last_vertex = path[-1]
    for neighbor in graph.get_adjacency_list(last_vertex):
        if neighbor not in path or (len(path) == graph.order() and neighbor == path[0]):
            path.append(neighbor)

            if hamiltonian_cycle_util(graph, path):
                return True

            path.pop()

    return False


def run_random_hierholzer_algorithm(num_vertices=5, num_edges=6):
    g = generate_connected_even_degree_graph(num_vertices, num_edges)
    return hamiltonian_path(g)


print(run_random_hierholzer_algorithm())
