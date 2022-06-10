import math

from src.AtomicObjects.Movables import NonInertialObject
from src.Sprites.LineSprite import LineSprite


class Mirror(NonInertialObject):
    """A mirror object."""

    def __init__(self, x, y, width, rotation):
        super().__init__(x, y)
        self.width = width
        self.rotation = rotation

        self.sprite = LineSprite(width=10, color=(32, 178, 170))
        self.pastSurface = self.getSurface()

    def getSurface(self):
        """Returns the surface of the mirror represented by 2 points"""
        cos, sin = math.cos(self.rotation), math.sin(self.rotation)

        p1 = self.x - (self.width / 2) * sin, self.y + (self.width / 2) * cos
        p2 = self.x + (self.width / 2) * sin, self.y - (self.width / 2) * cos

        return p1, p2

    def getPastSurface(self):
        return self.pastSurface[:]

    def getSurfaceNormal(self):
        """Returns the normal vector of the mirror surface"""
        cos, sin = math.cos(self.rotation), math.sin(self.rotation)
        return -sin, cos

    def setRotation(self, rotation):
        """Sets the rotation of the mirror"""
        self.rotation = rotation
        self.pastSurface = self.getSurface()

    def draw(self):
        """Draws the mirror"""
        self.sprite.draw(*self.getSurface())
