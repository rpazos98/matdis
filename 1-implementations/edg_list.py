class EdgeListGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_vertex(self, v):
        self.vertices.add(v)

    def delete_vertex(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            self.edges = [edge for edge in self.edges if edge[0] != v and edge[1] != v]

    def add_edge(self, u, v):
        if (
            u in self.vertices
            and v in self.vertices
            and (u, v) not in self.edges
            and (v, u) not in self.edges
        ):
            self.edges.append((u, v))

    def delete_edge(self, u, v):
        if (u, v) in self.edges:
            self.edges.remove((u, v))
        elif (v, u) in self.edges:
            self.edges.remove((v, u))

    def exists_edge(self, u, v):
        return (u, v) in self.edges or (v, u) in self.edges

    def order(self):
        return len(self.vertices)

    def edge_count(self):
        return len(self.edges)

    def get_vertex(self, v):
        return v if v in self.vertices else None

    def get_adjacency_list(self, v):
        if v in self.vertices:
            adjacency_list = [
                u if v == w else w for u, w in self.edges if u == v or w == v
            ]
            return adjacency_list
        return None

    def __str__(self):
        return f"Vertices: {self.vertices}\nEdges: {self.edges}\nEdge Count: {self.edge_count()}"
