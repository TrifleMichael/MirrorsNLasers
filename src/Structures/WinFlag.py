from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.LineSprite import LineSprite
from src.Sprites.PolygonSprite import PolygonSprite
from src.Structures import Structure

shape = [(0, 0), (80, 40), (0, 80)]


class WinFlag(Structure):
    """A wall is an immovable structure that makes player complete a level upon reaching."""
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.collisionModel = PolygonCollisionModel([(x+xs, y+ys) for xs, ys in shape])

        self.flag = PolygonSprite([(x+xs, y+ys) for xs, ys in shape], color=(0, 255, 0))
        self.leg = LineSprite(color=(160,82,45), width=5)

    def draw(self):
        self.flag.draw()
        self.leg.draw((self.x, self.y), (self.x, self.y+150))


