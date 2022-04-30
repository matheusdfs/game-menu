from abc import ABC

import pygame
from Entity import Entity
from GraphicManager import GraphicManager


class Button(Entity, ABC):
    name = None

    def __init__(self, gp, image, x, y, name):
        Entity.__init__(self, gp, image, x, y)
        self.name = name

    def execute(self):
        self.draw()
        if self.rect.collidepoint(self.graphicManager.getMousePosition()) and pygame.mouse.get_pressed()[0] == 1:
            return self.name
        return ''
