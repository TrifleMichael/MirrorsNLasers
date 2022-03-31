class Collidable:
    def distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

    def collides(self, other):
        if self.distance(other) < self.radius + other.radius:
            return True

    def bounce(self):
        self.vx = -self.vx
        self.vy = -self.vy
