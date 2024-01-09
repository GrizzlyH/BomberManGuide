import pygame


class BomberMan:
    def __init__(self):
        pygame.init()   #  Init pygame module

        self.screen = pygame.display.set_mode((1280, 892))
        self.FPS = pygame.time.Clock()

        self.run = True


    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False


    def update(self):
        self.FPS.tick(60)   #  The speed at which pygame will update each cycle


    def draw(self, window):
        window.fill((0, 0, 0))  #  Fill the screen with a black colour
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
