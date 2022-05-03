from abc import ABC

import pygame
from Entity import Entity


class Button(Entity, ABC):
    name = None
    soundButton = False

    def __init__(self, gp, sd, image, x, y, name):
        Entity.__init__(self, gp, sd, image, x, y)
        self.name = name

    def execute(self):
        self.draw()
        if self.rect.collidepoint(self.graphicManager.getMousePosition()):
            if not self.soundButton:
                self.soundManager.playSound('sounds/button-sound.wav')
                self.soundButton = True

            if pygame.mouse.get_pressed()[0] == 1:
                return self.name
        else:
            self.soundButton = False
        return ''
