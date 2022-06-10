from math import copysign


class NonInertialObject:
    """An object that moves with constant velocity in a given direction."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 300
        self.vy = 300

    def move(self, dir_x, dir_y, dt):
        self.x += self.vx * dir_x * dt
        self.y += self.vy * dir_y * dt

    def getPosition(self):
        return self.x, self.y

    def setPosition(self, x, y):
        self.x = x
        self.y = y


class InertialObject(NonInertialObject):
    """An object that accelerates in a given direction. Moves in the direction of its momentum."""

    def __init__(self, x, y):
        NonInertialObject.__init__(self, x, y)
        self.acc = 4000
        self.slow = 0.90
        self.slow_const = 20
        self.maxSpeed = 300
        self.vx = 0
        self.vy = 0

        self.sgn = lambda n: copysign(1, n)

    def setAcceleration(self, acc):
        self.acc = acc

    def setMaxSpeed(self, maxSpeed):
        self.maxSpeed = maxSpeed

    def move(self, dir_x, dir_y, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx += self.acc * dir_x * dt
        self.vy += self.acc * dir_y * dt

        self.vx *= self.slow
        self.vy *= self.slow

        speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        if speed > self.maxSpeed:
            self.vx *= self.maxSpeed / speed
            self.vy *= self.maxSpeed / speed

        if not dir_x:
            self.vx = (self.vx - self.slow_const * self.sgn(self.vx) * dt) if abs(self.vx) > self.slow_const else 0
        if not dir_y:
            self.vy = (self.vy - self.slow_const * self.sgn(self.vy) * dt) if abs(self.vy) > self.slow_const else 0
