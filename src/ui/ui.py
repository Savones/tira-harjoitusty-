import pygame

GREEN = (198, 235, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (219, 50, 77)
BLUE = (0, 0, 255)


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka
    """

    def __init__(self, logic) -> None:
        self.logic = logic
        self.screen = pygame.display.set_mode([1200, 1000])
        self.triangles_button = 0
        self.generate_button = False
        self.rooms = []
        self.room_vertices = []
        self.triangulation = []

    def start(self) -> None:
        pygame.init()
        pygame.display.set_caption('Luolaston generointi työkalu')
        self.screen.fill(WHITE)

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(500, 925, 200, 50).collidepoint(event.pos):
                        self.handle_generate_click()
                        self.background_reset()
                        self.show_triangulation()

                    if pygame.Rect(200, 925, 200, 50).collidepoint(event.pos) and self.generate_button:
                        self.triangles_button += 1
                        if self.triangles_button == 1:
                            self.background_reset()
                            self.show_room_vertices()

                        elif self.triangles_button == 2:
                            self.show_triangles()

                        elif self.triangles_button == 3:
                            self.show_circles()

                        elif self.triangles_button == 4:
                            self.show_triangulation()

                        else:
                            self.background_reset()
                            self.show_triangulation()
                            self.triangles_button = 0

            self.draw_backgroud()
            pygame.display.flip()
        pygame.quit()

    def handle_generate_click(self):
        self.logic.reset()
        self.rooms = self.logic.generate_rooms(15)
        self.room_vertices = self.logic.generate_room_vertices()
        self.triangulation = self.logic.get_triangulation()

        self.generate_button = True
        self.triangles_button = 0

    def background_reset(self):
        self.screen.fill(WHITE)
        self.draw_backgroud()
        self.show_rooms()

    def show_rooms(self):
        for room in self.rooms:
            self.create_rect(
                GREEN, (room.x, room.y, room.width, room.height))

    def show_room_vertices(self):
        for vertex in self.room_vertices:
            self.create_circle(BLACK, vertex, 5, 0)
            self.create_text(str(vertex), BLACK, vertex, pygame.font.Font(
                'freesansbold.ttf', 22))

    def show_triangles(self):
        for triangle in self.triangulation[0]:
            vertices = [(triangle.vertex1.x, triangle.vertex1.y),
                        (triangle.vertex2.x, triangle.vertex2.y),
                        (triangle.vertex3.x, triangle.vertex3.y)]
            self.create_polygon(RED, vertices, 1)

    def show_triangulation(self):
        for triangle in self.triangulation[1]:
            vertices = [(triangle.vertex1.x, triangle.vertex1.y),
                        (triangle.vertex2.x, triangle.vertex2.y),
                        (triangle.vertex3.x, triangle.vertex3.y)]
            self.create_polygon(BLUE, vertices, 2)

    def show_circles(self):
        for triangle in self.triangulation[0]:
            self.create_circle(
                BLACK, triangle.circum_center, triangle.radius, 1)

    def draw_backgroud(self) -> None:
        self.create_rect(RED, [0, 900, 1200, 100])
        self.create_rect(BLACK, [500, 925, 200, 50])
        self.create_text('Generoi luolasto', WHITE,
                         (512, 938), pygame.font.Font('freesansbold.ttf', 22))
        self.create_rect(BLACK, [200, 925, 200, 50])
        self.create_text('Näytä vaihteet', WHITE,
                         (212, 938), pygame.font.Font('freesansbold.ttf', 22))

    def create_rect(self, color: tuple, position: list) -> None:
        pygame.draw.rect(self.screen, color, position)

    def create_text(self, text: str, color: tuple, position: list, font) -> None:
        text_rect = font.render(text, True,
                                color)
        self.screen.blit(text_rect, position)

    def create_circle(self, color: tuple, center: tuple, radius: int, filled: int):
        pygame.draw.circle(self.screen, color, center, radius, filled)

    def create_polygon(self, color: tuple, vertices: list, width):
        pygame.draw.polygon(
            self.screen, color, vertices, width)
