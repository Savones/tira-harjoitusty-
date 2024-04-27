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
            Vertex(-2000, 900), Vertex(599, -500), Vertex(3200, 900))
        self.triangulation = []
        self.mst = []
        self.chosen_edges = []

    def reset(self):
        self.rooms = []
        self.room_vertices = []
        self.triangulation = []
        self.mst = []
        self.chosen_edges = []

    def generate_rooms(self, amount: int) -> list:
        """Generoi huoneet

        Args:
            amount (int): Generoitavien huoneiden määrä

        Returns:
            list: Lista Room olioita
        """
        for _ in range(amount):
            while True:
                room = Room(randrange(0, 1200), randrange(0, 900),
                            randrange(10, 150), randrange(10, 150))
                if self.room_service.check_overlap(room, self.rooms) and self.room_service.check_room_in_rect(room):
                    self.rooms.append(room)
                    break

        return self.rooms

    def generate_room_vertices(self) -> list:
        """Määrittää huoneiden keskipisteet

        Returns:
            list: Lista huoneiden keskipisteiden koordinaatteja tupleina
        """
        for room in self.rooms:
            self.room_vertices.append(
                room.vertex)
        return self.room_vertices

    def get_triangulation(self) -> tuple:
        """Suorittaa kolmioinnin

        Returns:
            tuple: Kaksi kolmiointia kuvaavaa listaa tuplena, joista 2. lopullinen
        """
        triangulation_logic = Triangulation(
            self.super_triangle, self.room_vertices)
        all_triangulation, self.triangulation = triangulation_logic.get_triangulation()
        return all_triangulation, self.triangulation

    def get_mst(self, triangulation: list) -> list:
        """Laskee huoneille pienimmän virittävän puun

        Args:
            triangulation (list): Kolmiointia kuvaava lista Triangle olioita

        Returns:
            list: Pienintä virittävää puuta kuvaava lista
        """
        self.mst = Mst(self.room_vertices, triangulation).get_mst()
        return self.mst

    def get_chosen_edges(self) -> list:
        """Lisää arpomalla osan kolmioinnin käytävistä mst käytäviin

        Returns:
            list: Lista lopullisia käytäviä 
        """
        self.chosen_edges = self.mst[:]
        edges = []
        for triangle in self.triangulation:
            for edge in triangle.edges:
                edge_tuple = [(edge[0].x, edge[0].y), (edge[1].x, edge[1].y)]
                if edge_tuple not in edges and edge_tuple[::-1] not in edges:
                    if edge_tuple not in self.mst and edge_tuple[::-1] not in self.mst:
                        edges.append(edge_tuple)

        for edge in edges:
            ticket = randrange(1, 10)
            if ticket > 8:
                self.chosen_edges.append(edge)

        print(self.chosen_edges)
        return self.chosen_edges
