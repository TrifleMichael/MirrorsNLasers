from abc import ABC, abstractmethod

from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.Sprites import RectangleSprite, CircleSprite, PolygonSprite


class Structure(ABC):
    """Abstract class for all sprites. Forces child classes to implement draw."""
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass


class RectangleWall(Structure):
    """ A wall is an immovable structure that can be collided with. """
    def __init__(self, x, y, width, height):
        pts = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
        self.collisionModel = PolygonCollisionModel(pts)
        self.sprite = RectangleSprite(width, height, color=(0, 100, 0))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.reflective = True

    def draw(self):
        self.sprite.draw(self.x, self.y)


class PolygonWall(Structure):
    def __init__(self, pointsList):
        self.collisionModel = PolygonCollisionModel(pointsList)
        self.sprite = PolygonSprite(pointsList)
        self.reflective = True

    def draw(self):
        self.sprite.draw()


class Column(Structure, RoundCollisionModel):
    """ A column is an immovable round object."""

    def __init__(self, x, y, radius):
        RoundCollisionModel.__init__(self, x, y, radius)
        self.sprite = CircleSprite(radius, color=(128, 128, 0))
        self.x = x
        self.y = y

    def draw(self):
        self.sprite.draw(self.x, self.y)
