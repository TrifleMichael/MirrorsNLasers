from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.PolygonSprite import PolygonSprite
from src.Structures import Structure


class PolygonWall(Structure):
    def __init__(self, pointsList):
        self.collisionModel = PolygonCollisionModel(pointsList)
        self.sprite = PolygonSprite(pointsList, color=(128, 128, 0))
        self.reflective = True

    def draw(self):
        self.sprite.draw()