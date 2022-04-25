from abc import ABC
from State import State
from GraphicManager import GraphicManager


class MainMenuState(State, ABC):
    graphicManager = None

    def __init__(self, gp):
        State.__init__(self, "MainMenu")
        self.graphicManager = gp

    def execute(self):
        print(self.name)
