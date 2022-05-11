import json

from src.Collisons.Column import Column
from src.Level import Level
from src.Player import Player

# TODO finish this class
class LevelBuilder:
    def __init__(self):
        self.level = None

        self.handlers = {"player": self.addPlayer, "walls": self.addWalls}

    def addPlayer(self, data): # TODO
        pass

    def addWalls(self, data): # TODO
        pass

    def addColumns(self, data): # TODO
        for col in data:
            x = col["x"]
            y = col["y"]
            r = col["r"]
            width = col["width"]
            height = col["height"]

            column = Column(x, y, r)

    def build(self, path):
        with open(path, 'r') as f:
            self.levelJson = json.load(f)
        for itemName, itemData in self.levelJson.items():
            handler = self.handlers[itemName]
            handler(itemData)

        return self.level

    def getTestLevel(self):
        self.level = Level(Player(100, 100))
        self.level.addObject(Column(200, 500, 20))
        self.level.addObject(Column(400, 100, 100))
        return self.level



