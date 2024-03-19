class RoomService:
    """Huoneiden logiikasta huolehtiva luokka
    """

    def check_overlap(self, checked_room, rooms: list) -> bool:
        for room in rooms:
            if checked_room.x + checked_room.width > room.x - 50 and checked_room.x < room.x + room.width + 50:
                if checked_room.y + checked_room.height > room.y - 50 and checked_room.y < room.y + room.height + 50:
                    return False
        return True

    def check_measurements(self, room) -> bool:
        if room.x + room.width <= 750:
            if room.y + room.height <= 750:
                return True
        return False
