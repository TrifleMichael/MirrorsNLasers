import pygame

from src import display
from src.Sprites import Sprite


class CircleSprite(Sprite):
    """A circle sprite. Has radius and color. Needs x and y to be drawn."""

    def __init__(self, radius, color=None, x=None, y=None):
        self.color = color or [0, 0, 0]
        self.radius = radius
        self.x, self.y = x, y

    def draw(self, x=None, y=None):
        pygame.draw.circle(display, self.color, (x or self.x, y or self.y), self.radius)
