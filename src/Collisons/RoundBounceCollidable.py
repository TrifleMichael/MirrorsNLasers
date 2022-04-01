from src.Utility.EuclidianFunctions import distance


class RoundBounceCollidable:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius

    def collides(self, other):
        return distance(self.x, self.y, other.x, other.y) < self.radius + other.radius

    def bounce(self):
        self.vx = -self.vx
        self.vy = -self.vy
