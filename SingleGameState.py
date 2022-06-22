from lib2to3.pygram import python_grammar_no_print_statement


import pygame
from Background import Background
from State import State
from Button import Button

class SingleGameState(State):
    backButtonControl = False

    def __init__(self, gp, sd, game):
        State.__init__(self, gp, sd, game)
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

        image = pygame.image.load('img/back.png').convert_alpha()

        aux = Button(
            self.graphicManager,
            self.soundManager,
            image,
            self.graphicManager.getScreenWidth() / 4 - image.get_rect().width / 2,
            100,
            'back'
        )
        self.entityArray.append(aux)
        image = pygame.image.load('img/singlePlayerButton.png').convert_alpha()
        aux = Button(
            self.graphicManager,
            self.soundManager,
            image,
            self.graphicManager.getScreenWidth() / 4 - image.get_rect().width / 2,
            self.graphicManager.getScreenHeight() / 2 + 50,
            "b"
        )

        self.entityArray.append(aux)
        
        image = pygame.image.load('img/wall3.png').convert_alpha()

        for i in range(0, 20):
            aux = Button(
                self.graphicManager,
                self.soundManager,
                image,
                image.get_rect().width*i,
                self.graphicManager.getScreenHeight() / 2 + image.get_rect().height*6,
                'a'
            )

            self.entityArray.append(aux)
    def execute(self):
        for entity in self.entityArray:
            code = entity.execute()
            if code == '':
                pass
            elif code == 'back' and not self.backButtonControl:
                self.game.removeLastState()
                self.backButtonControl = True