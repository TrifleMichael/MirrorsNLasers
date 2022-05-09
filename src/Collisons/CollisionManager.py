class CollisionManager:
    def __init__(self, playerMirror):
        self.roundCollisionModels = []  # colliders that don't move
        self.laserList = []  # Laser type
        self.playerMirror = playerMirror

    def addLaser(self, headOfLaser):
        self.laserList.append(headOfLaser)

    def checkCollisions(self):
        for i in range(len(self.roundCollisionModels)):
            for j in range(i + 1, len(self.roundCollisionModels)):
                if self.roundCollisionModels[i].ifCollides(self.roundCollisionModels[j]):
                    self.roundCollisionModels[i].reactToCollision()
                    self.roundCollisionModels[j].reactToCollision()

        for laser in self.laserList:
            laser.collidesWithSurface(self.playerMirror.getSurface())
