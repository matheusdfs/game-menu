import pygame.display
from pygame import mixer
from GraphicManager import GraphicManager
from MainMenuState import MainMenuState
from SoundManager import SoundManager

from SingleGameState import SingleGameState
from OnlineGameState import OnlineGameState
from MultiLocalGameState import MultiLocalGameState

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

    def addState(self, state):
        self.stateVector.append(state)

    def removeLastState(self):
        self.stateVector.pop(-1)

    def setShouldCloseWindowTrue(self):
        self.shouldCloseWindow = True

    def initSingleplayer(self):
        self.addState(SingleGameState(self.graphicManager, self.soundManager, self))

    def initMultiplayer(self):
        self.addState(OnlineGameState(self.graphicManager, self.soundManager, self))
    
    def initLocal(self):
        self.addState(MultiLocalGameState(self.graphicManager, self.soundManager, self))