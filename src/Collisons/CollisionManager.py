class CollisionManager:
    def __init__(self):
        self.roundCollisionModels = [] # colliders that don't move

    def checkCollisions(self):
        for i in range(len(self.roundCollisionModels)):
            for j in range(i+1, len(self.roundCollisionModels)):
                if self.roundCollisionModels[i].ifCollides(self.roundCollisionModels[j]):
                    # check future (not acutal) positions of colliders, call actual colliders as below
                    self.roundCollisionModels[i].reactToCollision()
                    self.roundCollisionModels[j].reactToCollision()

