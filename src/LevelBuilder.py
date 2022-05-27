import json

from src.Level import Level
from src.Player import Player
from src.LaserUtility.Laser import Laser
from src.Structures.Door import Door, Direction
from src.Structures.LaserDetector import LaserDetector
from src.Structures.Pit import Pit

from src.Structures.RectangleWall import RectangleWall
from src.Structures.Column import Column
from src.Structures.PolygonWall import PolygonWall
from src.Structures.WinFlag import WinFlag


class LevelBuilder:
    def __init__(self):
        self.level = None
        self.handlers = {
            "rectangleWalls": self.addRectangleWall,
            "columns": self.addColumn,
            "lasers": self.addLaser,
            "polygonWalls": self.addPolygonWall,
            "pits": self.addPit,
            "laserDetectors": self.addLaserDetector,
            "doors": self.addDoor,
            "winFlags": self.addWinFlag
        }

    def addRectangleWall(self, data):
        x, y = data["x"], data["y"]
        width, height = data["width"], data["height"]

        wall = RectangleWall(x, y, width, height)
        self.level.structureManager.add(wall)
        self.level.collisionManager.add(wall)

    def addPit(self, data):
        pl = data["pointList"]
        pit = Pit(pl)
        self.level.collisionManager.add(pit)
        self.level.structureManager.add(pit)


    def addColumn(self, data):
        x, y = data["x"], data["y"]
        r = data["r"]

        column = Column(x, y, r)
        self.level.structureManager.add(column)
        self.level.collisionManager.add(column)

    def addLaser(self, data):
        r = data["r"]
        x1, x2 = data["x1"], data["x2"]
        y1, y2 = data["y1"], data["y2"]
        speed = data["speed"]

        laser = Laser(r, x1, y1, x2, y2, speed)
        self.level.laserManager.add(laser)
        self.level.collisionManager.add(laser)

    def addPolygonWall(self, data):
        pl = data["pointList"]
        polygonWall = PolygonWall(pl)
        self.level.collisionManager.add(polygonWall)
        self.level.structureManager.add(polygonWall)

    def addLaserDetector(self, data):
        pl = data["pointList"]
        laserDetector = LaserDetector(pl)
        self.level.collisionManager.add(laserDetector)
        self.level.structureManager.add(laserDetector)
        self.level.logicManager.addEmmiter(laserDetector, id=data["id"])

    def addDoor(self, data):
        x, y = data["x"], data["y"]
        width = data["width"]
        direction = Direction(data["direction"])

        door = Door(x, y, width, direction)
        self.level.structureManager.add(door)
        self.level.logicManager.addReciever(door, id=data["id"])

    def addWinFlag(self, data):
        x, y = data["x"], data["y"]

        winFlag = WinFlag(x, y)
        self.level.collisionManager.add(winFlag)
        self.level.structureManager.add(winFlag)

    def build(self, path):
        with open(path, 'r') as f:
            levelJson = json.load(f)

        player = levelJson["player"]
        self.level = Level(Player(player["x"], player["y"]))

        for item_type, items in levelJson.items():
            handler = self.handlers.get(item_type, lambda x: None)
            for data in items:
                handler(data)

        return self.level
