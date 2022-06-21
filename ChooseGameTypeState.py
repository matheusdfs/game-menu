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

        image = pygame.image.load('img/singlePlayerButton.png').convert_alpha()

        # Initializing the play button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 0,
            'play'
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/multiPlayerButton.png').convert_alpha()

        # Initializing the play button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 100,
            'play'
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/localButton.png').convert_alpha()

        # Initializing the play button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 200,
            'play'
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/back.png').convert_alpha()

        aux = Button(
            gp,
            sd,
            image,
            25,
            25,
            'back'
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
