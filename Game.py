from GraphicManager import GraphicManager
from MainMenuState import MainMenuState

class Game:
    graphicManager = None
    stateVector = []

    def __init__(self):
        self.graphicManager = GraphicManager()
        self.stateVector.append(MainMenuState())
        # push no stateVector do stateMenu

    def execute(self):
        while not self.graphicManager.closeWindow():
            self.stateVector[-1].execute()
