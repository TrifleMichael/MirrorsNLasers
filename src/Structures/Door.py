from src.Sprites.LineSprite import LineSprite
from src.Structures import Structure
from enum import Enum
from math import pi, cos, sin


class Direction(Enum): # TODO: problably move this to a different file
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def to_rotation(self):
        return self.value*pi/2


class Door(Structure):
    def draw(self):
        self.sprite.draw(*self.getSurfacePoints())

    def __init__(self, x, y, width, direction: Direction, is_open=False):
        self.x, self.y = x, y
        self.width = width
        self.is_open = is_open
        self.rotation = direction.to_rotation()
        self.sprite = LineSprite(color=(255, 228, 196), width=15)

    def toggle(self):
        self.is_open = not self.is_open
        self.rotation += pi/2 if self.is_open else -pi/2

    def getSurfacePoints(self):
        p1 = (self.x, self.y)
        p2 = (self.x + cos(self.rotation)*self.width, self.y + sin(self.rotation)*self.width)
        return p1, p2
