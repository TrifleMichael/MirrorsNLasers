import json

from src.GuidedMovementModels.BasicEnemy import BasicEnemy
from src.LaserUtility.Laser import Laser
from src.Level import Level
from src.Player import Player
from src.Structures.Column import Column
from src.Structures.Door import Door, Direction
from src.Structures.LaserDetector import LaserDetector
from src.Structures.Pit import Pit
from src.Structures.PolygonWall import PolygonWall
from src.Structures.RectangleWall import RectangleWall
from src.Structures.WinFlag import WinFlag


class LevelBuilder:
    """
    Builds a level from a level file. Returns a Level object.
    All _addX are handler methods for different types of objects.
    """

    def __init__(self, level_files):
        self.level = None
        self.handlers = {
            "rectangleWalls": self._addRectangleWall,
            "columns": self._addColumn,
            "lasers": self._addLaser,
            "polygonWalls": self._addPolygonWall,
            "pits": self._addPit,
            "laserDetectors": self._addLaserDetector,
            "doors": self._addDoor,
            "winFlags": self._addWinFlag,
            "enemies": self._addBasicEnemy
        }

        self.level_files = level_files

    def _addRectangleWall(self, data):
        x, y = data["x"], data["y"]
        width, height = data["width"], data["height"]

        wall = RectangleWall(x, y, width, height)
        self.level.structureManager.add(wall)
        self.level.collisionManager.add(wall)

    def _addPit(self, data):
        pl = data["pointList"]
        pit = Pit(pl)
        self.level.collisionManager.add(pit)
        self.level.structureManager.add(pit)

    def _addColumn(self, data):
        x, y = data["x"], data["y"]
        r = data["r"]

        column = Column(x, y, r)
        self.level.structureManager.add(column)
        self.level.collisionManager.add(column)

    def _addLaser(self, data):
        r = data["r"]
        x1, x2 = data["x1"], data["x2"]
        y1, y2 = data["y1"], data["y2"]
        speed = data["speed"]

        laser = Laser(r, x1, y1, x2, y2, speed)
        self.level.laserManager.add(laser)
        self.level.collisionManager.add(laser)

    def _addPolygonWall(self, data):
        pl = data["pointList"]
        polygonWall = PolygonWall(pl)
        self.level.collisionManager.add(polygonWall)
        self.level.structureManager.add(polygonWall)

    def _addLaserDetector(self, data):
        pl = data["pointList"]
        laserDetector = LaserDetector(pl)
        self.level.collisionManager.add(laserDetector)
        self.level.structureManager.add(laserDetector)
        self.level.logicManager.addEmmiter(laserDetector, id=data["id"])

    def _addDoor(self, data):
        x, y = data["x"], data["y"]
        width = data["width"]
        direction = Direction(data["direction"])

        door = Door(x, y, width, direction)
        self.level.structureManager.add(door)
        self.level.logicManager.addReciever(door, id=data["id"])
        self.level.collisionManager.add(door)

    def _addWinFlag(self, data):
        x, y = data["x"], data["y"]
        winFlag = WinFlag(x, y)
        self.level.collisionManager.add(winFlag)
        self.level.structureManager.add(winFlag)

    def _addBasicEnemy(self, data):
        x, y, = data["x"], data["y"]
        r = data["r"]
        enemy = BasicEnemy(x, y, r, self.level.enemyManager)
        self.level.enemyManager.addEnemy(enemy)
        self.level.collisionManager.addEnemy(enemy)

    def build(self, level_num):
        with open(self.level_files[level_num], 'r') as f:
            levelJson = json.load(f)

        player = levelJson["player"]
        self.level = Level(Player(player["x"], player["y"]))

        for item_type, items in levelJson.items():
            handler = self.handlers.get(item_type, lambda x: None)
            for data in items:
                handler(data)

        return self.level
