from entities.room import Room
from random import randrange


class Logic:
    def __init__(self) -> None:
        self.rooms = []

    def generate_rooms(self, amount) -> list:
        for _ in range(amount):
            while True:
                room = Room(randrange(50, 740), randrange(50, 740),
                            randrange(10, 150), randrange(10, 150))
                if self.check_measurements(room) and self.check_overlap(room):
                    self.rooms.append(room)
                    break
        return self.rooms

    def check_overlap(self, checked_room) -> bool:
        for room in self.rooms:
            if checked_room.x + checked_room.width > room.x - 50 and checked_room.x < room.x + room.width + 50:
                if checked_room.y + checked_room.height > room.y - 50 and checked_room.y < room.y + room.height + 50:
                    return False
        return True

    def check_measurements(self, room):
        if room.x + room.width <= 750:
            if room.y + room.height <= 750:
                return True
        return False
