from time import time

from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.Enums import Direction
from src.Sprites.CircleSprite import CircleSprite
from src.Sprites.LineSprite import LineSprite
from src.Sprites.RectangleSprite import RectangleSprite
from src.Structures import Structure
from src.Utility.EuclidianFunctions import apply2dRotation


class LaserCannon(Structure):
    def __init__(self, x, y, direction: Direction, radius=60):
        self.collisionModel = RoundCollisionModel(x, y, radius)
        self.last_fire_time = time()

        self.p1 = (x, y)
        p2 = apply2dRotation((radius * 1.1, 0), -direction.to_rotation())
        self.p2 = (p2[0] + x, p2[1] + y)
        self.sprites = [
            RectangleSprite(radius * 2, radius * 2, color=(20, 0, 0), x=x - radius, y=y - radius),
            CircleSprite(radius, color=(100, 70, 0), x=x, y=y),
            LineSprite(color=(20, 20, 0),
                       width=int(radius * 0.3),
                       p1=self.p1,
                       p2=self.p2)
        ]

    def draw(self):
        for sprite in self.sprites:
            sprite.draw()

    def getLaserVector(self):
        return [self.p2, self.p1]

    def canFire(self):
        time_since_last_fire = time() - self.last_fire_time
        if time_since_last_fire > 4:
            self.last_fire_time = time()
            return True
        return False
