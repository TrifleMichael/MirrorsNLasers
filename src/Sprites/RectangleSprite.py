import pygame

from src import display
from src.Sprites import Sprite


class RectangleSprite(Sprite):
    """A rectangle sprite. Has width and height. Needs x and y to be drawn."""

    def __init__(self, width, height, color=None, x=None, y=None):
        self.width = width
        self.height = height
        self.color = color or (0, 0, 0)
        self.x = x
        self.y = y

    def draw(self, x=None, y=None):
        pygame.draw.rect(display, self.color,
                         (self.x or x, self.y or y, self.width, self.height))
