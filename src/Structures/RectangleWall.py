from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.RectangleSprite import RectangleSprite
from src.Structures import Structure


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