import unittest
from services.mst import Mst
from entities.room import Room
from entities.vertex import Vertex
from entities.triangle import Triangle
from services.triangulation import Triangulation
from services.room_service import RoomService
from services.logic import Logic


class TestLogic(unittest.TestCase):
    def setUp(self) -> None:
        self.logic = Logic(RoomService())

    def test_reset_resets_rooms(self):
        self.logic.generate_rooms(5)
        self.logic.reset()
        self.assertEqual((self.logic.rooms), [])

    def test_reset_resets_room_vertices(self):
        self.logic.generate_rooms(5)
        self.logic.generate_room_vertices()
        self.logic.reset()
        self.assertEqual((self.logic.room_vertices), [])
