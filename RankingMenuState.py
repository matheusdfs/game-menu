import pygame
import mysql.connector

from Text import Text
from Button import Button
from MenuState import MenuState
from Background import Background


class RankingMenuState(MenuState):
    config = {
        'user': 'root',
        'password': 'root123',
        'host': 'localhost',
    }

    con = None
    backButtonControl = False
    coordYRanking = 200

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

        # connect to the database
        try:
            self.con = mysql.connector.connect(**self.config)
            self.initializeEntityConnectionSuccessful()
        except mysql.connector.Error as err:
            print(err)
            self.initializeEntityConnectionError()

    def initializeEntityConnectionSuccessful(self):
        cursor = self.con.cursor(buffered=True)
        query = ("select player.name, score.score, level.name as lvl_name from game_menu.score left join "
                 "game_menu.player on score.player_id = player.id left join game_menu.level on score.level_id = "
                 "level.id order by score desc limit 5;")

        cursor.execute(query)

        for (name, score, lvl_name) in cursor:
            self.coordYRanking = self.coordYRanking + 50
            aux = Text(
                self.graphicManager,
                self.soundManager,
                25,
                self.coordYRanking,
                name + " " + str(score) + " " + lvl_name
            )

            self.entityArray.append(aux)

        cursor.close()
        self.con.close()

        image = pygame.image.load('img/back.png').convert_alpha()

        aux = Button(
            self.graphicManager,
            self.soundManager,
            image,
            25,
            25,
            'back'
        )

        self.entityArray.append(aux)

    def initializeEntityConnectionError(self):
        image = pygame.image.load('img/connectionError.png').convert_alpha()

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
            elif code == '100%':
                self.soundManager.setVolume(1.0)
            elif code == '50%':
                self.soundManager.setVolume(0.5)
            elif code == '10%':
                self.soundManager.setVolume(0.1)
            elif code == 'back' and not self.backButtonControl:
                if self.con:
                    self.con.close()
                self.game.removeLastState()
                self.backButtonControl = True
