from graph import Graph


class AdjacencyMatrixGraph(Graph):
    def __init__(self):
        self.vertex_list = []
        self.adjacency_matrix = []
        self._edge_count = 0

    def add_vertex(self, v):
        if v not in self.vertex_list:
            self.vertex_list.append(v)

            for row in self.adjacency_matrix:
                row.append(False)
            self.adjacency_matrix.append([False] * len(self.vertex_list))

    def delete_vertex(self, v):
        if v in self.vertex_list:
            index = self.vertex_list.index(v)

            for i in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[index][i]:
                    self._edge_count -= 1

            self.adjacency_matrix.pop(index)
            for row in self.adjacency_matrix:
                row.pop(index)

            self.vertex_list.remove(v)

    def add_edge(self, u, v):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            if not self.adjacency_matrix[index_u][index_v]:
                self.adjacency_matrix[index_u][index_v] = True
                self.adjacency_matrix[index_v][index_u] = True
                self._edge_count += 1

    def delete_edge(self, u, v):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            if self.adjacency_matrix[index_u][index_v]:
                self.adjacency_matrix[index_u][index_v] = False
                self.adjacency_matrix[index_v][index_u] = False
                self._edge_count -= 1

    def exists_edge(self, u, v):
        if u in self.vertex_list and v in self.vertex_list:
            index_u = self.vertex_list.index(u)
            index_v = self.vertex_list.index(v)
            return self.adjacency_matrix[index_u][index_v]
        return False

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
            for i, is_adjacent in enumerate(self.adjacency_matrix[index_v]):
                if is_adjacent:
                    adjacency_list.append(self.vertex_list[i])
            return adjacency_list
        return None

    def __str__(self):
        return f"Vertices: {self.vertex_list}\nAdjacency Matrix: {self.adjacency_matrix}\nEdge Count: {self._edge_count}"
