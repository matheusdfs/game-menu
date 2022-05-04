import pygame

from abc import ABC
from Entity import Entity


class Text(Entity, ABC):
    text = ''
    surface = None

    def __init__(self, gp, sd, x, y, text):
        Entity.__init__(self, gp, sd, None, x, y)
        self.text = text

        font = pygame.font.SysFont("verdana", 40)

        self.surface = font.render(text, True, (0, 0, 0))

    def draw(self):
        self.graphicManager.drawText(self.surface, (self.coordX, self.coordY))

    def execute(self):
        self.draw()
        return ''
