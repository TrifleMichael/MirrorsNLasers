from enum import Enum
from math import pi

from src import xResolution, yResolution


class ScreenCorner(Enum):
    """Enum for the corners of a screen."""
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_RIGHT = 3
    BOTTOM_LEFT = 4

    def point(self):
        """ Returns the x and y coordinates of the corner."""
        return xResolution * (1 - self.isLeft()), yResolution * (1 - self.isTop())

    def isLeft(self):
        """ Returns True if the corner is on the left side of the screen."""
        return self.value == 1 or self.value == 4

    def isTop(self):
        """ Returns True if the corner is on the top side of the screen."""
        return self.value == 1 or self.value == 2


class Direction(Enum):
    """ Enum for the directions."""
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4

    def to_rotation(self):
        """ Returns the rotation of the direction in radians (0 is right, counterclockwise)."""
        return (self.value - 1) * pi / 2
      
    def rotate90(self, n=1):
        return Direction((self.value+n-1)%4+1)


class GameState(Enum):
    """Enum for the different states of the game."""
    START = 1
    PLAYING = 2
    PAUSED = 3
    DEAD = 4
    WON = 5
    OVER = 6
    COMPLETED = 7
