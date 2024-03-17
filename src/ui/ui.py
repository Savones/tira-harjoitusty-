import pygame


class UI():
    def __init__(self, logic) -> None:
        self.logic = logic

    def start(self):
        pygame.init()

        screen = pygame.display.set_mode([800, 900])
        pygame.display.set_caption('Luolaston generointi työkalu')

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_backgroud(screen)

            pygame.display.flip()

        pygame.quit()

    def draw_backgroud(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (219, 50, 77), [0, 800, 800, 100])
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render('Generoi luolasto', True,
                           (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (400, 850)
        screen.blit(text, textRect)
