from src.sprites import CircleSprite
from src.Collisons.RoundCollisonModel import RoundCollisionModel


class Column(RoundCollisionModel):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self.sprite = CircleSprite(radius=r, color=(0, 0, 255))

    def reactToCollision(self):
        pass  # columns don't react to collisions





