import copy


class NonInertialObject:
    """An object that moves with constant velocity in a given direction."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 300
        self.vy = 300

    def move(self, dir_x, dir_y, dt):
        self.x += self.vx*dir_x*dt
        self.y += self.vy*dir_y*dt

    def setPosition(self, x, y):
        self.x = x
        self.y = y


class InertialObject(NonInertialObject):
    """An object that accelerates in a given direction. Moves in the direction of its momentum."""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.acc = 3000
        self.slowing = 900
        self.maxSpeed = 400
        self.vx = 0
        self.vy = 0

    def move(self, dir_x, dir_y, dt):
        self.x += self.vx*dt
        self.y += self.vy*dt

        self.vx += self.acc*dir_x*dt
        self.vy += self.acc*dir_y*dt

        self.vx = max(self.vx, -self.maxSpeed)
        self.vx = min(self.vx, self.maxSpeed)
        self.vy = max(self.vy, -self.maxSpeed)
        self.vy = min(self.vy, self.maxSpeed)

        self.vx = max(self.vx-self.slowing*dt, 0) if self.vx > 0 else min(self.vx+self.slowing*dt, 0)
        self.vy = max(self.vy-self.slowing*dt, 0) if self.vy > 0 else min(self.vy+self.slowing*dt, 0)



