from abc import ABC, abstractmethod


class State(ABC):
    name = ""
    graphicManager = None

    def __init__(self, name, gp):
        self.name = name
        self.graphicManager = gp

    @abstractmethod
    def execute(self):
        pass
