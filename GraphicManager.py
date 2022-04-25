import pygame


class GraphicManager:
    size = width, height = 1024, 576
    screen = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

    def draw(self, figure, position):
        self.screen.blit(figure, position)

    def fill(self):
        self.screen.fill((0, 0, 0))

    def closeWindow(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
