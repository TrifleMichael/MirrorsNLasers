from src.AtomicObjects.Movables import NonInertialObject
from src.Collisons.RoundCollisonModel import RoundCollisionModel


class CollidingBall(RoundCollisionModel):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self.moveModel = NonInertialObject(x, y)

    def update(self):
        self.moveModel.x = self.x
        self.moveModel.y = self.y

    def move(self, dir_x, dir_y, dt):
        self.moveModel.move(dir_x, dir_y, dt)
        self.x = self.moveModel.x
        self.y = self.moveModel.y
