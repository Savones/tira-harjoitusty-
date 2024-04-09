import unittest
from entities.triangle import Triangle
from entities.vertex import Vertex


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle = Triangle(
            Vertex(500, 200), Vertex(510, 210), Vertex(520, 220))
