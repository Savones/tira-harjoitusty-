import pygame

GREEN = (198, 235, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (219, 50, 77)


class UI:
    def __init__(self, logic) -> None:
        self.logic = logic
        self.screen = pygame.display.set_mode([800, 900])

    def start(self):
        pygame.init()
        pygame.display.set_caption('Luolaston generointi työkalu')
        self.screen.fill(WHITE)

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(300, 825, 200, 50).collidepoint(event.pos):
                        rooms = self.logic.generate_rooms(10)
                        for room in rooms:
                            self.create_rect(
                                GREEN, (room.x, room.y, room.width, room.height))
            self.draw_backgroud()
            pygame.display.flip()
        pygame.quit()

    def draw_backgroud(self):
        self.create_rect(RED, [0, 800, 800, 100])
        self.create_rect(BLACK, [300, 825, 200, 50])
        self.create_text('Generoi luolasto', WHITE,
                         (312, 838), pygame.font.Font('freesansbold.ttf', 22))

    def create_rect(self, color, position):
        pygame.draw.rect(self.screen, color, position)

    def create_text(self, text, color, position, font):
        text_rect = font.render(text, True,
                                color)
        self.screen.blit(text_rect, position)
