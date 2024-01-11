import pygame
from assets import Assets
from game import Game
import gamesettings as gs


class BomberMan:
    def __init__(self):
        pygame.init()   #  Init pygame module

        self.screen = pygame.display.set_mode((gs.SCREENWIDTH, gs.SCREENHEIGHT))
        pygame.display.set_caption("BomberMan")
        self.FPS = pygame.time.Clock()

        self.assets = Assets()
        self.game = Game(self, self.assets)

        self.run = True


    def input(self):
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #self.run = False
        self.game.input()


    def update(self):
        self.FPS.tick(60)   #  The speed at which pygame will update each cycle
        self.game.update()


    def draw(self, window):
        window.fill((0, 0, 0))  #  Fill the screen with a black colour
        self.game.draw(window)
        pygame.display.update()


    def rungame(self):
        while self.run:
            self.input()
            self.update()
            self.draw(self.screen)


if __name__=="__main__":
    game = BomberMan()
    game.rungame()
    pygame.quit()