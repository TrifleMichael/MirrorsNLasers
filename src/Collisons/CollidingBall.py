from AtomicObjects.Movables import NonInertialObject
from Collisons.RoundCollisonModel import RoundCollisionModel


class CollidingBall(RoundCollisionModel):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.moveModel = NonInertialObject(x, y)

    def update(self):
        self.moveModel.x = self.x
        self.moveModel.y = self.y

    def move(self, dir_x, dir_y, dt):
        self.moveModel.move(dir_x, dir_y, dt)
        self.x = self.moveModel.x
        self.y = self.moveModel.y
