import pygame
from abc import ABC
from GraphicManager import GraphicManager


class Entity(ABC):
    coordX = 0
    coordY = 0

    image = None
    rect = None
    graphicManager = None

    def __init__(self, gp, imageDir):
        self.image = pygame.image.load(imageDir)
        self.rect = self.image.get_rect()
        self.graphicManager = gp

    def setGraphicManager(self, gp):
        self.graphicManager = gp

    def draw(self):
        self.graphicManager.draw(self.image, (self.coordX, self.coordY))
