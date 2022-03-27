from src.AtomicObjects.CircleSprite import CircleSprite


class PlayerVisualManager:
    def __init__(self, DISPLAY):
        self.playerSprite = CircleSprite(50)
        self.DISPLAY = DISPLAY
        self.x = None  # initialized in update()
        self.y = None

    def draw(self):
        self.playerSprite.draw(self.DISPLAY, self.x, self.y)

    def update(self, x, y):
        self.x = x
        self.y = y
