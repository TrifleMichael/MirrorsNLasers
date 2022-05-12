import pygame
from abc import ABC, abstractmethod

from src import display


class Sprite(ABC):
    """Abstract class for all sprites. Forces child classes to implement draw."""
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass


class CircleSprite(Sprite):
    """A circle sprite. Has radius and color. Needs x and y to be drawn."""
    def __init__(self, radius, color=None):
        self.color = color or (0, 0, 0)
        self.radius = radius

    def draw(self, x, y):
        pygame.draw.circle(display, self.color, (x, y), self.radius)


class LineSprite(Sprite):
    """A line sprite. Needs two points to be drawn."""
    def __init__(self, color=None, width=5):
        self.color = color or (0, 0, 0)
        self.width = width

    def draw(self, p1, p2):
        pygame.draw.line(display, self.color, p1, p2, self.width)


class MultiLineSprite(Sprite):
    """A multi-line sprite. Needs a list of points to be drawn."""
    def __init__(self, color=None, width=5):
        self.color = color or (0, 0, 0)
        self.width = width

    def draw(self, pointList):
        for i in range(len(pointList)-1):
            p1 = pointList[i]
            p2 = pointList[i+1]
            pygame.draw.line(display,  self.color, p1, p2, self.width)


class RectangleSprite(Sprite):
    """A rectangle sprite. Has width and height. Needs x and y to be drawn."""
    def __init__(self, width, height, color=None):
        self.width = width
        self.height = height
        self.color = color or (0, 0, 0)

    def draw(self, x, y):
        pygame.draw.rect(display, self.color, (x, y, self.width, self.height))


class PolygonSprite(Sprite):
    """A polygon sprite. Needs a list of points to be drawn."""
    def __init__(self, segmentList, color=None):
        self.color = color or (0, 0, 0)
        self.segmentList = segmentList

    def draw(self):
        pygame.draw.polygon(display, self.color, self.segmentList)
