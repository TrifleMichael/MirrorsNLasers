import time

from src.Sprites import RectangleSprite
from src.Collisons.CollisionManager import CollisionManager
from src.Managers import LaserManager, StructureManager
from src.Settings import xResolution, yResolution


class Level:
    """Responsible for managing the level simulation."""
    def __init__(self, player):
        self.player = player

        self.structureManager = StructureManager()
        self.laserManager = LaserManager()
        self.collisionManager = CollisionManager(player.mirror, player)

        self.sprite = RectangleSprite(xResolution, yResolution, color=(40, 40, 40))
        self.time = time.time()

    def update(self, keys):
        """Updates all objects in the level. Updates everything."""
        dt = time.time() - self.time
        self.time = time.time()

        self.player.update(keys, dt)
        self.structureManager.update(dt)
        self.collisionManager.update()
        self.laserManager.update(dt)

    def addObject(self, obj):
        """Adds an object to the level. The object will be updated and drawn each frame."""
        pass # TODO

    def draw(self):
        """Draws all objects in the level. Draws everything."""
        self.sprite.draw(0, 0)
        self.structureManager.draw()
        self.laserManager.draw()
        self.player.draw()
