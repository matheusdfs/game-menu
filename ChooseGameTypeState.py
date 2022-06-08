import pygame

from MenuState import MenuState
from Button import Button
from Background import Background


class ChooseGameTypeState(MenuState):
    backButtonControl = False

    def __init__(self, gp, sd, game):
        MenuState.__init__(self, gp, sd, game)

        self.entityArray = []

        image = pygame.image.load('img/landscapeMainMenu.png').convert_alpha()

        aux = Background(
            gp,
            sd,
            image,
            0,
            0
        )

        self.entityArray.append(aux)

    def execute(self):
        for entity in self.entityArray:
            code = entity.execute()
            if code == '':
                pass
            elif code == '100%':
                self.soundManager.setVolume(1.0)
            elif code == '50%':
                self.soundManager.setVolume(0.5)
            elif code == '10%':
                self.soundManager.setVolume(0.1)
            elif code == 'back' and not self.backButtonControl:
                self.game.removeLastState()
                self.backButtonControl = True
