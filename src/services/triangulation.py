from entities.vertex import Vertex
from entities.triangle import Triangle


class Triangulation:
    """Luokka kolmionnille

    Attributes:
        super_triangle: Triangle luokan olio
        room_vertices (list): lista huoneiden keskipisteitä
    """

    def __init__(self, super_triangle, room_vertices: list):
        self.super_triangle = super_triangle
        self.room_vertices = room_vertices
        self.triangulation = [self.super_triangle]

    def get_triangulation(self) -> tuple:
        for point in self.room_vertices:
            bad_triangles = self.get_bad_triangles(point)
            polygon = self.get_polygon(bad_triangles)

            for triangle in bad_triangles:
                self.triangulation.remove(triangle)

            self.add_triangles(polygon, point)

        new_triangles = self.remove_super_triangle()

        return self.triangulation, new_triangles

    def get_bad_triangles(self, point: tuple) -> list:
        bad_triangles = []
        for triangle in self.triangulation:
            if triangle.point_in_circumcircle(point):
                bad_triangles.append(triangle)
        return bad_triangles

    def get_polygon(self, bad_triangles: list) -> list:
        polygon = []
        for triangle1 in bad_triangles:
            for edge in triangle1.edges:
                edge_shared = False
                for triangle2 in bad_triangles:
                    if triangle1 is not triangle2:
                        edge0_shared = str(edge[0]) in [str(e[0])
                                                        for e in triangle2.edges]
                        edge1_shared = str(edge[1]) in [str(e[1])
                                                        for e in triangle2.edges]
                        if edge0_shared and edge1_shared:
                            edge_shared = True
                            break
                if not edge_shared:
                    polygon.append(edge)
        return polygon

    def add_triangles(self, polygon, point):
        vertex1 = Vertex(point[0], point[1])

        for edge in polygon:
            vertex2 = Vertex(edge[0].x, edge[0].y)
            vertex3 = Vertex(edge[1].x, edge[1].y)
            vertices = [{str(triangle.vertex1), str(triangle.vertex2), str(
                triangle.vertex3)} for triangle in self.triangulation]

            if {str(vertex1), str(vertex2), str(vertex3)} not in vertices:
                self.triangulation.append(
                    Triangle(vertex1, vertex2, vertex3))

    def remove_super_triangle(self):
        new_triangles = []
        for triangle in self.triangulation:
            has_shared_vertex = False
            for vertex in triangle.triangle:
                for supervertex in self.super_triangle.triangle:
                    if vertex.x == supervertex.x and vertex.y == supervertex.y:
                        has_shared_vertex = True
                        break
                if has_shared_vertex:
                    break
            if not has_shared_vertex:
                new_triangles.append(triangle)
        return new_triangles
