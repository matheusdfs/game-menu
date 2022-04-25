from abc import abstractmethod


class State:
    name = ""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        pass
