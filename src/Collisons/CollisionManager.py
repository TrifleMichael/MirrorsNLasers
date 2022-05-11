from src.Collisons.CollisionFunctions import ifPolygonCollidesWithRound, ifPointCollidesWithLine
from src.Utility.EuclidianFunctions import pointToSegmentDistance


class CollisionManager:
    def __init__(self, playerMirror, player):
        self.roundCollisionModels = []  # colliders that don't move
        self.laserList = []  # Laser type
        self.playerMirror = playerMirror
        self.player = player

        self.playerDed = False

    def addLaser(self, headOfLaser):
        self.laserList.append(headOfLaser)

    def checkCollisions(self):
        for i in range(len(self.roundCollisionModels)):
            for j in range(i + 1, len(self.roundCollisionModels)):
                if self.roundCollisionModels[i].ifCollides(self.roundCollisionModels[j]):
                    self.roundCollisionModels[i].reactToCollision()
                    self.roundCollisionModels[j].reactToCollision()

        for laser in self.laserList:
            self.laserMirrorCollision(self.playerMirror, laser)
            self.playerLaserCollision(self.player, laser)

    def playerLaserCollision(self, player, laser):
        if player.ifCollides(laser.front) and not self.playerDed:
            self.playerDed = True
            print("U died to a bad laser.")

    def wallPlayerCollision(self, player, wall):
        ifPolygonCollidesWithRound(player.move, wall) # TODO: Transfer wall to polygon

    def laserMirrorCollision(self, mirror, laser):
        if ifPointCollidesWithLine(laser.getFrontPoint(), mirror.getSurface()):
            laser.reactToCollision(mirror.getSurface())