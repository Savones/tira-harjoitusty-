import unittest
from entities.room import Room


class TestRoom(unittest.TestCase):
    def test_init_initializes_correct(self):
        room = Room(10, 10, 10, 10)
        self.assertEqual(room.x, 10)
        self.assertEqual(room.y, 10)
        self.assertEqual(room.width, 10)
        self.assertEqual(room.height, 10)

    def test_str_method_return_correct_string(self):
        room = Room(10, 11, 12, 13)
        self.assertEqual(str(room), "10, 11, 12, 13")

    def test_vertex_calculated_correct_with_even_number(self):
        room = Room(10, 10, 10, 10)
        self.assertEqual(room.vertex, (15, 15))

    def test_vertex_calculated_correct_with_uneven_number(self):
        room = Room(10, 9, 10, 9)
        self.assertEqual(room.vertex, (15, 13))
