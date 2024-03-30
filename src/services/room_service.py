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

    def check_inside_triangle(self, room, triangle_vertices) -> bool:
        room_corners = [(room.x, room.y), (room.x + room.width, room.y),
                        (room.x, room.y + room.height), (room.x + room.width, room.y + room.height)]

        for corner in room_corners:
            if not self.check_point_inside_triangle(corner, triangle_vertices):
                return False
        return True

    def check_point_inside_triangle(self, point, triangle):
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

        b1 = sign(point, (triangle.vertex1.x, triangle.vertex1.y),
                  (triangle.vertex2.x, triangle.vertex2.y)) < 0.0
        b2 = sign(point, (triangle.vertex2.x, triangle.vertex2.y),
                  (triangle.vertex3.x, triangle.vertex3.y)) < 0.0
        b3 = sign(point, (triangle.vertex3.x, triangle.vertex3.y),
                  (triangle.vertex1.x, triangle.vertex1.y)) < 0.0

        return (b1 == b2) and (b2 == b3)
