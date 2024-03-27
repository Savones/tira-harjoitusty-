class Edge:
    def __init__(self, vertex1: tuple, vertex2: tuple):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.edge = [vertex1, vertex2]
