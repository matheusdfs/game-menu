from abc import ABC, abstractmethod
from State import State


class MenuState(State, ABC):
    def __init__(self, gp):
        State.__init__(self, "MainMenu", gp)

    @abstractmethod
    def execute(self):
        pass
