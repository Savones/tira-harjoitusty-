import unittest
import math
from services.triangulation import Triangulation
from services.logic import Logic
from services.room_service import RoomService
from entities.triangle import Triangle
from entities.vertex import Vertex


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

    def test_get_bad_triangles_returns_list_with_supertriangle_only(self):
        point = (0, 0)
        result = self.triangulation.get_bad_triangles(point)
        self.assertEqual(len(result), 1)
        self.assertEqual(
            str(result[0]), "['-2000, 900', '599, -500', '3200, 900']")

    def test_no_points_in_final_triangulation_circles(self):
        returns = []
        triangulation = self.triangulation.get_triangulation()[1]
        for point in self.room_vertices:
            for triangle in triangulation:
                point_distance = math.sqrt(
                    (point[0] - triangle.circum_center[0])**2 + (point[1] - triangle.circum_center[1])**2)
                radius = math.sqrt(
                    (triangle.vertex1.x - triangle.circum_center[0])**2 + (triangle.vertex1.y - triangle.circum_center[1])**2)
                returns.append(int(point_distance) >= int(radius))

        self.assertEqual(False not in returns, True)

    def test_all_points_found_in_triangulation(self):
        triangulation = self.triangulation.get_triangulation()[1]
        found = [False] * len(self.room_vertices)
        for i, point in enumerate(self.room_vertices):
            for triangle in triangulation:
                if point[0] in [vertex.x for vertex in triangle.triangle] and point[1] in [vertex.y for vertex in triangle.triangle]:
                    found[i] = True

        self.assertEqual(False not in found, True)
