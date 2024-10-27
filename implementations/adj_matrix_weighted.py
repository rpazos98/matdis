from implementations.graph import Graph
from implementations.weighted_graph import WeightedGraph


class WeightedAdjacencyMatrixGraph(WeightedGraph):
    def __init__(self, directed=False):
        self.vertex_list = []
        self.adjacency_matrix = []
        self._edge_count = 0
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.vertex_list:
            self.vertex_list.append(v)
            for row in self.adjacency_matrix:
                row.append(None)
            self.adjacency_matrix.append([None] * len(self.vertex_list))

    def delete_vertex(self, v):
        if v in self.vertex_list:
            index = self.vertex_list.index(v)

            for i in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[index][i] is not None:
                    self._edge_count -= 1

            self.adjacency_matrix.pop(index)
            for row in self.adjacency_matrix:
                row.pop(index)

            self.vertex_list.remove(v)

    def add_edge(self, u, v, weight):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            if self.adjacency_matrix[index_u][index_v] is None:
                self.adjacency_matrix[index_u][index_v] = weight
                if not self.directed:
                    self.adjacency_matrix[index_v][index_u] = weight
                self._edge_count += 1

    def delete_edge(self, u, v):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            if self.adjacency_matrix[index_u][index_v] is not None:
                self.adjacency_matrix[index_u][index_v] = None
                if not self.directed:
                    self.adjacency_matrix[index_v][index_u] = None
                self._edge_count -= 1

    def exists_edge(self, u, v):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            return self.adjacency_matrix[index_u][index_v] is not None
        return False

    def get_edge_weight(self, u, v):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            return self.adjacency_matrix[index_u][index_v]
        return None

    def order(self):
        return len(self.vertex_list)

    def edge_count(self):
        return self._edge_count

    def get_vertex(self, v):
        if v in self.vertex_list:
            return v
        return None

    def get_adjacency_list(self, v):
        if v in self.vertex_list:
            index_v = self.vertex_list.index(v)
            adjacency_list = []
            for i, weight in enumerate(self.adjacency_matrix[index_v]):
                if weight is not None:
                    adjacency_list.append((self.vertex_list[i], weight))
            return adjacency_list
        return None

    def __str__(self):
        return f"Vertices: {self.vertex_list}\nAdjacency Matrix: {self.adjacency_matrix}\nEdge Count: {self._edge_count}"
