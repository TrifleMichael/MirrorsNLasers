import json

from src.LaserUtility.Laser import Laser
from src.Structures import Column, RectangleWall, PolygonWall
from src.Level import Level
from src.Player import Player


class LevelBuilder:
    def __init__(self):
        self.level = None

    def addRectangleWall(self, data):
        x, y = data["x"], data["y"]
        width, height = data["width"], data["height"]

        wall = RectangleWall(x, y, width, height)
        self.level.structureManager.add(wall)
        self.level.collisionManager.add(wall)


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

    def build(self, path):
        with open(path, 'r') as f:
            levelJson = json.load(f)

        player = levelJson["player"]
        self.level = Level(Player(player["x"], player["y"]))

        for col_data in levelJson.get("columns", []):
            self.addColumn(col_data)

        for wall_data in levelJson.get("rectangleWalls", []):
            self.addRectangleWall(wall_data)

        for laser_data in levelJson.get("lasers", []):
            self.addLaser(laser_data)

        for polygon_wall_data in levelJson.get("polygonWalls", []):
            self.addPolygonWall(polygon_wall_data)

        return self.level
