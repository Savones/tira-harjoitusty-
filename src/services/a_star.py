import math
from queue import PriorityQueue


class Astar:
    """Etsii huoneiden välille reitit A* algoritmilla
    """

    def __init__(self) -> None:
        self.maze = [[30] * 900 for _ in range(1200)]
        self.edges = {}

    def add_rooms_to_maze(self, room_list: list):
        """Lisää huoneisiin seinät ja ovet

        Args:
            room_list (list): Huoneet listana
        """

        for room in room_list:
            width = room.width + 40
            height = room.height + 40
            x = room.x - 20
            y = room.y - 20

            door_1 = x + (width // 2)
            door_2 = y + (height // 2)

            for i in range(x, x + width + 1):
                if i == door_1:
                    self.maze[door_1][y] = 1
                    self.maze[door_1][y + height] = 1
                    continue
                self.maze[i][y] = 100
                self.maze[i][y + height] = 100

            for j in range(y, y + height + 1):
                if j == door_2:
                    self.maze[x][door_2] = 1
                    self.maze[x + width][door_2] = 1
                    continue
                self.maze[x][j] = 100
                self.maze[x + width][j] = 100

    def make_edge_list(self) -> None:
        """Tekee kaarilistan solmujen naapureista
        """

        for i in range(1200):
            for j in range(900):
                self.edges[(i, j)] = []
                jj = j - 1
                if 0 < jj < 900:
                    self.edges[(i, j)].append((i, jj, self.maze[i][jj]))

                jj = j + 1
                if 0 < jj < 900:
                    self.edges[(i, j)].append((i, jj, self.maze[i][jj]))

                ii = i - 1
                if 0 < ii < 1200:
                    self.edges[(i, j)].append((ii, j, self.maze[ii][j]))

                ii = i + 1
                if 0 < ii < 1200:
                    self.edges[(i, j)].append((ii, j, self.maze[ii][j]))

    def get_astar_paths(self, paths: list, room_list: list) -> list:
        """Käy läpi A* algoritmin jokaisen käytävän päätepisteille

        Args:
            paths (list): lista kahdesta huoneesta koostuvia tupleja
            room_list (list): lista kaikista huone olioista

        Returns:
            list: lista listoja tupleista, jotka kuvaavat A* reittiä
        """

        self.add_rooms_to_maze(room_list)
        self.make_edge_list()
        results = []

        for path in paths:
            doors = self.choose_door(path[0], path[1])
            results.append(self.run_astar(doors[0], doors[1]))

        return results

    def run_astar(self, start: tuple, end: tuple) -> list:
        """Etsii reitin alkupisteestä päätepisteeseen

        Args:
            start (tuple): (x, y) koordinaatti alkupisteelle
            end (tuple): (x, y) koordinaatti päätepisteelle

        Returns:
            list: lista tupleja, jotka kuvaavat reittiä alusta loppuun
        """

        priority_queue = PriorityQueue()
        distance = [[float('inf')] * 900 for _ in range(1200)]
        visited = [[False] * 900 for _ in range(1200)]
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

            if visited[node[0]][node[1]]:
                continue

            visited[node[0]][node[1]] = True

            if self.maze[node[0]][node[1]] == 100:
                continue

            for edge in self.edges[node]:
                current = distance[edge[0]][edge[1]]
                new = distance[node[0]][node[1]] + edge[2]
                if new < current:
                    distance[edge[0]][edge[1]] = new
                    new += abs(edge[0] - end[0]) + abs(edge[1] - end[1])
                    priority_queue.put((new, (edge[0], edge[1])))
                    parents[(edge[0], edge[1])] = node

    def update_maze(self, pos: tuple) -> None:
        """Päivittää solmun painon, kun solmu on polussa

        Args:
            pos (tuple): (x, y) koordinaatti solmulle
        """

        self.maze[pos[0]][pos[1]] = 1

    def choose_door(self, start_room, end_room) -> tuple:
        """Valitsee kahdesta huoneesta ovet, jotka ovat lähimpänä toisiaan

        Args:
            start_room (Room): toinen huoneista
            end_room (Room): toinen huoneista

        Returns:
            tuple: tuple tupleja, jotka kuvaavat huoneiden ovien koordinaatteja
        """

        start_doors = self.get_doors(start_room)
        end_doors = self.get_doors(end_room)
        min_distance = float('inf')
        chosen_doors = None

        for start_door in start_doors:
            for end_door in end_doors:
                distance = math.sqrt(
                    (start_door[0] - end_door[0]) ** 2 + (start_door[1] - end_door[1]) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    chosen_doors = (start_door, end_door)

        return chosen_doors

    def get_doors(self, room) -> list:
        """Laskee huoneen ovien sijainnit

        Args:
            room (Room): Huone, jonka ovet lasketaan

        Returns:
            list: lista ovien koordinaatteja kuvaavia tupleja
        """

        doors = [(room.x + room.width // 2, room.y),
                 (room.x + room.width //
                  2, room.y + room.height),
                 (room.x, room.y + room.height // 2),
                 (room.x + room.width, room.y + room.height // 2)]

        return doors
