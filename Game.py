from GraphicManager import GraphicManager

import sys


class Game:
    graphicManager = None
    stateVector = None

    def __init__(self):
        self.graphicManager = GraphicManager()
        # push no stateVector do stateMenu

    def execute(self):
        while not self.graphicManager.closeWindow():
            print("execute last state")
