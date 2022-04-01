import time

from src.AtomicObjects.RectangleSprite import RectangleSprite
from src.Player import PlayerSimulationManager


class LevelSimulationManager:
    def __init__(self, DISPLAY, width, height):
        self.levelVisualManager = LevelVisualManager(DISPLAY, width, height)
        self.width = width
        self.height = height

        self.playerSimulationManager = PlayerSimulationManager(DISPLAY, 200, 200)
        self.levelVisualManager.addObject(self.playerSimulationManager)

        self.time = time.time()

    def update(self, keys):
        dt = time.time() - self.time
        self.time = time.time()
        self.playerSimulationManager.update(keys, dt)

    def updateVisualManager(self):
        pass  # stand holder function, might want to change background in the future


class LevelVisualManager:
    def __init__(self, DISPLAY, width, height):
        self.sprite = RectangleSprite(DISPLAY, width, height)

        self.objectsToDraw = []

    def addObject(self, obj):
        self.objectsToDraw.append(obj)

    def draw(self):
        self.sprite.draw(0, 0)
        for obj in self.objectsToDraw:
            obj.draw()

    def update(self):
        pass  # mock function, level sprite should not move
