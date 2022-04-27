from math import sin, cos, atan2, pi, sqrt

from src.AtomicObjects.LineSprite import LineSprite
from src.Collisons.CollidingBall import CollidingBall


class Laser:
    def __init__(self, r, x1, y1, x2, y2, speed, dt, display):
        self.front = CollidingBall(x1, y1, r)
        self.end = CollidingBall(x2, y2, r)

        self.front.moveModel.vx = speed
        self.front.moveModel.vy = speed
        self.end.moveModel.vx = speed
        self.end.moveModel.vy = speed

        self.length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.sprite = LineSprite((x1, y1), (x2, y2), display)

        self.angle = (atan2(x2 - x1, y2 - y1) + pi) % (2 * pi)
        self.dt = dt
        self.framesUntilFlip = -1  # -1 means not waiting for flip

    def move(self):
        dir_x = sin(self.angle)
        dir_y = cos(self.angle)
        self.front.move(dir_x, dir_y, self.dt)
        self.end.move(dir_x, dir_y, self.dt)
        self.flipCountDown()

    def ifCollidesWithRCM(self, otherRCM):
        return otherRCM.ifCollides(self.front)

    def reactToCollision(self):
        #self.front.moveModel.vx *= -1
        self.front.moveModel.vy *= -1
        currentSpeed = sqrt(self.end.moveModel.vx ** 2 + self.end.moveModel.vy ** 2)
        print(self.length / currentSpeed / self.dt)
        self.framesUntilFlip = int(self.length / currentSpeed / self.dt)

    def flipCountDown(self):
        if self.framesUntilFlip == 0:
            self.framesUntilFlip = -1
            #self.end.moveModel.vx *= -1
            self.end.moveModel.vy *= -1
        elif self.framesUntilFlip != -1:
            self.framesUntilFlip -= 1


    def draw(self):
        self.sprite.update((self.front.x, self.front.y), (self.end.x, self.end.y))
        self.sprite.draw()
