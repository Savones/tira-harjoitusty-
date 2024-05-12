class RoomService:
    """Huoneiden logiikasta huolehtiva luokka
    """

    def check_overlap(self, checked_room, rooms: list) -> bool:
        """Tarkistaa, ettei huone ole toisen huoneen päällä

        Args:
            checked_room (Room): Tarkastettava huone olio
            rooms (list): Lista jo generoituja huone olioita

        Returns:
            bool: Palauttaa True, jos huone ei ole toisen huoneen päällä
        """
        for room in rooms:
            if checked_room.x + checked_room.width > room.x - 50 and checked_room.x < room.x + room.width + 50:
                if checked_room.y + checked_room.height > room.y - 50 and checked_room.y < room.y + room.height + 50:
                    return False
        return True

    def check_inside_triangle(self, room, triangle) -> bool:
        """Tarkistaa, onko huone super kolmion sisällä

        Args:
            room (Room): Huone olio
            triangle (Triangle): Super kolmion Triangle olio

        Returns:
            bool: Palauttaa True, jos huone on super kolmion sisällä
        """
        room_corners = [(room.x, room.y), (room.x + room.width, room.y),
                        (room.x, room.y + room.height), (room.x + room.width, room.y + room.height)]

        for corner in room_corners:
            if not self.check_point_inside_triangle(corner, triangle):
                return False
        return True

    def check_room_in_rect(self, room) -> bool:
        """Tarkistaa, onko huone ikkunan sisällä

        Args:
            room (Room): Room luokan olio

        Returns:
            bool: Palauttaa True, jos huone on ikkunan sisällä, muuten False
        """

        if room.x + room.width >= 1150:
            return False
        if room.x <= 50:
            return False
        if room.y + room.height >= 850:
            return False
        if room.y <= 50:
            return False
        return True

    def check_point_inside_triangle(self, point: tuple, triangle) -> bool:
        """Tarkistaa, onko annettu piste annetun kolmion sisällä

        Args:
            point (tuple): (x,y) koordinaatti
            triangle (Triangle): Triangle luokan olio

        Returns:
            bool: Palauttaa True, jos piste on kolmion sisällä, muuten False
        """

        def sign(point1, point2, point3):
            return (point1[0] - point3[0]) * (point2[1] - point3[1]) - (point2[0] - point3[0]) * (point1[1] - point3[1])

        b1 = sign(point, (triangle.vertex1.x, triangle.vertex1.y),
                  (triangle.vertex2.x, triangle.vertex2.y)) < 0.0
        b2 = sign(point, (triangle.vertex2.x, triangle.vertex2.y),
                  (triangle.vertex3.x, triangle.vertex3.y)) < 0.0
        b3 = sign(point, (triangle.vertex3.x, triangle.vertex3.y),
                  (triangle.vertex1.x, triangle.vertex1.y)) < 0.0

        return (b1 == b2) and (b2 == b3)
