class NonInertialObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 10

    def move(self, field, directions):
        if directions[0] and self.y - self.v > 0:
            self.y -= self.v
        if directions[1] and self.x + self.v < field.width:
            self.x += self.v
        if directions[2] and self.y + self.v < field.height:
            self.y += self.v
        if directions[3] and self.x - self.v > 0:
            self.x -= self.v