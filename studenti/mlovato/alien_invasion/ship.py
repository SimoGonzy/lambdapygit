import pygame


class Ship:
    """Class to handle a space ship"""

    def __init__(self, ai_game):
        """initialize a spaceship and draw it onto the screen"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rectangle
        # Scale the image because it's massive
        self.image = pygame.transform.scale(
            pygame.image.load("images/ship.bmp"), (70, 70)
        )
        self.rect = self.image.get_rect()

        # start position of the ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # flag moving right
        self.moving_right = False
        # flag for left. start at 0 so the ship doesnt move
        self.moving_left = False

    def update(self):
        """move the ship based on movement flags"""
        # different ifs so if both keydown ship will stop
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = int(self.x)

    def blitme(self):
        """draw ship in current position"""
        self.screen.blit(self.image, self.rect)
