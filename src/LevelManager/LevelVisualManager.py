from src.AtomicObjects.RectangleSprite import RectangleSprite


class LevelVisualManager:
    def __init__(self, DISPLAY, width, height):
        self.sprite = RectangleSprite(DISPLAY, width, height)

    def draw(self):
        self.sprite.draw(0, 0)

    def update(self):
        pass # mock function, level sprite should not move

