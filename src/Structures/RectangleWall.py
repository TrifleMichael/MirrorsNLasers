from src.Sprites.RectangleSprite import RectangleSprite
from src.Structures.BasicStructure import BasicStructure


class RectangleWall(BasicStructure):
    def __init__(self, DISPLAY, x, y, width, height):
        super().__init__()
        self.sprite = RectangleSprite(DISPLAY, width, height)
        self.sprite.color = (10, 100, 100)
        self.collisionShape = None  # TODO: Add rectangle collision simulation
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite.update(self.x, self.y)

    def getPointList(self):
        return [[self.x, self.y],
                [self.x + self.width, self.y],
                [self.x + self.width, self.y + self.height],
                [self.x, self.y + self.height]]



