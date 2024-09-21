from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def add_edge(self, u, v):
        pass

    @abstractmethod
    def add_vertex(self, v):
        pass

    @abstractmethod
    def delete_vertex(self, v):
        pass

    @abstractmethod
    def delete_edge(self, u, v):
        pass

    @abstractmethod
    def exists_edge(self, u, v):
        pass

    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def edge_count(self):
        pass

    @abstractmethod
    def get_vertex(self, v):
        pass

    @abstractmethod
    def get_adjacency_list(self, v):
        pass
