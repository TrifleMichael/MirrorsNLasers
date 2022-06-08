from src.LogicManager import Receiver
from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.PolygonSprite import PolygonSprite
from src.Structures import Structure
from src.Enums import Direction
from src.Utility.EuclidianFunctions import apply2dRotation


class Door(Structure, Receiver):
    """A door is a structure that can be opened and closed"""
    def __init__(self, x, y, width, direction: Direction, girth=20, is_open=False):
        self.x, self.y = x, y
        self.width = width
        self.girth = girth
        self.is_open = is_open
        self.direction = direction
        self.sprite = PolygonSprite(self.getSegmentList(), color=(139, 69, 19))
        self.collisionModel = PolygonCollisionModel(self.getSegmentList())

    def draw(self):
        self.sprite.draw(self.getSegmentList())

    def trigger(self):
        if not self.is_open:
            self.is_open = True
            self.direction = self.direction.rotate90()
            self.collisionModel = PolygonCollisionModel(self.getSegmentList())

    def getSegmentList(self):
        pts = [
            (self.x, self.y),
            (self.x, self.y + self.girth),
            (self.x + self.width, self.y + self.girth),
            (self.x + self.width, self.y),
        ]
        center = pts[0]
        pts = [(p[0] - center[0], p[1] - center[1]) for p in pts]
        pts = [apply2dRotation(p, self.direction.to_rotation()) for p in pts]
        pts = [(p[0] + center[0], p[1] + center[1]) for p in pts]
        return pts
