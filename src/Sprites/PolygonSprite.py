import pygame

from src import display
from src.Sprites import Sprite


class PolygonSprite(Sprite):
    """A polygon sprite. Needs a list of points to be drawn."""
    def __init__(self, color=None):
        self.color = color or (0, 0, 0)

    def draw(self, segmentList):
        pygame.draw.polygon(display, self.color, segmentList)
