import sys

import pygame

from src import display
from src.Enums import ScreenCorner, GameState
from src.Gui.Banner import BannerPresets
from src.Gui.Hud import Hud
from src.LevelBuilder import LevelBuilder
from src.Settings import FPS, MAX_LIVES

level_files = ['lvls/1.json', 'lvls/2.json', 'lvls/3.json']


class App:
    """Main class for the game."""

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.banner = BannerPresets()
        self.hud = Hud(450, 40, ScreenCorner.TOP_LEFT)
        self.levelBuilder = LevelBuilder(level_files)

        self.state = GameState.START
        self.level = None

        self.lives = MAX_LIVES
        self.level_num = 0

        self.updateHandlers = {
            GameState.START: self.updateStart,
            GameState.PLAYING: self.updatePlaying,
            GameState.PAUSED: self.updatePaused,
            GameState.DEAD: self.updateDead,
            GameState.WON: self.updateWon,
            GameState.OVER: self.updateOver,
            GameState.COMPLETED: self.updateCompleted,
        }

        self.events = []

    def run(self):
        """Main loop of the game. Updates and draws the game."""
        while True:
            self.clock.tick(FPS)

            self.events = pygame.event.get()
            if pygame.QUIT in [e.type for e in self.events]:
                self.quit()

            self.updateHandlers[self.state]()

            if not self.state == GameState.START:
                self.level.draw()
                self.hud.update(f"Lvl: {self.level_num} Life: {self.lives}")
                self.hud.draw()
            else:
                display.fill([30, 30, 30])
            self.banner.draw(self.state)

            pygame.display.update()

    def updateStart(self):
        if self._key_down(pygame.K_q):
            self.quit()
        if self._key_down(pygame.K_SPACE):
            self.level = self.levelBuilder.build(self.level_num)
            self.state = GameState.PLAYING

    def updatePlaying(self):
        self.level.update(pygame.key.get_pressed())
        if self._key_down(pygame.K_ESCAPE):
            self.state = GameState.PAUSED

        if self.level.player.win:
            self.level_num += 1
            self.state = GameState.WON if self.level_num < len(level_files) else GameState.COMPLETED

        elif not self.level.player.alive:
            self.lives -= 1
            self.state = GameState.DEAD if self.lives > 0 else GameState.OVER

    def updatePaused(self):
        if self._key_down(pygame.K_q):
            self.quit()
        if self._key_down(pygame.K_ESCAPE):
            self.state = GameState.PLAYING
        if self._key_down(pygame.K_r):
            self.level = self.levelBuilder.build(self.level_num)
            self.state = GameState.PLAYING

    def updateDead(self):
        self.level.update(keys=None)
        if self._key_down(pygame.K_q):
            self.quit()
        if self._key_down(pygame.K_SPACE):
            self.level = self.levelBuilder.build(self.level_num)
            self.state = GameState.PLAYING

    def updateWon(self):
        self.level.update(keys=None)
        if self._key_down(pygame.K_q):
            self.quit()
        if self._key_down(pygame.K_SPACE):
            self.level = self.levelBuilder.build(self.level_num)
            self.state = GameState.PLAYING

    def updateOver(self):
        self.level.update(keys=None)
        if self._key_down(pygame.K_q):
            self.quit()
        if self._key_down(pygame.K_SPACE):
            self.level_num = 0
            self.lives = MAX_LIVES
            self.state = GameState.START

    def updateCompleted(self):
        self.level.update(keys=None)
        if self._key_down(pygame.K_q):
            self.quit()
        if self._key_down(pygame.K_SPACE):
            self.level_num = 0
            self.lives = MAX_LIVES
            self.state = GameState.START

    def quit(self):
        pygame.quit()
        sys.exit()

    def _key_down(self, key):
        """Returns True on the event that the key is pressed down. """
        for event in self.events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
