import pygame.display
from pygame import mixer
from GraphicManager import GraphicManager
from MainMenuState import MainMenuState
from SoundManager import SoundManager


class Game:
    shouldCloseWindow = False
    graphicManager = None
    soundManager = None
    stateVector = []

    def __init__(self):
        self.graphicManager = GraphicManager()
        self.soundManager = SoundManager()
        self.stateVector.append(MainMenuState(self.graphicManager, self.soundManager, self))
        self.execute()

    def execute(self):
        while not self.graphicManager.shouldCloseWindow() and not self.shouldCloseWindow:
            self.graphicManager.fill()
            self.stateVector[-1].execute()
            pygame.display.update()
            print(self.stateVector)
            print(self.stateVector[-1])

    def addState(self, state):
        self.stateVector.append(state)

    def removeLastState(self):
        self.stateVector.pop(-1)

    def setShouldCloseWindowTrue(self):
        self.shouldCloseWindow = True
