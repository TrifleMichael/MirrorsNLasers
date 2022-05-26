from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.PolygonSprite import PolygonSprite
from src.Structures import Structure


class LaserDetector(Structure):
    def __init__(self, pointList):
        self.collisionModel = PolygonCollisionModel(pointList)
        self.sprite = PolygonSprite(pointList)
        self.sprite.color = (0, 0, 255)

        self.receivers = []

    def draw(self):
        self.sprite.draw()

    def reactToCollision(self):
        for receiver in self.receivers:
            receiver.trigger()
        self.sprite.color = (255, 0, 0)
