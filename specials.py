import pygame
import gamesettings as gs


class Special(pygame.sprite.Sprite):
    def __init__(self, game, image, name, group, row_num, col_num, size):
        super().__init__(group)
        self.GAME = game

        self.name = name

        #  Level Matrix Position
        self.row = row_num
        self.col = col_num

        #  x, y coordinates
        self.size = size
        self.x = self.col * self.size
        self.y = (self.row * self.size) + gs.Y_OFFSET

        #  Image
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        #  Power Up Abilities
        self.power_up_activate = {"bomb_up": self.bomb_up_special,
                                  "fire_up": self.fire_up_special,
                                  "speed_up": self.speed_up_special,
                                  "wall_hack": self.wall_hack_special,
                                  "remote": self.remote_special,
                                  "bomb_pass": self.bomb_hack_special,
                                  "flame_pass": self.flame_pass_special,
                                  "invincible": self.invincible_special}


    def update(self):
        if self.GAME.player.rect.collidepoint(self.rect.center):
            #  Activate power up
            self.power_up_activate[self.name](self.GAME.player)
            self.GAME.level_matrix[self.row][self.col] = "_"
            self.kill()
            return


    def draw(self,window, x_offset):
        window.blit(self.image, (self.rect.x - x_offset, self.rect.y))


    def bomb_up_special(self, player):
        """Increase the player's bomb limit"""
        player.bomb_limit += 1

    def fire_up_special(self, player):
        """Increase the Bombs Power"""
        player.power += 1

    def speed_up_special(self, player):
        """Increase the speed of the player"""
        player.speed += 1

    def wall_hack_special(self, player):
        """Turn on the player wall hack"""
        player.wall_hack = True

    def remote_special(self, player):
        """Turn on the remote detonate ability"""
        player.remote = True

    def bomb_hack_special(self, player):
        """Turn on the bomb Hack"""
        player.bomb_hack = True

    def flame_pass_special(self, player):
        """Turn on the ability to ignore bomb blasts"""
        player.flame_pass = True

    def invincible_special(self, player):
        """Turn on the players invincibility"""
        player.invincibility = True