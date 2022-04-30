from abc import ABC, abstractmethod


class State(ABC):
    game = None
    graphicManager = None
    soundManager = None

    def __init__(self, gp, sd, game):
        self.graphicManager = gp
        self.soundManager = sd
        self.game = game

    @abstractmethod
    def execute(self):
        pass
