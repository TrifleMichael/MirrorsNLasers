import pygame

from src.Sprites import Sprite
from src import display


class CircleSprite(Sprite):
    """A circle sprite. Has radius and color. Needs x and y to be drawn."""
    def __init__(self, radius, color=None):
        self.color = color or [0, 0, 0]
        self.radius = radius

    def draw(self, x, y):
        pygame.draw.circle(display, self.color, (x, y), self.radius)