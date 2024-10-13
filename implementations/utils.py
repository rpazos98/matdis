import random

from implementations.adj_list import AdjacencyListGraph


def create_random_graph(num_vertices, num_edges):
    g = AdjacencyListGraph()

    for v in range(num_vertices):
        g.add_vertex(v)

    edges = set()
    while len(edges) < num_edges:
        v1 = random.randint(0, num_vertices - 1)
        v2 = random.randint(0, num_vertices - 1)
        if v1 != v2:
            edges.add((v1, v2))

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


def generate_connected_even_degree_graph(num_vertices, num_edges):
    if num_vertices < 1 or num_edges < num_vertices - 1 or num_edges % 2 != 0:
        raise ValueError(
            "Invalid number of vertices or edges. Ensure the graph is possible."
        )

    graph = AdjacencyListGraph()

    # Add vertices
    for i in range(num_vertices):
        graph.add_vertex(i)

    # Connect vertices to ensure the graph is connected (forming a cycle)
    for i in range(num_vertices):
        graph.add_edge(i, (i + 1) % num_vertices)

    # Add edges until the desired edge count is reached
    while graph.edge_count() < num_edges:
        u, v = random.sample(range(num_vertices), 2)
        if v not in graph.get_adjacency_list(u):
            graph.add_edge(u, v)

    # Ensure all vertices have even degree
    for vertex in range(num_vertices):
        while len(graph.get_adjacency_list(vertex)) % 2 != 0:
            # Randomly select a neighbor to connect to
            neighbor = random.choice([n for n in range(num_vertices) if n != vertex])
            if neighbor not in graph.get_adjacency_list(vertex):
                graph.add_edge(vertex, neighbor)

    return graph
