
import pygame
from Background import Background
from State import State
from Button import Button
from Server import Server

class OnlineGameState(State):
    backButtonControl = False
    def __init__(self, gp, sd, game):
        State.__init__(self, gp, sd, game)
        self.entityArray = []
        self.server = Server()
        self.server.createServer()
        image = pygame.image.load('img/multiPlayerButton.png').convert_alpha()

        aux = Background(
            self.graphicManager,
            self.soundManager,
            image,
            self.graphicManager.getScreenWidth() / 4 - image.get_rect().width / 2,
            self.graphicManager.getScreenHeight() / 2 + 50
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
    def execute(self):
        for entity in self.entityArray:
            code = entity.execute()
            if code == '':
                pass
            elif code == 'back' and not self.backButtonControl:
                self.game.removeLastState()
                self.backButtonControl = True