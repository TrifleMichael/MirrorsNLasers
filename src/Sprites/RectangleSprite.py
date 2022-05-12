import pygame

from src import display
from src.Sprites import Sprite


class RectangleSprite(Sprite):
    """A rectangle sprite. Has width and height. Needs x and y to be drawn."""
    def __init__(self, width, height, color=None):
        self.width = width
        self.height = height
        self.color = color or (0, 0, 0)

    def draw(self, x, y):
        pygame.draw.rect(display, self.color, (x, y, self.width, self.height))
