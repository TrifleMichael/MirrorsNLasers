from math import sin, cos, atan2, pi, sqrt

from src.AtomicObjects.LineSprite import LineSprite
from src.AtomicObjects.MultiLineSprite import MultiLineSprite
from src.Collisons.CollidingBall import CollidingBall
from src.Utility.EuclidianFunctions import lineAngle, bounceVector


class Laser:
    def __init__(self, r, x1, y1, x2, y2, speed, dt, display):
        self.front = CollidingBall(x1, y1, r)
        self.end = CollidingBall(x2, y2, r)

        self.front.moveModel.vx = speed
        self.front.moveModel.vy = speed
        self.end.moveModel.vx = speed
        self.end.moveModel.vy = speed

        self.length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.lineSprite = LineSprite((x1, y1), (x2, y2), display)
        self.multiLineSprite = MultiLineSprite([], display)

        self.angle = lineAngle((x1, y1), (x2, y2))
        self.dt = dt
        self.framesUntilFlip = -1  # -1 means not waiting for flip, > 0 means executing flip, 0 means ending flip
        self.flipCoords = None
        self.flipSurfaceLine = None

    def move(self):
        dir_x = sin(self.angle)
        dir_y = cos(self.angle)
        self.front.move(dir_x, dir_y, self.dt)
        self.end.move(dir_x, dir_y, self.dt)
        self.flipCountDown()

    def updateMultiLineSprite(self):
        self.multiLineSprite.update([(self.front.moveModel.x, self.front.moveModel.y),
                                     (self.flipCoords[0], self.flipCoords[1]),
                                     (self.end.moveModel.x, self.end.moveModel.y)])

    def ifCollidesWithRCM(self, otherRCM):
        return otherRCM.ifCollides(self.front)

    def reactToCollision(self, flipSurface):
        """Bounces of surface defined by two points"""
        self.flipSurfaceLine = flipSurface
        self.front.moveModel.vx, self.front.moveModel.vy = bounceVector((self.front.moveModel.vx, self.front.moveModel.vy), flipSurface[0], flipSurface[1])

        self.flipCoords = (self.front.moveModel.x, self.front.moveModel.y)
        currentSpeed = sqrt(self.end.moveModel.vx ** 2 + self.end.moveModel.vy ** 2)
        self.framesUntilFlip = int(self.length / currentSpeed / self.dt * 1.4)

    def flipCountDown(self):
        if self.framesUntilFlip == 0:
            self.framesUntilFlip = -1
            self.end.moveModel.vx = self.front.moveModel.vx
            self.end.moveModel.vy = self.front.moveModel.vy
            # above code may make laser fly sideways if two collisions happen in short period of time
            self.end.moveModel.x, self.end.moveModel.y = self.flipCoords
        elif self.framesUntilFlip != -1:
            self.framesUntilFlip -= 1

    def draw(self):
        if self.framesUntilFlip >= 0 and self.framesUntilFlip != -1:
            self.updateMultiLineSprite()
            self.multiLineSprite.draw()
        else:
            self.lineSprite.update((self.front.x, self.front.y), (self.end.x, self.end.y))
            self.lineSprite.draw()
