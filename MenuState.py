from abc import ABC, abstractmethod
from State import State


class MenuState(State, ABC):
    background = None

    def __init__(self, gp, sd, game):
        State.__init__(self, gp, sd, game)

    @abstractmethod
    def execute(self):
        pass
