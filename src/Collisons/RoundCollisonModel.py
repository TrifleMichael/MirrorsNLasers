from src.Utility.EuclidianFunctions import distance


class RoundCollisionModel:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def ifCollides(self, otherRCM):  # RCM - RoundCollisionModel
        return distance(otherRCM.x, otherRCM.y, self.x, self.y) < self.r + otherRCM.r

    def update(self, x, y):
        self.x = x
        self.y = y
