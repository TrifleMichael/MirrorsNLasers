from src.Utility.EuclidianFunctions import distance
from abc import ABC, abstractmethod


class RoundCollisionModel:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def ifCollides(self, otherRCM):  # RCM - RoundCollisionModel
        return distance(otherRCM.x, otherRCM.y, self.x, self.y) < self.r + otherRCM.r

    @abstractmethod
    def reactToCollision():
        pass

    def update(self, x, y):
        self.x = x
        self.y = y
