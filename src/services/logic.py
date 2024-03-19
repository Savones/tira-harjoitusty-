from entities.room import Room
from random import randrange


class Logic:
    def __init__(self) -> None:
        self.rooms = []

    def generate_rooms(self, amount) -> list:
        for _ in range(amount):
            self.rooms.append(Room(randrange(0, 800), randrange(0, 800),
                                   randrange(3, 75), randrange(3, 75)))
        return self.rooms
