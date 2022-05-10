from src.AtomicObjects.RectangleSprite import RectangleSprite
from src.Structures.BasicStructure import BasicStructure


class Wall(BasicStructure):
    def __init__(self, DISPLAY, x, y, width, height):
        super().__init__()
        self.sprite = RectangleSprite(DISPLAY, width, height)
        self.sprite.color = (10, 100, 100)
        self.collisionShape = None  # TODO: Add rectangle collision simulation
        self.x = x
        self.y = y
        self.sprite.update(self.x, self.y)


