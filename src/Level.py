import time

from src.GuidedMovementModels.EnemyManager import EnemyManager
from src.LaserUtility.Laser import Laser
from src.Sprites.RectangleSprite import RectangleSprite
from src.Collisons.CollisionManager import CollisionManager
from src.LaserUtility.LaserManager import LaserManager
from src.Structures import StructureManager
from src.Settings import xResolution, yResolution

from src.LogicManager import LogicManager


class Level:
    """Responsible for managing the level simulation."""
    def __init__(self, player):
        self.player = player

        self.structureManager = StructureManager()
        self.laserManager = LaserManager()
        self.logicManager = LogicManager()
        self.collisionManager = CollisionManager(player.mirror, player)
        self.enemyManager = EnemyManager(self)

        self.sprite = RectangleSprite(xResolution, yResolution, color=(40, 40, 40))
        self.time = time.time()

    def update(self, keys):
        """Updates all objects in the level. Updates everything."""
        dt = time.time() - self.time
        self.time = time.time()

        self.player.update(keys, dt)
        self.structureManager.update()
        self.collisionManager.update()
        self.laserManager.update(dt)
        self.enemyManager.update(dt)

    def addObject(self, obj):
        """Adds an object to the level. The object will be updated and drawn each frame."""
        pass

    def addLaser(self, laserVec):
        x1, y1 = laserVec[0]
        x2, y2 = laserVec[1]
        r = 1
        speed = 200
        laser = Laser(r, x1, y1, x2, y2, speed)
        self.laserManager.add(laser)
        self.collisionManager.add(laser)

    def draw(self):
        """Draws all objects in the level. Draws everything."""
        self.sprite.draw(0, 0)
        self.structureManager.draw()
        self.laserManager.draw()
        self.player.draw()
        self.enemyManager.draw()