import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Create the base of the game"""

    def __init__(self):
        """
        Initialize resouces"""

        _ = pygame.init()
        # initialize a clock
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)

    def run_game(self):
        """
        Start the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            # clock for fps so the game will run at the same speed on every
            # machine
            _ = self.clock.tick(60)

    def _check_events(self):
        # waiting for events from mouse or keyboad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        pass

    def _update_screen(self):
        # draw the screen every cycle
        _ = self.screen.fill(self.bg_color)
        self.ship.blitme()
        # update screen
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
