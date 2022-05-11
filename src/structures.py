from abc import ABC, abstractmethod

from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.sprites import RectangleSprite, CircleSprite

# TODO add more structures
class Structure(ABC):
    """Abstract class for all sprites. Forces child classes to implement draw."""
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass


class Wall(Structure):
    """ A wall is a ..."""  # TODO add description
    def __init__(self, x, y, width, height):
        self.sprite = RectangleSprite(width, height)
        self.collisionShape = None  # TODO: Add rectangle collision simulation
        self.x = x
        self.y = y

    def draw(self):
        self.sprite.draw(self.x, self.y)


class Column(Structure, RoundCollisionModel):
    """ A column is an immovable round object."""

    def __init__(self, x, y, radius):
        RoundCollisionModel.__init__(self, x, y, radius)
        self.sprite = CircleSprite(radius, color=(0, 0, 255))
        self.x = x
        self.y = y

    def draw(self):
        self.sprite.draw(self.x, self.y)

    def reactToCollision(self):
        # The column doesn't react to collisions
        pass
