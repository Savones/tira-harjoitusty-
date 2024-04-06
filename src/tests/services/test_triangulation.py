from entities.vertex import Vertex
from entities.triangle import Triangle
import unittest
from services.triangulation import Triangulation
from services.logic import Logic
from services.room_service import RoomService


class TestTriangulation(unittest.TestCase):
    def setUp(self) -> None:
        self.room_service = RoomService()
        self.logic = Logic(self.room_service)
        self.room_vertices = [(780, 713), (797, 403),
                              (462, 411), (474, 628), (226, 693)]
        self.triangulation = Triangulation(
            self.logic.super_triangle, self.room_vertices)

    def test_get_triangulation_returns_tuple(self):
        result = self.triangulation.get_triangulation()
        self.assertIsInstance(result, tuple)

    def test_get_bad_triangles_returns_empty_list_for_point_outside_circumcircle(self):
        point = (100, 100)
        result = self.triangulation.get_bad_triangles(point)
        self.assertEqual(len(result), 0)
