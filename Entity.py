import pygame
from GraphicManager import GraphicManager


class Entity:
    image = None
    rect = None

    def __init__(self, imageDir):
        self.image = pygame.image.load(imageDir)
        self.rect = self.image.get_rect()
