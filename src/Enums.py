from enum import Enum
from src import xResolution, yResolution
from math import pi


class ScreenCorner(Enum):
    """
    Enum for the corners of a screen.
    """
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_RIGHT = 3
    BOTTOM_LEFT = 4

    def point(self):
        return xResolution * (1 - self.isLeft()), yResolution * (1 - self.isTop())

    def isLeft(self):
        return self.value == 1 or self.value == 4

    def isTop(self):
        return self.value == 1 or self.value == 2


class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4

    def to_rotation(self):
        return (self.value-1)*pi/2

    def rotate90(self, n=1):
        return Direction((self.value+n-1)%4+1)
