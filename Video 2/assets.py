import pygame
import gamesettings as gs


class Assets:
    def __init__(self):
        self.spritesheet = self.load_sprite_sheet("images", "spritesheet.png")


    def load_sprite_sheet(self, path, filename):
        """Load in the sprite sheet image"""
        image = pygame.image.load(f"{path}/{filename}").convert_alpha()
        image = pygame.transform.scale(image, (192*4, 272*4))
        return image