import unittest
from services.room_service import RoomService
from entities.room import Room


class TestRoomService(unittest.TestCase):
    def setUp(self) -> None:
        self.room_service = RoomService()
        self.checked_room = Room(100, 100, 100, 100)

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
