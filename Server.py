import pygame

class Server():
    num_server = 0
    def __init__(self):
        self.num_server += 1
    def createServer(self):
        print("O Servidor " + str(self.num_server) + " foi Criado!")