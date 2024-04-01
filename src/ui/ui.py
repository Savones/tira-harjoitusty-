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
                        self.logic.reset()
                        self.screen.fill(WHITE)

                        rooms = self.logic.generate_rooms(4)
                        room_vertices = self.logic.generate_room_vertices()
                        triangulation = self.logic.get_triangulation()

                        for room in rooms:
                            self.create_rect(
                                GREEN, (room.x, room.y, room.width, room.height))

                        for vertex in room_vertices:
                            self.create_circle(BLACK, vertex, 5, 0)
                            self.create_text(str(vertex), BLACK, vertex, pygame.font.Font(
                                'freesansbold.ttf', 22))

                        for triangle in triangulation[0]:
                            vertices = [(triangle.vertex1.x, triangle.vertex1.y),
                                        (triangle.vertex2.x, triangle.vertex2.y),
                                        (triangle.vertex3.x, triangle.vertex3.y)]
                            pygame.draw.polygon(
                                self.screen, RED, vertices, 1)

                        for triangle in triangulation[1]:
                            vertices = [(triangle.vertex1.x, triangle.vertex1.y),
                                        (triangle.vertex2.x, triangle.vertex2.y),
                                        (triangle.vertex3.x, triangle.vertex3.y)]
                            pygame.draw.polygon(
                                self.screen, BLUE, vertices, 2)
                            pygame.draw.circle(
                                self.screen, BLACK, triangle.circum_center, triangle.radius, 1, )

            self.draw_backgroud()
            pygame.display.flip()
        pygame.quit()

    def draw_backgroud(self) -> None:
        self.create_rect(RED, [0, 900, 1200, 100])
        self.create_rect(BLACK, [500, 925, 200, 50])
        self.create_text('Generoi luolasto', WHITE,
                         (512, 938), pygame.font.Font('freesansbold.ttf', 22))

    def create_rect(self, color: tuple, position: list) -> None:
        pygame.draw.rect(self.screen, color, position)

    def create_text(self, text: str, color: tuple, position: list, font) -> None:
        text_rect = font.render(text, True,
                                color)
        self.screen.blit(text_rect, position)

    def create_circle(self, color: tuple, center: tuple, radius: int, filled: int):
        pygame.draw.circle(self.screen, color, center, radius, filled)
