from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.RectangleSprite import RectangleSprite
from src.Structures.BasicStructure import BasicStructure


class RectangleWall(BasicStructure):
    def __init__(self, DISPLAY, x, y, width, height):
        super().__init__()
        self.sprite = RectangleSprite(DISPLAY, width, height)
        self.sprite.color = (10, 100, 100)
        self.collisionModel = None  # TODO: Add rectangle collision simulation
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite.update(self.x, self.y)

        self.setupCollisionModel()
        self.ifReflective = True

    def setupCollisionModel(self):
        points = [[self.x, self.y],
                [self.x + self.width, self.y],
                [self.x + self.width, self.y + self.height],
                [self.x, self.y + self.height]]

        self.collisionModel = PolygonCollisionModel(points)



