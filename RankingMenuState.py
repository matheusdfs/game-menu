import pygame
import psycopg2

from Text import Text
from Button import Button
from MenuState import MenuState
from Background import Background

class RankingMenuState(MenuState):
    con = None
    cur = None
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
            self.con = psycopg2.connect(host="localhost", user="postgres", password="postgres", dbname="operation")
            self.initializeEntityConnectionSuccessful()
        except psycopg2.Error as err:
            print(err)
            self.initializeEntityConnectionError()

    def initializeEntityConnectionSuccessful(self):
        self.cur = self.con.cursor()
        query = ("select p.name, s.score, l.name from game.score s inner join game.player p on s.player_id = p.id inner join game.level l on s.level_id = l.id order by s.score desc limit 5;")

        self.cur.execute(query)

        recset = self.cur.fetchall()

        for (name, score, lvl_name) in recset:
            self.coordYRanking = self.coordYRanking + 50
            aux = Text(
                self.graphicManager,
                self.soundManager,
                25,
                self.coordYRanking,
                name + " " + str(score) + " " + lvl_name
            )

            self.entityArray.append(aux)

        self.cur.close()
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
            elif code == 'back' and not self.backButtonControl:
                if self.con:
                    self.con.close()
                self.game.removeLastState()
                self.backButtonControl = True
