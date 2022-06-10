import pygame

from src import display
from src.Sprites import Sprite


class PolygonSprite(Sprite):
    """A polygon sprite. Needs a list of points to be drawn."""

    def __init__(self, segmentList, color=None):
        self.color = color or (0, 0, 0)
        self.segmentList = segmentList

    def draw(self, segmentList=None):
        pygame.draw.polygon(display, self.color, segmentList or self.segmentList)
