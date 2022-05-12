from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.Sprites.CircleSprite import CircleSprite
from src.Structures import Structure


class Column(Structure, RoundCollisionModel):
    """ A column is an immovable round object."""

    def __init__(self, x, y, radius):
        RoundCollisionModel.__init__(self, x, y, radius)
        self.sprite = CircleSprite(radius, color=(128, 128, 0))
        self.x = x
        self.y = y

    def draw(self):
        self.sprite.draw(self.x, self.y)