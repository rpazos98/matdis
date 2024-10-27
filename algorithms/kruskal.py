from implementations.adj_matrix_weighted import WeightedAdjacencyMatrixGraph
from implementations.weighted_graph import WeightedGraph


class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_algorithm(graph: WeightedGraph):
    mst_edges = []
    edges = []

    for v in graph.vertex_list:
        for neighbor, weight in graph.get_adjacency_list(v):
            if (neighbor, v, weight) not in edges:
                edges.append((v, neighbor, weight))

    edges.sort(key=lambda x: x[2])

    uf = UnionFind(graph.vertex_list)

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))

    return mst_edges


individuals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
uf = UnionFind(individuals)

relationships = [
    ('a', 'b'),
    ('b', 'd'),
    ('c', 'f'),
    ('c', 'i'),
    ('j', 'e'),
    ('g', 'j')
]

for u, v in relationships:
    uf.union(u, v)

groups = {}
for person in individuals:
    root = uf.find(person)
    if root not in groups:
        groups[root] = []
    groups[root].append(person)

for group in groups.values():
    print(group)

graph = WeightedAdjacencyMatrixGraph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 3)

mst = kruskal_algorithm(graph)

print("Árbol de Expansión Mínima:")
for u, v, weight in mst:
    print(f"{u} - {v} (peso: {weight})")


