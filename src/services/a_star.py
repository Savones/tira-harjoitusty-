from queue import PriorityQueue


class Node:
    def __init__(self, position):
        self.f = 0
        self.position = position

    def __eq__(self, other):
        return self.position == other.position


class Astar:
    def __init__(self):
        self.maze = [[10] * 900 for _ in range(1200)]

    def add_rooms_to_maze(self, room_list: list):
        """Lisää huoneisiin seinät, joiden läpi käytävät eivät voi kulkea

        Args:
            room_list (list): Huoneet listana
        """
        for room in room_list:
            door_1 = room.x + room.width // 2
            door_2 = room.y + room.height // 2

            for i in range(room.width - 10, room.width + 10):
                if i == (room.width // 2):
                    self.maze[door_1][room.y] = 0
                    self.maze[door_1][room.y + (room.height - 1)] = 0
                    continue
                self.maze[room.x + i][room.y] = 100
                self.maze[room.x + i][room.y + (room.height - 1)] = 100

            for j in range(room.height - 10, room.height + 10):
                if j == (room.height // 2):
                    self.maze[room.x][door_2] = 0
                    self.maze[room.x + (room.width - 1)][door_2] = 0
                    continue
                self.maze[room.x][room.y + j] = 100
                self.maze[room.x + (room.width - 1)][room.y + j] = 100

    def get_astar_paths(self, paths, room_list):
        self.add_rooms_to_maze(room_list)
        results = []

        for path in paths:
            start = path[0].vertex
            end = path[1].vertex

            results.append(self.run_astar(start, end))

        return results

    def run_astar(self, alku, loppu):
        keko = PriorityQueue()
        etaisyys = [[float('inf')] * 900 for _ in range(1200)]
        kasitelty = [[False] * 900 for _ in range(1200)]
        vanhemmat = {}

        keko.put((0, alku))
        etaisyys[alku[0]][alku[1]] = 0

        while not keko.empty():
            solmu = keko.get()[1]

            if solmu == loppu:
                path = []
                while solmu in vanhemmat:
                    path.append(solmu)
                    self.update_maze(solmu)
                    solmu = vanhemmat[solmu]
                path.append(alku)
                return path[::-1]

            if kasitelty[solmu[0]][solmu[1]]:
                continue

            if self.maze[solmu[0]][solmu[1]] == 100:
                continue

            kasitelty[solmu[0]][solmu[1]] = True

            kaaret = [(solmu[0] + 1, solmu[1]),
                      (solmu[0] - 1, solmu[1]),
                      (solmu[0], solmu[1] + 1),
                      (solmu[0], solmu[1] - 1)]

            for kaari in kaaret:
                nyky = etaisyys[kaari[0]][kaari[1]]
                uusi = etaisyys[solmu[0]][solmu[1]] + \
                    self.maze[kaari[0]][kaari[1]]
                if uusi < nyky:
                    etaisyys[kaari[0]][kaari[1]] = uusi
                    uusi += (kaari[0] - loppu[0]) ** 2 + \
                        (kaari[1] - loppu[1]) ** 2
                    keko.put((uusi, kaari))
                    vanhemmat[kaari] = solmu

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
