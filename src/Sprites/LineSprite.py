import pygame

from src import display
from src.Sprites import Sprite


class LineSprite(Sprite):
    """A line sprite. Needs two points to be drawn."""

    def __init__(self, color=None, width=5, p1=None, p2=None):
        self.color = color or (0, 0, 0)
        self.width = width
        self.p1, self.p2 = p1, p2

    def draw(self, p1=None, p2=None):
        pygame.draw.line(display, self.color, self.p1 or p1, self.p2 or p2, self.width)
