import time

from src.AtomicObjects.RectangleSprite import RectangleSprite
from src.Collisons.CollisionManager import CollisionManager
from src.Collisons.Column import Column
from src.LaserUtility.LaserManager import LaserManager
from src.Player import PlayerSimulationManager


class LevelSimulationManager:
    def __init__(self, DISPLAY, field, dt):
        self.field = field
        self.levelVisualManager = LevelVisualManager(DISPLAY, self.field.width, self.field.height)

        self.playerSimulationManager = PlayerSimulationManager(DISPLAY, 200, 400, 50, self.field)
        self.levelVisualManager.addObject(self.playerSimulationManager)
        self.collisionManager = CollisionManager()
        self.collisionManager.roundCollisionModels.append(self.playerSimulationManager)
        self.laserManager = LaserManager(dt, DISPLAY)

        self.time = time.time()

    def update(self, keys):
        dt = time.time() - self.time
        self.time = time.time()
        self.playerSimulationManager.update(keys, dt)
        self.collisionManager.checkCollisions()
        self.laserManager.move()

    def createLaser(self, r, x1, y1, x2, y2, speed):
        self.laserManager.createLaser(r, x1, y1, x2, y2, speed)
        # TODO: add laser hitbox to collision manager

    def updateVisualManager(self):
        pass  # stand holder function, might want to change background in the future

    def addColumn(self, x, y, r):
        column = Column(x, y, r, self.levelVisualManager.display)
        column.update(x, y)
        self.collisionManager.roundCollisionModels.append(column)
        self.levelVisualManager.addObject(column.sprite)

    # JUST FOR TESTING
    def addObject(self, obj):
        self.levelVisualManager.addObject(obj.visualManager.sprite)


class LevelVisualManager:
    def __init__(self, DISPLAY, width, height):
        self.display = DISPLAY
        self.sprite = RectangleSprite(DISPLAY, width, height)
        self.objectsToDraw = []  # hierarchy and layers will be needed

    def addObject(self, obj):
        self.objectsToDraw.append(obj)

    def draw(self):
        self.sprite.draw(0, 0)
        for obj in self.objectsToDraw:
            obj.draw()

    def update(self):
        pass  # mock function, level sprite should not move
