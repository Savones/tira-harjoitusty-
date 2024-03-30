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
