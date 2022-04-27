import math

from src.AtomicObjects.LineSprite import LineSprite
from src.AtomicObjects.Movables import InertialObject


class Mirror(InertialObject):
    """A mirror object."""
    def __init__(self, x, y, width, rotation, display):
        super().__init__(x, y)
        self.width = width
        self.rotation = rotation

        self.visualManager = MirrorVisualManager(*self.getSurface(), display)

    def getSurface(self):
        """Returns the surface of the mirror represented by 2 points"""
        cos, sin = math.cos(self.rotation), math.sin(self.rotation)

        p1 = self.x + (self.width / 2) * cos, self.y + (self.width / 2) * sin
        p2 = self.x - (self.width / 2) * cos, self.y - (self.width / 2) * sin

        return p1, p2

    def getSurfaceNormal(self):
        """Returns the normal vector of the mirror surface"""
        cos, sin = math.cos(self.rotation), math.sin(self.rotation)
        return -sin, cos


class MirrorVisualManager:
    def __init__(self, p1, p2, display):
        self.p1, self.p2 = p1, p2

        self.sprite = LineSprite(p1, p2, display)

    def draw(self):
        self.sprite.draw()

    def update(self, p1, p2):
        self.sprite.update(p1, p2)
