from cmath import sqrt
from math import sin, cos

from src.AtomicObjects.LineSprite import LineSprite
from src.Collisons.CollidingBall import CollidingBall


class Laser:
    def __init__(self, r, x1, y1, x2, y2, speed, angle, dt, display):
        self.front = CollidingBall(x1, y1, r)
        self.end = CollidingBall(x2, y2, r)

        self.length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.sprite = LineSprite((x1, y1), (x2, y2), display)

        self.speed = speed
        self.angle = angle # from top clockwise
        self.dt = dt

    def move(self):
        dir_x = sin(self.angle)
        dir_y = cos(self.angle)
        self.front.move(dir_x, dir_y, self.dt)
        self.end.move(dir_x, dir_y, self.dt)

    def ifCollidesWithRCM(self, otherRCM):
        return otherRCM.ifCollides(self.front)

    def reactToCollision(self):
        self.front.moveModel.vx *= -1
        self.front.moveModel.vy *= -1
        #self.timeToFlip = self.length / 
        # timer for flipping back of laser?

    def calculateSpeed(self):
        pass

    def draw(self):
        self.sprite.draw()