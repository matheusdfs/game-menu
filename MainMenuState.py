import pygame

from MenuState import MenuState
from Button import Button
from Background import Background
from OptionsMenuState import OptionsMenuState
from RankingMenuState import RankingMenuState


class MainMenuState(MenuState):
    def __init__(self, gp, sd, game):
        MenuState.__init__(self, gp, sd, game)

        self.entityArray = []

        image = pygame.image.load('img/landscapeMainMenu.png').convert_alpha()

        # Initializing the background of the mainMenu
        aux = Background(
            gp,
            sd,
            image,
            0,
            0
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/mainTitle.png').convert_alpha()

        # Initializing the title of the mainMenu
        aux = Background(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight()/4
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/playButton.png').convert_alpha()

        # Initializing the play button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 50,
            'play'
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/optionsButton.png').convert_alpha()

        # Initializing the config button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 100,
            'options'
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/rankingButton.png').convert_alpha()

        # Initializing the credits button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 150,
            'ranking'
        )

        self.entityArray.append(aux)

        image = pygame.image.load('img/exitButton.png').convert_alpha()

        # Initializing the exit button of the mainMenu
        aux = Button(
            gp,
            sd,
            image,
            gp.getScreenWidth() / 2 - image.get_rect().width / 2,
            gp.getScreenHeight() / 2 + 200,
            'exit'
        )

        self.entityArray.append(aux)

    def execute(self):
        for entity in self.entityArray:
            code = entity.execute()
            if code == '':
                pass
            elif code == 'play':
                print('Iniciando game')
            elif code == 'options':
                self.game.addState(OptionsMenuState(self.graphicManager, self.soundManager, self.game))
            elif code == 'ranking':
                self.game.addState(RankingMenuState(self.graphicManager, self.soundManager, self.game))
            elif code == 'exit':
                self.game.setShouldCloseWindowTrue()
