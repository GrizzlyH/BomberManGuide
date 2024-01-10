import pygame
import gamesettings as gs


class Game:
    def __init__(self, main, assets):
        #  Link with the Main and Assets Classes
        self.MAIN = main
        self.ASSETS = assets


    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()


    def update(self):
        pass


    def draw(self, window):
        window.fill((188, 188, 188))


    def quit_game(self):
        """"Access main Object Class and switch the Run boolean to False"""
        self.MAIN.run = False