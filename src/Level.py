from src.Collisons.CollisionManager import CollisionManager
from src.GuidedMovementModels.EnemyManager import EnemyManager
from src.LaserUtility.LaserManager import LaserManager
from src.LogicManager import LogicManager
from src.Settings import xResolution, yResolution, FPS
from src.Sprites.RectangleSprite import RectangleSprite
from src.Structures import StructureManager


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

    def update(self, keys):
        """Updates all objects in the level. Updates everything."""
        dt = 1 / FPS
        self.player.update(keys, dt)
        self.structureManager.update()
        self.collisionManager.update()
        self.laserManager.update(dt)
        self.enemyManager.update(dt)

    def draw(self):
        """Draws all objects in the level."""
        self.sprite.draw(0, 0)
        self.structureManager.draw()
        self.laserManager.draw()
        self.player.draw()
        self.enemyManager.draw()