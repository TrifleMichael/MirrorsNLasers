from src.Collisons.CollisionFunctions import ifPolygonCollidesWithRound, ifPointCollidesWithLine, \
    whichSurfaceOfPolygonCollidesWithRound, ifRoundCollidesWithRound
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.LaserUtility.Laser import Laser
from src.Structures import RectangleWall, Column


class CollisionManager:
    def __init__(self, playerMirror, player):
        self.playerMirror = playerMirror
        self.player = player

        self.columnList = []
        self.laserList = []  # Laser type
        self.wallList = []

        self.playerDed = False

    def add(self, obj):
        if isinstance(obj, Laser):
            self.laserList.append(obj)
        if isinstance(obj, RectangleWall):
            self.wallList.append(obj)
        if isinstance(obj, Column):
            self.columnList.append(obj)

    def update(self):
        for column in self.columnList:
            for laser in self.laserList:
                self.laserColumnCollision(laser, column)

        for column in self.columnList:
            self.columnPlayerCollision(column, self.player)

        for laser in self.laserList:
            self.laserMirrorCollision(self.playerMirror, laser)
            self.playerLaserCollision(self.player, laser)

        for wall in self.wallList:
            self.wallPlayerCollision(self.player, wall)

        for wall in self.wallList:
            if wall.reflective:
                for laser in self.laserList:
                    self.wallLaserCollision(wall, laser)

    def playerLaserCollision(self, player, laser):
        if player.ifCollides(laser.front) and not self.playerDed:
            self.playerDed = True
            print("U died to a bad laser.")

    def wallLaserCollision(self, wall, laser):
        if ifPolygonCollidesWithRound(wall.collisionModel, laser.front):
            surface = whichSurfaceOfPolygonCollidesWithRound(wall.collisionModel, laser.front)
            laser.reactToCollision(surface)

    def wallPlayerCollision(self, player, wall):
        if ifPolygonCollidesWithRound(wall.collisionModel, player): # TODO: Transfer wall to polygon
            player.reactToFlatCollision( whichSurfaceOfPolygonCollidesWithRound(wall.collisionModel, player) )

    def columnPlayerCollision(self, column, player):
        if ifRoundCollidesWithRound(player, column):
            player.reactToRoundCollision(column.getPoint())

    def laserColumnCollision(self, laser, column):
        if ifRoundCollidesWithRound(laser.front, column):
            laser.reactToRoundCollision(column.getPoint())

    def laserMirrorCollision(self, mirror, laser):
        if ifPointCollidesWithLine(laser.getFrontPoint(), mirror.getSurface()):
            laser.reactToCollision(mirror.getSurface())