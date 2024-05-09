import pygame

GREEN = (198, 235, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (219, 50, 77)
BLUE = (0, 0, 255)
ORANGE = (255, 140, 0)

GENERATE_BUTTON = 500, 925, 200, 50
STAGES_BUTTON = 200, 925, 200, 50
FIVE_BUTTON = 800, 925, 50, 50
TEN_BUTTON = 860, 925, 50, 50
TWENTY_BUTTON = 920, 925, 50, 50
THIRTY_BUTTON = 980, 925, 50, 50
FORTY_BUTTON = 1040, 925, 50, 50


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka

    Attributes:
        logic: Logic luokan olio
    """

    def __init__(self, logic) -> None:
        self.logic = logic
        self.screen = pygame.display.set_mode([1200, 1000])
        self.triangles_button = 0
        self.generate_button = False
        self.rooms, self.room_vertices, self.triangulation, self.chosen_edges, self.a_star_paths = [], [], [], [], []
        self.room_amount = 5
        self.changed_amount = ('5', FIVE_BUTTON)

    def start(self) -> None:
        """Käynnistää ohjelman
        """

        pygame.init()
        pygame.display.set_caption('Luolaston generointi työkalu')
        self.screen.fill(WHITE)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(GENERATE_BUTTON).collidepoint(event.pos):
                        self.handle_generate_click()
                    if pygame.Rect(STAGES_BUTTON).collidepoint(event.pos) and self.generate_button:
                        self.handle_show_stages_click()

                    if pygame.Rect(FIVE_BUTTON).collidepoint(event.pos):
                        self.room_amount = 5
                        self.changed_amount = ('5', FIVE_BUTTON)
                    if pygame.Rect(TEN_BUTTON).collidepoint(event.pos):
                        self.room_amount = 10
                        self.changed_amount = ('10', TEN_BUTTON)
                    if pygame.Rect(TWENTY_BUTTON).collidepoint(event.pos):
                        self.room_amount = 20
                        self.changed_amount = ('20', TWENTY_BUTTON)
                    if pygame.Rect(THIRTY_BUTTON).collidepoint(event.pos):
                        self.room_amount = 30
                        self.changed_amount = ('30', THIRTY_BUTTON)
                    if pygame.Rect(FORTY_BUTTON).collidepoint(event.pos):
                        self.room_amount = 40
                        self.changed_amount = ('40', FORTY_BUTTON)

            self.draw_backgroud()
            pygame.display.flip()
        pygame.quit()

    def handle_amount_click(self) -> None:
        """Huolehtii muutoksista, kun käyttäjä vaihtaa generoitavien huoneiden määrää
        """

        self.draw_amount_buttons()
        self.create_rect(BLACK, self.changed_amount[1])
        self.create_text(self.changed_amount[0], WHITE,
                         (self.changed_amount[1][0] + 15, 938), pygame.font.Font('freesansbold.ttf', 22))

    def handle_generate_click(self) -> None:
        """Huolehtii generointinapin painalluksen jälkisistä toimista
        """

        self.logic.reset()
        self.rooms = self.logic.generate_rooms(self.room_amount)
        self.room_vertices = self.logic.generate_room_vertices()
        self.triangulation = self.logic.get_triangulation()
        self.mst = self.logic.get_mst(self.triangulation[1])
        self.chosen_edges = self.logic.get_chosen_edges()
        self.a_star_paths = self.logic.get_a_star_paths()

        self.generate_button = True
        self.triangles_button = 0

        self.background_reset()
        self.show_a_star_paths()
        self.show_rooms()

    def handle_show_stages_click(self) -> None:
        """Huolehtii näytä vaihteet-napin painalluksen jälkeisistä toimista
        """

        self.triangles_button += 1
        if self.triangles_button == 1:
            self.background_reset()

        elif self.triangles_button == 2:
            self.show_triangles()

        elif self.triangles_button == 3:
            self.show_circles()

        elif self.triangles_button == 4:
            self.show_triangulation()

        elif self.triangles_button == 5:
            self.background_reset()
            self.show_triangulation()

        elif self.triangles_button == 6:
            self.show_mst()

        elif self.triangles_button == 7:
            self.background_reset()
            self.show_mst()

        elif self.triangles_button == 8:
            self.background_reset()
            self.show_chosen_edges()

        else:
            self.background_reset()
            self.show_a_star_paths()
            self.show_rooms()
            self.triangles_button = 0

    def background_reset(self) -> None:
        """Piirtää taustan uudelleen
        """

        self.screen.fill(WHITE)
        self.draw_backgroud()
        self.show_rooms()

    def show_chosen_edges(self) -> None:
        """Piirtää mst + arvottuja käytäviä kuvaavat suorat
        """

        for edge in self.chosen_edges:
            pygame.draw.line(self.screen, ORANGE, edge[0], edge[1], 3)

    def show_mst(self):
        """Piirtää mst:n käytäviä kuvaaavat suorat
        """

        for edge in self.mst:
            pygame.draw.line(self.screen, RED, edge[0], edge[1], 3)

    def show_rooms(self) -> None:
        """Piirtää huoneet
        """

        for room in self.rooms:
            self.create_rect(
                GREEN, (room.x, room.y, room.width, room.height))

    def show_triangles(self) -> None:
        """Piirtää kolmioinnin, mukaan lukien superkolmion
        """

        for triangle in self.triangulation[0]:
            vertices = [(triangle.vertex1.x, triangle.vertex1.y),
                        (triangle.vertex2.x, triangle.vertex2.y),
                        (triangle.vertex3.x, triangle.vertex3.y)]
            self.create_polygon(RED, vertices, 1)

    def show_triangulation(self) -> None:
        """Piirtää lopullisen kolmioinnin
        """

        for triangle in self.triangulation[1]:
            vertices = [(triangle.vertex1.x, triangle.vertex1.y),
                        (triangle.vertex2.x, triangle.vertex2.y),
                        (triangle.vertex3.x, triangle.vertex3.y)]
            self.create_polygon(BLUE, vertices, 2)

    def show_circles(self) -> None:
        """Piirtää kolmioiden ulkoympyrät
        """

        for triangle in self.triangulation[0]:
            self.create_circle(
                BLACK, triangle.circum_center, triangle.radius, 1)

    def show_a_star_paths(self) -> None:
        """Piirtää A* polut
        """

        for path in self.a_star_paths:
            for point in path:
                self.create_rect(
                    RED, [point[0] - 3, point[1] - 3, 6, 6])

    def draw_amount_buttons(self) -> None:
        """Piirtää huoneiden määrä muuttavat napit
        """

        self.create_rect(WHITE, [800, 925, 50, 50])
        self.create_rect(WHITE, [860, 925, 50, 50])
        self.create_rect(WHITE, [920, 925, 50, 50])
        self.create_rect(WHITE, [980, 925, 50, 50])
        self.create_rect(WHITE, [1040, 925, 50, 50])

        self.create_text('5', BLACK,
                         (815, 938), pygame.font.Font('freesansbold.ttf', 22))
        self.create_text('10', BLACK,
                         (875, 938), pygame.font.Font('freesansbold.ttf', 22))
        self.create_text('20', BLACK,
                         (935, 938), pygame.font.Font('freesansbold.ttf', 22))
        self.create_text('30', BLACK,
                         (995, 938), pygame.font.Font('freesansbold.ttf', 22))
        self.create_text('40', BLACK,
                         (1055, 938), pygame.font.Font('freesansbold.ttf', 22))

    def draw_backgroud(self) -> None:
        """Piirtää taustan
        """

        self.create_rect(RED, [0, 900, 1200, 100])
        self.create_rect(BLACK, [500, 925, 200, 50])

        self.handle_amount_click()

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
