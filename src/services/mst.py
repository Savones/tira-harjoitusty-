import math


class Mst:
    def __init__(self, room_vertices, triangulation):
        self.room_vertices = room_vertices
        self.triangulation = triangulation
        self.graph = []
        self.room_amount = len(room_vertices)

    def get_mst(self):
        graph = self.create_graph()
        distance = [10000] * self.room_amount
        parent = [None] * self.room_amount
        visited = [False] * self.room_amount

        distance[0] = 0
        parent[0] = -1

        while False in visited:
            min_index = self.get_min_index(distance, visited)
            visited[min_index] = True
            for neighbor in range(self.room_amount):
                if graph[min_index][neighbor] > 0 and visited[neighbor] == False \
                        and distance[neighbor] > graph[min_index][neighbor]:
                    distance[neighbor] = graph[min_index][neighbor]
                    parent[neighbor] = min_index

        return self.get_mst_edges(parent)

    def calculate_distance(self, vertex1, vertex2):
        x1, y1 = vertex1.x, vertex1.y
        x2, y2 = vertex2.x, vertex2.y
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def create_graph(self):
        edges = {}
        for triangle in self.triangulation:
            for edge in triangle.edges:
                edge_tuple = ((edge[0].x, edge[0].y), (edge[1].x, edge[1].y))
                if edge_tuple not in edges and edge_tuple[::-1] not in edges:
                    edges[edge_tuple] = self.calculate_distance(
                        edge[0], edge[1])

        graph = [[0] * self.room_amount
                 for _ in range(self.room_amount)]

        for vertex_index, vertex in enumerate(self.room_vertices):
            for edge, distance in edges.items():
                if vertex in edge:
                    neighbor = edge[0] if edge[0] != vertex else edge[1]
                    neighbor_index = self.room_vertices.index(neighbor)
                    graph[vertex_index][neighbor_index] = distance

        return graph

    def get_min_index(self, distanse, visited):
        min = 10000
        for vertex_index in range(self.room_amount):
            if distanse[vertex_index] < min and visited[vertex_index] == False:
                min = distanse[vertex_index]
                min_index = vertex_index
        return min_index

    def get_mst_edges(self, parent):
        help_dict = {}
        mst_edges = []

        for i, vertex in enumerate(self.room_vertices):
            help_dict[i] = vertex
        for vertex in range(1, self.room_amount):
            neighbor = parent[vertex]
            mst_edges.append([help_dict[neighbor], help_dict[vertex]])
        return mst_edges
