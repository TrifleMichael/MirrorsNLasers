import pygame

from src import display, xResolution, yResolution
from src.Enums import GameState
from src.Sprites.RectangleSprite import RectangleSprite


class Banner:
    """Rectangle with text on it to be drawn at the center of the screen."""

    def __init__(self, main_text, *sub_texts):
        self.font = pygame.font.SysFont("monospace", 50)
        self.subfont = pygame.font.SysFont("monospace", 25)

        x, y = xResolution / 2, yResolution / 2 - 40
        self.text = self.font.render(main_text, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        y += self.textRect.height + 10

        self.subtexts = []
        for line in sub_texts:
            text = self.subfont.render(line, True, (255, 255, 255))
            rect = text.get_rect()
            rect.center = (x, y)
            y += rect.height

            self.subtexts.append((text, rect))

        self.bg = RectangleSprite(int(xResolution * 0.6), int(yResolution * 0.4), color=(0, 0, 139))

    def draw(self):
        self.bg.draw((xResolution - self.bg.width) // 2, (yResolution - self.bg.height) // 2)
        display.blit(self.text, self.textRect)
        for text, rect in self.subtexts:
            display.blit(text, rect)


class BannerPresets:
    """Helper class featuring a banners with preset texts."""

    def __init__(self):
        self.texts = {
            GameState.START: [
                "Welcome to the game!",
                "Press [space] to start.",
            ],
            GameState.PAUSED: [
                "Paused!",
                "Press [esc] to resume.",
                "Press [r] to restart.",
            ],
            GameState.DEAD: [
                "You died!",
                "Press [space] to try again.",
            ],
            GameState.WON: [
                "You won!",
                "Press [space] to go to next level.",
            ],
            GameState.OVER: [
                "You lost all lives!",
                "Press [space] to return to main menu.",
            ],
            GameState.COMPLETED: [
                "You completed all levels!",
                "Press [space] to return to main menu.",
            ],
        }
        self.texts = {k: v + ["Press [q] to quit."] for k, v in self.texts.items()}

        self.banners = {key: Banner(text[0], *text[1:]) for key, text in self.texts.items()}

    def draw(self, state):
        if state in self.banners:
            self.banners[state].draw()
