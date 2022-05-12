import pygame

from src import display
from src.Sprites import Sprite


class LineSprite(Sprite):
    """A line sprite. Needs two points to be drawn."""
    def __init__(self, color=None, width=5):
        self.color = color or (0, 0, 0)
        self.width = width

    def draw(self, p1, p2):
        pygame.draw.line(display, self.color, p1, p2, self.width)
