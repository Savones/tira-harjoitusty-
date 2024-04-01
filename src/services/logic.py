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

        # Väliaikainen
        self.rooms = [Room(880, 617, 44, 32), Room(
            616, 605, 123, 58), Room(295, 815, 40, 76), Room(474, 739, 84, 138)]
        # self.rooms = [Room(389, 511, 91, 49), Room(
        #     758, 418, 35, 63), Room(238, 784, 107, 75), Room(611, 243, 86, 124)]

        return self.rooms

    def generate_room_vertices(self) -> list:
        for room in self.rooms:
            self.room_vertices.append(
                ((room.x + (room.width // 2), (room.y + (room.height // 2)))))
        return self.room_vertices

    def get_triangulation(self) -> list:
        trianglutation = [self.super_triangle]

        for point in self.room_vertices:
            print(f"\nPoint is {point}")
            bad_triangles = []

            for triangle in trianglutation:
                print(
                    f"Triangle in trianglulation: {str(triangle)}, circumcenter {triangle.circum_center}")
                if triangle.point_in_circumcircle(point):
                    print(
                        f"Point in circumcircle")
                    bad_triangles.append(triangle)

            polygon = []

            for triangle1 in bad_triangles:
                for edge in triangle1.edges:
                    edge_shared = False
                    for triangle2 in bad_triangles:
                        if triangle1 is not triangle2 and edge in triangle2.edges:
                            edge_shared = True
                            break
                    if not edge_shared:
                        polygon.append(edge)

            for triangle in bad_triangles:
                trianglutation.remove(triangle)

            for edge in polygon:
                vertex1 = Vertex(point[0], point[1])
                vertex2 = Vertex(edge[0].x, edge[0].y)
                vertex3 = Vertex(edge[1].x, edge[1].y)

                if {str(vertex1), str(vertex2), str(vertex3)} not in [{str(triangle.vertex1), str(triangle.vertex2), str(triangle.vertex3)} for triangle in trianglutation]:
                    trianglutation.append(Triangle(vertex1, vertex2, vertex3))
                    print(
                        f"Triangle added: {str(Triangle(vertex1, vertex2, vertex3))}")

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

        print(len(trianglutation), len(new_triangles))
        for triangle in new_triangles:
            print(str(triangle))

        return trianglutation, new_triangles
