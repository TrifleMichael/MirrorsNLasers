from src.LogicManager import Receiver
from src.Sprites.LineSprite import LineSprite
from src.Structures import Structure
from enum import Enum
from math import pi, cos, sin


class Direction(Enum): # TODO: problably move this to a different file
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

    def to_rotation(self):
        return self.value*pi/2


class Door(Structure, Receiver):
    """A door is a structure that can be opened and closed"""
    def __init__(self, x, y, width, direction: Direction, is_open=False):
        self.x, self.y = x, y
        self.width = width
        self.is_open = is_open
        self.rotation = direction.to_rotation()
        self.sprite = LineSprite(color=(139, 69, 19), width=15)

    def draw(self):
        self.sprite.draw(*self.getSurfacePoints())

    def trigger(self):
        if not self.is_open:
            self.is_open = True
            self.rotation += pi/2

    def getSurfacePoints(self):
        p1 = (self.x, self.y)
        p2 = (self.x + cos(self.rotation)*self.width, self.y + sin(self.rotation)*self.width)
        return p1, p2
