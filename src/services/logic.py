from entities.room import Room
from random import randrange


class Logic:
    """Luokka sovelluksen yleiselle logiikalle

    Attributes:
        room_service (RoomService()): Huoneiden logiikasta vastaavan luokan olio
    """

    def __init__(self, room_service) -> None:
        self.room_service = room_service
        self.rooms = []

    def generate_rooms(self, amount) -> list:
        for _ in range(amount):
            while True:
                room = Room(randrange(50, 740), randrange(50, 740),
                            randrange(10, 150), randrange(10, 150))
                if self.room_service.check_measurements(room) and self.room_service.check_overlap(room, self.rooms):
                    self.rooms.append(room)
                    break
        return self.rooms
