import unittest
from services.a_star import Astar
from entities.room import Room


class TestAstar(unittest.TestCase):
    def setUp(self) -> None:
        self.astar = Astar()

    def test_update_maze_updates_correct_spot(self):
        self.astar.update_maze((1, 1))
        self.assertEqual(self.astar.maze[1][1], 1)

    def test_get_doors_works_with_even_numbers(self):
        room = Room(10, 10, 10, 10)
        self.assertEqual(self.astar.get_doors(room),
                         [(15, 10), (15, 20), (10, 15), (20, 15)])

    def test_get_doors_works_with_uneven_numbers(self):
        room = Room(9, 9, 9, 9)
        self.assertEqual(self.astar.get_doors(room),
                         [(13, 9), (13, 18), (9, 13), (18, 13)])

    def test_choose_doors_chooses_the_closest_doors(self):
        start_room = Room(0, 0, 10, 10)
        end_room = Room(0, 20, 10, 10)
        self.assertEqual(self.astar.choose_door(start_room, end_room),
                         ((5, 10), (5, 20)))
