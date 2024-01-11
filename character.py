import pygame
import gamesettings as gs


class Character(pygame.sprite.Sprite):
    def __init__(self, game, image_dict, group, row_num, col_num, size):
        super().__init__(group)
        self.GAME = game

        #  Character coordinates
        self.x = 0
        self.y = 0

        #  Character attributes
        self.speed = 3

        #  Character Action
        self.action = "walk_right"

        #  Character Images
        self.index = 0
        self.anim_time = 50
        self.anim_time_set = pygame.time.get_ticks()
        self.image_dict = image_dict
        self.image = self.image_dict[self.action][self.index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def input(self):
        for event in pygame.event.get():
            #  Pygameevent detection, "X" close button clicked, quit the program
            if event.type == pygame.QUIT:
                self.GAME.quit_game()
            #  Check if keys are pressed
            elif event.type == pygame.KEYDOWN:
                #  Check if the Escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    self.GAME.quit_game()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.move("walk_right")
        elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.move("walk_left")
        elif keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.move("walk_up")
        elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.move("walk_down")


    def update(self):
        pass


    def draw(self, window):
        window.blit(self.image, self.rect)


    def move(self, action):
        direction = {"walk_left": -self.speed, "walk_right": self.speed,
                     "walk_up": -self.speed, "walk_down": self.speed}
        #  Check if the animation is different to the movement direction, to reset the index
        if action != self.action:
            self.action = action
            self.index = 0
        #  Change the player's x or y coordinates dependant on the direction input used
        if action == "walk_left":
            self.x += direction[action]
        elif action == "walk_right":
            self.x += direction[action]
        elif action == "walk_up":
            self.y += direction[action]
        elif action == "walk_down":
            self.y += direction[action]
        #  Update the image animations for movement
        self._animate(action)
        #  Update the player character Rectangle
        self.rect.topleft = (self.x, self.y)




    def _animate(self, action):
        """Switches between images in order to animate movement"""
        if pygame.time.get_ticks() - self.anim_time_set >= self.anim_time:
            self.index += 1
            if self.index == len(self.image_dict[action]):
                self.index = 0

            self.image = self.image_dict[self.action][self.index]
            self.anim_time_set = pygame.time.get_ticks()
        return

