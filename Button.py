import pygame
from Entity import Entity
from GraphicManager import GraphicManager


class Button(Entity):
    def __init__(self, gp, imageDir):
        Entity.__init__(self, gp, imageDir)
        self.image = pygame.image.load(imageDir)
        self.rect = self.image.get_rect()
