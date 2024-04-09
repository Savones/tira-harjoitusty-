import unittest
from entities.vertex import Vertex


class TestVertex(unittest.TestCase):
    def test_int_initializes_correct(self):
        vertex = Vertex(10, 10)
        self.assertEqual(vertex.x, 10)
        self.assertEqual(vertex.y, 10)

    def test_str_method_returns_correct_str(self):
        vertex = Vertex(10, 10)
        self.assertEqual(str(vertex), "10, 10")
