import unittest
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

    def test_generates_correct_amount_of_rooms(self):
        self.logic.generate_rooms(5)
        self.assertEqual(len(self.logic.rooms), 5)

    def test_generates_correct_amount_of_room_vertices(self):
        self.logic.generate_rooms(5)
        self.logic.generate_room_vertices()
        self.assertEqual(len(self.logic.room_vertices), 5)

    def test_get_triangulation_returns_tuple(self):
        self.logic.generate_rooms(5)
        self.assertEqual(type(self.logic.get_triangulation()), tuple)

    def test_get_triangulation_triangulation_is_list(self):
        self.logic.generate_rooms(5)
        self.assertEqual(type(self.logic.get_triangulation()[0]), list)

    def test_get_triangulation_new_triangulation_is_list(self):
        self.logic.generate_rooms(5)
        self.assertEqual(type(self.logic.get_triangulation()[1]), list)

    def test_get_mst_returns_list(self):
        self.logic.room_vertices = [(780, 713), (797, 403),
                                    (462, 411), (474, 628), (226, 693)]
        triangulation, new_triangulation = self.logic.get_triangulation()
        self.assertEqual(type(self.logic.get_mst(new_triangulation)), list)

    def test_get_mst_includes_all_vertices(self):
        self.logic.room_vertices = [(780, 713), (797, 403),
                                    (462, 411), (474, 628), (226, 693)]
        triangulation, new_triangulation = self.logic.get_triangulation()
        self.assertEqual(len(self.logic.get_mst(new_triangulation)), 4)
