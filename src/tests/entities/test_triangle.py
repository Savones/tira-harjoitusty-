import unittest
from entities.triangle import Triangle
from entities.vertex import Vertex


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle = Triangle(
            Vertex(500, 200), Vertex(600, 200), Vertex(500, 300))

    def test_str_returns_correct_string(self):
        self.assertEqual(str(self.triangle),
                         "['500, 200', '600, 200', '500, 300']")

    def test_point_in_circumcircle_true_when_in_circle(self):
        point = (550, 210)
        self.assertEqual(True, self.triangle.point_in_circumcircle(point))

    def test_point_in_circumcircle_false_when_not_in_circle(self):
        point = (400, 210)
        self.assertEqual(False, self.triangle.point_in_circumcircle(point))

    def test_get_circum_center_returns_correct_point(self):
        self.assertEqual([550, 250], self.triangle.get_circum_center())
