from src.Collisons.CollisionFunctions import ifPointCollidesWithLine, \
    ifRoundCollidesWithRound, surfaceOfPolygonRoundCollision
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.GuidedMovementModels import BasicEnemy
from src.LaserUtility.Laser import Laser
from src.Structures.Door import Door
from src.Structures.LaserDetector import LaserDetector
from src.Structures.Pit import Pit
from src.Structures.RectangleWall import RectangleWall
from src.Structures.Column import Column
from src.Structures.PolygonWall import PolygonWall
from src.Structures.WinFlag import WinFlag
from src.Utility.EuclidianFunctions import movePointAwayFromSurface, movePointAwayFromPoint, pointToPointDistance


class CollisionManager:
    def __init__(self, playerMirror, player):
        self.playerMirror = playerMirror
        self.player = player

        self.columnList = []
        self.laserList = []
        self.wallList = []
        self.polygonWallList = []
        self.pitList = []
        self.laserDetectorList = []
        self.enemyList = []
        self.winFlags = []
        self.doorList = []

    def add(self, obj):
        if isinstance(obj, Laser):
            self.laserList.append(obj)
        if isinstance(obj, RectangleWall):
            self.wallList.append(obj)
        if isinstance(obj, Column):
            self.columnList.append(obj)
        if isinstance(obj, PolygonWall):
            self.polygonWallList.append(obj)
        if isinstance(obj, Pit):
            self.pitList.append(obj)
        if isinstance(obj, LaserDetector):
            self.laserDetectorList.append(obj)
        if isinstance(obj, WinFlag):
            self.winFlags.append(obj)
        if isinstance(obj, Door):
            self.doorList.append(obj)

    def addEnemy(self, enemy):  # is instance doesn't work for weird reasons
        self.enemyList.append(enemy)

    def update(self):
        for column in self.columnList:
            for laser in self.laserList:
                self.laserColumnCollision(laser, column)

        for column in self.columnList:
            self.columnPlayerCollision(column, self.player)

        for laser in self.laserList:
            self.laserMirrorCollision(self.playerMirror, laser)
            self.playerLaserCollision(self.player, laser)

        for wall in self.wallList + self.polygonWallList:
            self.wallPlayerCollision(self.player, wall)

        for wall in self.wallList + self.polygonWallList:
            if wall.reflective:
                for laser in self.laserList:
                    self.wallLaserCollision(wall, laser)

        for pit in self.pitList:
            self.playerPitCollision(self.player, pit)

        for laserDetector in self.laserDetectorList:
            for laser in self.laserList:
                self.laserDetectorLaserCollision(laserDetector, laser)

        for enemy in self.enemyList:
            for otherEnemy in self.enemyList:
                if self is not otherEnemy:
                    self.enemyEnemyCollision(enemy, otherEnemy)

            for wall in self.wallList + self.polygonWallList:
                self.enemyWallCollision(enemy, wall)
            for column in self.columnList:
                self.enemyColumnColision(enemy, column)
            for laser in self.laserList:
                self.enemyLaserCollision(enemy, laser)
            for pit in self.pitList:
                self.enemyPitCollision(enemy, pit)

        for flag in self.winFlags:
            self.playerFlagCollision(self.player, flag)

        for door in self.doorList:
            self.playerDoorCollision(self.player, door)

    def enemyEnemyCollision(self, enemy1, enemy2):
        # TODO: Fix
        # Quickfix because the same references are not differentiated by is
        if not pointToPointDistance(enemy1.getPoint(), enemy2.getPoint()) == 0:
            if ifRoundCollidesWithRound(enemy1.collisionModel, enemy2.collisionModel):
                enemy1.reactToRoundCollision(enemy2)

    def enemyPitCollision(self, enemy, pit):
        if surfaceOfPolygonRoundCollision(pit.collisionModel, enemy.collisionModel) is not None:
            enemy.reactToPit(pit)

    def enemyLaserCollision(self, enemy, laser):
        if ifRoundCollidesWithRound(enemy.collisionModel, laser.front) or ifRoundCollidesWithRound(enemy.collisionModel,
                                                                                                   laser.end):
            enemy.reactToLaser(laser)

    def playerDoorCollision(self, player, door):
        result = surfaceOfPolygonRoundCollision(door.collisionModel, player)
        if result is not None:
            player.reactToFlatCollision(result)

    def enemyColumnColision(self, enemy, column):
        if ifRoundCollidesWithRound(enemy.collisionModel, column):
            enemy.reactToRoundCollision(column)

    def enemyWallCollision(self, enemy, wall):
        if surfaceOfPolygonRoundCollision(wall.collisionModel, enemy.collisionModel) is not None:
            enemy.reactToWall(wall)

    def laserDetectorLaserCollision(self, laserDetector, laser):
        result = surfaceOfPolygonRoundCollision(laserDetector.collisionModel, laser.front)
        if result is not None:
            laserDetector.reactToCollision()

    def playerFlagCollision(self, player, flag):
        result = surfaceOfPolygonRoundCollision(flag.collisionModel, player)
        if result is not None:
            player.win = True

    def playerPitCollision(self, player, pit):
        result = surfaceOfPolygonRoundCollision(pit.collisionModel, player)
        if result is not None:
            if type(result[0]) is list or type(result[0]) is tuple:
                surface = result
                player.vx = 0
                player.vy = 0
                player.x, player.y = movePointAwayFromSurface(player.getPoint(), surface, 1)
            else:
                point = result
                player.vx = 0
                player.vy = 0
                player.x, player.y = movePointAwayFromPoint(player.getPoint(), point, 1)

    def playerLaserCollision(self, player, laser):
        if player.ifCollides(laser.front) and player.alive:  # TODO: switch to new collision function
            player.damage()

    def wallLaserCollision(self, wall, laser):
        result = surfaceOfPolygonRoundCollision(wall.collisionModel, laser.front)
        if result is not None:
            if type(result[0]) is list or type(result[0]) is tuple:
                surface = result
                laser.reactToCollision(surface)
            else:
                point = result
                laser.reactToRoundCollision(point)

    def wallPlayerCollision(self, player, wall):
        result = surfaceOfPolygonRoundCollision(wall.collisionModel, player)
        if result is not None:
            if type(result[0]) is list or type(result[0]) is tuple:
                surface = result
                player.reactToFlatCollision(surface)
            else:
                point = result
                player.x, player.y = movePointAwayFromPoint(player.getPoint(), point, 1)
                player.reactToRoundCollision(point)

    def columnPlayerCollision(self, column, player):
        if ifRoundCollidesWithRound(player, column):
            player.reactToRoundCollision(column.getPoint())

    def laserColumnCollision(self, laser, column):
        if ifRoundCollidesWithRound(laser.front, column):
            laser.reactToRoundCollision(column.getPoint())

    def laserMirrorCollision(self, mirror, laser):
        if ifPointCollidesWithLine(laser.getFrontPoint(), mirror.getSurface()):
            laser.reactToCollision(mirror.getSurface())
