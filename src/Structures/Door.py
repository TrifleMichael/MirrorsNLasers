from src.LogicManager import Receiver
from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.LineSprite import LineSprite
from src.Structures import Structure
from src.Enums import Direction
from math import pi, cos, sin

from src.Utility.EuclidianFunctions import rotate2dLine, lineAngle, apply2dRotation


class Door(Structure, Receiver):
    """A door is a structure that can be opened and closed"""
    def __init__(self, x, y, width, direction: Direction, is_open=False):
        self.x, self.y = x, y
        self.width = width
        self.is_open = is_open
        self.rotation = direction.to_rotation()
        self.sprite = LineSprite(color=(139, 69, 19), width=15)
        self.collisionModel = PolygonCollisionModel(self.getSurfacePoints())

    def draw(self):
        self.sprite.draw(*self.getSurfacePoints())

    def trigger(self):
        if not self.is_open:
            self.is_open = True
            self.rotation += pi/2
        self.collisionModel = PolygonCollisionModel([])

    def getSurfacePoints(self):
        p1 = (self.x, self.y)
        p2 = (self.x + cos(self.rotation)*self.width, self.y + sin(self.rotation)*self.width)
        return p1, p2
