from src.Collisons.CollisionFunctions import ifPolygonCollidesWithRound, ifPointCollidesWithLine, \
    whichSurfaceOfPolygonCollidesWithRound
from src.Utility.EuclidianFunctions import pointToSegmentDistance


class CollisionManager:
    def __init__(self, playerMirror, player):
        self.roundCollisionModels = []  # colliders that don't move
        self.laserList = []  # Laser type
        self.wallList = []
        self.playerMirror = playerMirror
        self.player = player

        self.playerDed = False

    def addLaser(self, headOfLaser):
        self.laserList.append(headOfLaser)

    def addWall(self, wall):
        self.wallList.append(wall)

    def checkCollisions(self):
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

            if wall.ifReflective:
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