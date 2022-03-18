class InertialObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.acc = 0.7
        self.slowing = 0.5
        self.maxV = 10

    def move(self, field, directions):
        if 0 < self.x + self.vx < field.width:
            self.x += self.vx
        else:
            self.vx = 0

        if 0 < self.y + self.vy < field.height:
            self.y += self.vy
        else:
            self.vy = 0

        if directions[0] and self.vy - self.acc > -self.maxV:
            self.vy -= self.acc
        if directions[1] and self.vx + self.acc < self.maxV:
            self.vx += self.acc
        if directions[2] and self.vy + self.acc < self.maxV:
            self.vy += self.acc
        if directions[3] and self.vx - self.acc > -self.maxV:
            self.vx -= self.acc

        if abs(self.vx) - self.slowing > 0:
            self.vx -= abs(self.vx) / self.vx * self.slowing
        else:
            self.vx = 0

        if abs(self.vy) - self.slowing > 0:
            self.vy -= abs(self.vy) / self.vy * self.slowing
        else:
            self.vy = 0