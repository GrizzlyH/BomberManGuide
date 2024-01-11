import pygame
import gamesettings as gs


class Assets:
    def __init__(self):
        self.spritesheet = self.load_sprite_sheet("images", "spritesheet.png")

        self.player_char = self.load_sprites_range(gs.PLAYER, self.spritesheet)


    def load_sprite_sheet(self, path, filename):
        """Load in the sprite sheet image"""
        image = pygame.image.load(f"{path}/{filename}").convert_alpha()
        image = pygame.transform.scale(image, (192*4, 272*4))
        return image


    def load_sprites(self, spritesheet, row, col, width, height):
        """Load an individual sprite image"""
        image = pygame.Surface((width, height)) #  Generate a blank surface
        image.fill((0, 0, 1))   #  Fill the surface with a color
        image.blit(spritesheet, (0, 0), (row, col, width, height))  #  Blit the sprite at coords onto surface
        image.set_colorkey((0, 0, 0))
        return image

    def load_sprites_range(self, image_dict, spritesheet):
        """Return a dictionary containing a list of images for the various animations"""
        animation_images = {}
        for animation in image_dict.keys():
            animation_images[animation] = []
            for coord in image_dict[animation]:
                image = self.load_sprites(spritesheet, coord[1] * 64, coord[0] * 64, 64, 64)
                animation_images[animation].append(image)
        return animation_images