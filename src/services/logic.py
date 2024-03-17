from random import randrange


class Logic():
    def generate_rooms(self, amount):
        rooms = []
        for i in range(amount):
            rooms.append((randrange(0, 800), randrange(0, 800),
                         randrange(3, 75), randrange(3, 75)))
        return rooms
