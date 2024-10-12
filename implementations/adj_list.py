class AdjacencyListGraph:
    def __init__(self):
        self.adjacency_list = {}
        self._edge_count = 0

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

    def delete_vertex(self, v):
        if v in self.adjacency_list:
            for adj_vertex in self.adjacency_list[v]:
                self.adjacency_list[adj_vertex].remove(v)
                self._edge_count -= 1
            del self.adjacency_list[v]

    def add_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list:
            if v not in self.adjacency_list[u]:
                self.adjacency_list[u].append(v)
                self.adjacency_list[v].append(u)
                self._edge_count += 1

    def delete_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list:
            if v in self.adjacency_list[u]:
                self.adjacency_list[u].remove(v)
                self.adjacency_list[v].remove(u)
                self._edge_count -= 1

    def exists_edge(self, u, v):
        return u in self.adjacency_list and v in self.adjacency_list[u]

    def order(self):
        return len(self.adjacency_list)

    def edge_count(self):
        return self._edge_count

    def get_vertex(self, v):
        if v in self.adjacency_list:
            return v
        return None

    def get_adjacency_list(self, v):
        if v in self.adjacency_list:
            return self.adjacency_list[v]
        return None

    def __str__(self):
        return f"Adjacency List: {self.adjacency_list}\nEdge Count: {self._edge_count}"
