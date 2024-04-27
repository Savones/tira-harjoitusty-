class Node:
    def __init__(self, parent, position):
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position == other.position


class Astar:
    def __init__(self):
        self.maze = [[3] * 900 for _ in range(1200)]

    def add_rooms_to_maze(self, room_list: list):
        """Lisää huoneisiin seinät, joiden läpi käytävät eivät voi kulkea

        Args:
            room_list (list): Huoneet listana
        """
        for room in room_list:
            door_1 = room.x + room.width // 2
            door_2 = room.y + room.height // 2

            for i in range(room.width - 1):
                if i == (room.width // 2):
                    self.maze[door_1][room.y] = 0
                    self.maze[door_1][room.y + (room.height - 1)] = 0
                    continue
                self.maze[room.x + i][room.y] = 100
                self.maze[room.x + i][room.y + (room.height - 1)] = 100

            for j in range(room.height):
                if j == (room.height // 2):
                    self.maze[room.x][door_2] = 0
                    self.maze[room.x + (room.width - 1)][door_2] = 0
                    continue
                self.maze[room.x][room.y + j] = 100
                self.maze[room.x + (room.width - 1)][room.y + j] = 100

    def get_astar_paths(self, paths, room_list):
        # self.add_rooms_to_maze(room_list)
        results = []

        for path in paths:
            start = path[0].vertex
            end = path[1].vertex

            results.append(self.run_astar(start, end))

        return results

    def run_astar(self, start, end):
        end = Node(None, end)
        open_list = [Node(None, start)]
        closed_list = []

        while True:
            # Valitsee käsiteltävän noden, eli pienimmän f hinnan node open_list:sta
            current_index = 0
            for index in range(len(open_list)):
                if open_list[index].f < open_list[current_index].f:
                    current_index = index

            # Lisää closed_listiin ja poistaa open_listista käsiteltävän noden
            current_node = open_list[current_index]
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Jos käsiteltävä node on määränpää, lisää polun karttaan ja palauttaa polun
            if current_node == end:
                path = []
                while current_node:
                    path.append(current_node.position)
                    self.update_maze(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            children = []
            positions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            # Lisää kelvolliset lapset listaan
            for position in positions:
                node_position = (
                    current_node.position[0] + position[0], current_node.position[1] + position[1])

                # Jos sijainti yli kartan, ei sovellu lapseksi
                if node_position[0] > (len(self.maze) - 1) or node_position[1] > (len(self.maze[len(self.maze) - 1]) - 1):
                    continue

                # Jos vastassa huoneen seinä, ei sovellu lapseksi
                if self.maze[node_position[0]][node_position[1]] == 100:
                    continue

                children.append(Node(current_node, node_position))

            # Lisää halvat lapset open_listiin
            for child in children:

                # Jos lapsi on jo käsitelty, siirry seuraavaan lapseen
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Päivitä g, h, f hinnat
                child.g = current_node.g + \
                    self.maze[child.position[0]][child.position[1]]
                child.h = ((child.position[0] - end.position[0]) ** 2) + (
                    (child.position[1] - end.position[1]) ** 2)
                child.f = child.g + child.h

                # Jos lapsi on jo open_listissa ja se on kalliimpi, siirry seuraavaan lapseen
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)

    def update_maze(self, pos):
        self.maze[pos[0]][pos[1]] = 0


class Room:
    """Huonetta kuvaava luokka

    Attributes:
            x (int): Huoneen vasemmanpuolimmaisin x-koordinaatti
            y (int): Huoneen ylin y-koordinaatti
            width (int): Huoneen leveys
            height (int): Huoneen korkeus
    """

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertex = (x + (width // 2), (y + (height // 2)))

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"


if __name__ == "__main__":
    astar = Astar()
    room_1 = Room(10, 5, 5, 5)
    room_2 = Room(1, 1, 4, 4)
    rooms = [room_1, room_2]
    paths = [[room_1, room_2]]
    results = astar.get_astar_paths(paths, rooms)

    for i in results:
        print()
        print(len(i))
