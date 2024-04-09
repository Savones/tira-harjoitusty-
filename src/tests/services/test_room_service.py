import unittest
from services.room_service import RoomService
from entities.room import Room
from entities.vertex import Vertex
from entities.triangle import Triangle


class TestRoomService(unittest.TestCase):
    def setUp(self) -> None:
        self.room_service = RoomService()
        self.checked_room = Room(100, 100, 100, 100)
        self.super_triangle = Triangle(
            Vertex(0, 898), Vertex(599, 0), Vertex(1198, 898))

    def test_check_overlap_return_true_when_no_x_overlap(self):
        rooms = [Room(400, 100, 100, 100)]
        self.assertEqual(
            True, self.room_service.check_overlap(self.checked_room, rooms))

    def test_check_overlap_return_true_when_no_y_overlap(self):
        rooms = [Room(100, 400, 100, 100)]
        self.assertEqual(
            True, self.room_service.check_overlap(self.checked_room, rooms))

    def test_check_overlap_return_false_when_overlap(self):
        rooms = [Room(100, 100, 100, 100)]
        self.assertEqual(
            False, self.room_service.check_overlap(self.checked_room, rooms))

    def test_check_inside_triangle_returns_true_when_room_in_triangle(self):
        self.assertEqual(self.room_service.check_inside_triangle(
            Room(500, 200, 10, 10), self.super_triangle), True)

    def test_check_inside_triangle_returns_false_when_room_not_in_triangle(self):
        self.assertEqual(self.room_service.check_inside_triangle(
            self.checked_room, self.super_triangle), False)

    def test_check_point_inside_triangle_returns_true_when_point_in_triangle(self):
        self.assertEqual(
            self.room_service.check_point_inside_triangle((500, 200), self.super_triangle), True)

    def test_check_point_inside_triangle_returns_false_when_point_not_in_triangle(self):
        self.assertEqual(
            self.room_service.check_point_inside_triangle((0, 0), self.super_triangle), False)
