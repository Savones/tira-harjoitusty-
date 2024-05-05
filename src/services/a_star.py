from queue import PriorityQueue


class Astar:
    def __init__(self):
        self.maze = [[1] * 900 for _ in range(1200)]

    def add_rooms_to_maze(self, room_list: list):
        """Lisää huoneisiin seinät, joiden läpi käytävät eivät voi kulkea

        Args:
            room_list (list): Huoneet listana
        """
        for room in room_list:
            width = room.width
            height = room.height
            x = room.x
            y = room.y

            door_1 = x + (width // 2)
            door_2 = y + (height // 2)

            for i in range(x, x + width + 1):
                if i == door_1:
                    self.maze[door_1][y] = 0
                    self.maze[door_1][y + height] = 0
                    continue
                self.maze[i][y] = 100
                self.maze[i][y + height] = 100

            for j in range(y, y + height + 1):
                if j == door_2:
                    self.maze[x][door_2] = 0
                    self.maze[x + width][door_2] = 0
                    continue
                self.maze[x][j] = 100
                self.maze[x + width][j] = 100

    def get_astar_paths(self, paths, room_list):
        self.add_rooms_to_maze(room_list)
        results = []

        for path in paths:
            start = path[0].vertex
            end = path[1].vertex

            results.append(self.run_astar(start, end))

        return results

    def run_astar(self, start, end):
        priority_queue = PriorityQueue()
        distance = [[float('inf')] * 900 for _ in range(1200)]
        handled = [[False] * 900 for _ in range(1200)]
        parents = {}

        priority_queue.put((0, start))
        distance[start[0]][start[1]] = 0

        while not priority_queue.empty():
            node = priority_queue.get()[1]

            if node == end:
                path = []
                while node in parents:
                    path.append(node)
                    self.update_maze(node)
                    node = parents[node]
                path.append(start)
                return path[::-1]

            if handled[node[0]][node[1]]:
                continue

            if self.maze[node[0]][node[1]] == 100:
                continue

            handled[node[0]][node[1]] = True

            edges = [(node[0] + 1, node[1]),
                     (node[0] - 1, node[1]),
                     (node[0], node[1] + 1),
                     (node[0], node[1] - 1)]

            for edge in edges:
                current = distance[edge[0]][edge[1]]
                new = distance[node[0]][node[1]] + \
                    self.maze[edge[0]][edge[1]]
                if new < current:
                    distance[edge[0]][edge[1]] = new
                    new += (edge[0] - end[0]) ** 2 + \
                        (edge[1] - end[1]) ** 2
                    priority_queue.put((new, edge))
                    parents[edge] = node

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

    print(results)
    for i in results:
        print()
        print(len(i))
