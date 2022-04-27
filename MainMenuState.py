from MenuState import MenuState
from Button import Button


class MainMenuState(MenuState):
    playButton = None

    def __init__(self, gp):
        MenuState.__init__(self, "MainMenu")
        self.graphicManager = gp
        self.playButton = Button(gp, 'img/landscapeMainMenu.png')

    def execute(self):
        self.playButton.draw()
