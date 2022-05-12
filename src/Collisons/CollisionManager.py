from src.Collisons.CollisionFunctions import ifPolygonCollidesWithRound, ifPointCollidesWithLine, \
    whichSurfaceOfPolygonCollidesWithRound
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.LaserUtility.Laser import Laser
from src.Structures import RectangleWall, Column


class CollisionManager:
    def __init__(self, playerMirror, player):
        self.playerMirror = playerMirror
        self.player = player

        self.roundCollisionModels = [player]  # colliders that don't move
        self.laserList = []  # Laser type
        self.wallList = []

        self.playerDed = False

    def add(self, obj):
        if isinstance(obj, Laser):
            self.laserList.append(obj)
        if isinstance(obj, RectangleWall):
            self.wallList.append(obj)
        if isinstance(obj, Column):
            self.roundCollisionModels.append(obj)

    def update(self):
        for i in range(len(self.roundCollisionModels)):
            for j in range(i + 1, len(self.roundCollisionModels)):
                if self.roundCollisionModels[i].ifCollides(self.roundCollisionModels[j]):
                    self.roundCollisionModels[i].reactToCollision()
                    self.roundCollisionModels[j].reactToCollision()

        for laser in self.laserList:
            self.laserMirrorCollision(self.playerMirror, laser)
            self.playerLaserCollision(self.player, laser)

        for wall in self.wallList:
            if self.wallPlayerCollision(self.player, wall):
                self.player.reactToCollision()

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
        return ifPolygonCollidesWithRound(wall.collisionModel, player) # TODO: Transfer wall to polygon

    def laserMirrorCollision(self, mirror, laser):
        if ifPointCollidesWithLine(laser.getFrontPoint(), mirror.getSurface()):
            laser.reactToCollision(mirror.getSurface())