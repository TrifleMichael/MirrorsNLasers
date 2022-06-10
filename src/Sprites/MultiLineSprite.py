import pygame

from src import display
from src.Sprites import Sprite


class MultiLineSprite(Sprite):
    """A multi-line sprite. Needs a list of points to be drawn."""

    def __init__(self, color=None, width=5):
        self.color = color or (0, 0, 0)
        self.width = width

    def draw(self, pointList):
        for i in range(len(pointList) - 1):
            p1 = pointList[i]
            p2 = pointList[i + 1]
            pygame.draw.line(display, self.color, p1, p2, self.width)
