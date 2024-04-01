from entities.room import Room
from entities.vertex import Vertex
from entities.triangle import Triangle
from random import randrange


class Logic:
    """Luokka sovelluksen yleiselle logiikalle

    Attributes:
        room_service (RoomService()): Huoneiden logiikasta vastaavan luokan olio
    """

    def __init__(self, room_service) -> None:
        self.room_service = room_service
        self.rooms = []
        self.room_vertices = []
        self.super_triangle = Triangle(
            Vertex(0, 898), Vertex(599, 0), Vertex(1198, 898))

    def reset(self):
        self.rooms = []
        self.room_vertices = []

    def generate_rooms(self, amount: int) -> list:
        for _ in range(amount):
            while True:
                room = Room(randrange(0, 1200), randrange(0, 900),
                            randrange(10, 150), randrange(10, 150))
                if self.room_service.check_overlap(room, self.rooms) and self.room_service.check_inside_triangle(room, self.super_triangle):
                    self.rooms.append(room)
                    break
        return self.rooms

    def generate_room_vertices(self) -> list:
        for room in self.rooms:
            self.room_vertices.append(
                ((room.x + (room.width // 2), (room.y + (room.height // 2)))))
        return self.room_vertices

    def get_trianglutation(self) -> list:
        trianglutation = [self.super_triangle]
        for point in self.room_vertices:
            bad_triangles = []

            for triangle in trianglutation:
                if triangle.point_in_circumcycle(point):
                    bad_triangles.append(triangle)

            polygon = []

            # Rikollisen monta for looppia
            for triangle in bad_triangles:
                for edge in triangle.edges:
                    for triangle2 in bad_triangles:
                        if edge not in [e for e in triangle2.edges if e not in triangle.edges]:
                            polygon.append(edge)

            for triangle in bad_triangles:
                trianglutation.remove(triangle)

            for edge in polygon:
                trianglutation.append(
                    Triangle(Vertex(point[0], point[1]), Vertex(edge.edge[0].x, edge.edge[0].y), Vertex(edge.edge[1].x, edge.edge[1].y)))

        new_triangles = []
        for triangle in trianglutation:
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

        new_triangles

        return trianglutation, new_triangles
