import pygame.display

from GraphicManager import GraphicManager
from MainMenuState import MainMenuState


class Game:
    graphicManager = None
    stateVector = []

    def __init__(self):
        self.graphicManager = GraphicManager()
        self.stateVector.append(MainMenuState(self.graphicManager))
        self.execute()

    def execute(self):
        while not self.graphicManager.windowIsOpen():
            self.graphicManager.fill()
            self.stateVector[-1].execute()
            pygame.display.update()
