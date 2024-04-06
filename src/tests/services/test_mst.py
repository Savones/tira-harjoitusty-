import unittest
from services.mst import Mst
from entities.room import Room
from entities.vertex import Vertex
from entities.triangle import Triangle
from services.room_service import RoomService
from services.logic import Logic


class TestMst(unittest.TestCase):
    def setUp(self) -> None:
        self.logic = Logic(RoomService())
        self.room_vertices = [(780, 713), (797, 403),
                              (462, 411), (474, 628), (226, 693)]
        self.triangulation = [
            Triangle(Vertex(474, 628), Vertex(462, 411), Vertex(797, 403)),
            Triangle(Vertex(474, 628), Vertex(797, 403), Vertex(780, 713)),
            Triangle(Vertex(226, 693), Vertex(474, 628), Vertex(780, 713)),
            Triangle(Vertex(226, 693), Vertex(474, 628), Vertex(462, 411))]
        self.mst = Mst(self.room_vertices, self.triangulation)

    def test_get_mst_returns_list(self):
        result = self.mst.get_mst()
        self.assertIsInstance(result, list)
