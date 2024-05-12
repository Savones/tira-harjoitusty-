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

    def test_finds_the_least_costly_path(self):
        room1 = Room(10, 10, 10, 10)
        room2 = Room(30, 10, 10, 10)
        self.assertEqual(self.astar.get_astar_paths([(room1, room2)], [room1, room2]),
                         [[(20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15),
                           (28, 15), (29, 15), (30, 15)]])

    def test_chooses_the_same_path_when_going_back_and_forth(self):
        room1 = Room(10, 10, 10, 10)
        room2 = Room(30, 10, 10, 10)
        expected_path = [(20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15),
                         (28, 15), (29, 15), (30, 15)]
        path_backwards = expected_path[::-1]
        self.assertEqual(self.astar.get_astar_paths([(room1, room2), (room2, room1)], [room1, room2]),
                         [expected_path, path_backwards])

    def test_chooses_the_same_path_no_matter_which_room_is_start_room(self):
        room1 = Room(10, 10, 10, 10)
        room2 = Room(30, 10, 10, 10)
        path = self.astar.get_astar_paths([(room1, room2)], [room1, room2])
        backwards_path = path[0][::-1]

        another_astar = Astar()

        self.assertEqual(backwards_path, another_astar.get_astar_paths(
            [(room2, room1)], [room1, room2])[0])

    def test_algorithm_doesnt_produce_diagonal_movement(self):
        start_room = Room(0, 0, 10, 10)
        end_room = Room(10, 10, 10, 10)
        expected_path = [(0, 0), (1, 1), (2, 2), ..., (10, 10)]
        self.assertNotEqual(self.astar.get_astar_paths([(start_room, end_room)], [start_room, end_room]),
                            [expected_path])

    def test_paths_dont_go_through_walls_in_maze(self):
        self.astar.maze[25][15] = 100
        room1 = Room(10, 10, 10, 10)
        room2 = Room(30, 10, 10, 10)
        expected_path = [(20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (24, 14),
                         (25, 14), (26, 14), (26, 15), (27, 15),
                         (28, 15), (29, 15), (30, 15)]
        self.assertEqual(self.astar.get_astar_paths([(room1, room2)], [room1, room2]),
                         [expected_path])
