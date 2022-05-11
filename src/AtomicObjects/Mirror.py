import math

from src.sprites import LineSprite
from src.AtomicObjects.Movables import NonInertialObject


class Mirror(NonInertialObject):
    """A mirror object."""

    def __init__(self, x, y, width, rotation):
        super().__init__(x, y)
        self.width = width
        self.rotation = rotation

        self.sprite = LineSprite()

    def getSurface(self):
        """Returns the surface of the mirror represented by 2 points"""
        cos, sin = math.cos(self.rotation), math.sin(self.rotation)

        p1 = self.x - (self.width / 2) * sin, self.y + (self.width / 2) * cos
        p2 = self.x + (self.width / 2) * sin, self.y - (self.width / 2) * cos

        return p1, p2

    def getSurfaceNormal(self):
        """Returns the normal vector of the mirror surface"""
        cos, sin = math.cos(self.rotation), math.sin(self.rotation)
        return -sin, cos

    def setRotation(self, rotation):
        """Sets the rotation of the mirror"""
        self.rotation = rotation

    def draw(self):
        """Draws the mirror"""
        self.sprite.draw(*self.getSurface())

