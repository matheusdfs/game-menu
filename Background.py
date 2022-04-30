from abc import ABC

import pygame
from Entity import Entity
from GraphicManager import GraphicManager


class Background(Entity, ABC):
    def __init__(self, gp, image, x, y):
        Entity.__init__(self, gp, image, x, y)
        self.rect = self.image.get_rect()

    def execute(self):
        self.draw()
