import pygame

from src import display
from src.Enums import ScreenCorner
from src.Sprites.RectangleSprite import RectangleSprite


class Hud:
    """Heads up display. Shows messages on the screen."""

    def __init__(self, width, height, corner: ScreenCorner):
        self.bg = RectangleSprite(width, height, color=(70, 30, 40))
        self.x, self.y = corner.point()
        self.x -= width if not corner.isLeft() else 0
        self.y -= height if not corner.isTop() else 0

        self.font = pygame.font.SysFont("monospace", int(height * 0.9))
        self.msg_text = ""
        self.msg = self.font.render(self.msg_text, True, (255, 255, 255))

    def update(self, msg_text):
        """Updates the message if it has changed."""
        if msg_text != self.msg_text:
            self.msg_text = msg_text
            self.msg = self.font.render(self.msg_text, True, (255, 255, 255))

    def draw(self):
        """Draws the message on the screen."""
        self.bg.draw(self.x, self.y)
        display.blit(self.msg, (self.x + 10, self.y))
