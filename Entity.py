import pygame
from abc import ABC, abstractmethod
from GraphicManager import GraphicManager


class Entity(ABC):
    coordX = 0
    coordY = 0

    image = None
    rect = None
    graphicManager = None

    def __init__(self, gp, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.coordX = x
        self.coordY = y
        self.graphicManager = gp

    def setGraphicManager(self, gp):
        self.graphicManager = gp

    def draw(self):
        self.graphicManager.draw(self.image, (self.coordX, self.coordY))

    @abstractmethod
    def execute(self):
        pass
