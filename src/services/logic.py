from services.mst import Mst
from entities.room import Room
from entities.vertex import Vertex
from entities.triangle import Triangle
from services.triangulation import Triangulation
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

    def get_triangulation(self) -> tuple:
        triangulation_logic = Triangulation(
            self.super_triangle, self.room_vertices)
        triangulation, new_triangulation = triangulation_logic.get_triangulation()
        return triangulation, new_triangulation

    def get_mst(self, triangulation):
        return Mst(self.room_vertices, triangulation).get_mst()
