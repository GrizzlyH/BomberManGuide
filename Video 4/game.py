import pygame
from character import Character
import gamesettings as gs


class Game:
    def __init__(self, main, assets):
        #  Link with the Main and Assets Classes
        self.MAIN = main
        self.ASSETS = assets

        self.player_group = pygame.sprite.Group()
        self.player = Character(self, self.ASSETS.player_char, self.player_group, 0, 0, 64)


    def input(self):
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        self.quit_game()
        self.player.input()


    def update(self):
        self.player_group.update()


    def draw(self, window):
        window.fill((188, 188, 188))
        self.player_group.draw(window)


    def quit_game(self):
        """"Access main Object Class and switch the Run boolean to False"""
        self.MAIN.run = False