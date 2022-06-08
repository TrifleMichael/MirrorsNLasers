import math
from math import sin, cos, sqrt

from src.Sprites.LineSprite import LineSprite
from src.Sprites.MultiLineSprite import MultiLineSprite
from src.Collisons.CollidingBall import CollidingBall
from src.Utility.EuclidianFunctions import lineAngle, bounceVector, pointToLineDistance, surfaceContainsPointShadow, \
    lineTangentToPoints, pointsNormalVector, extendVector, movePointAwayFromSurface, movePointAwayFromPoint
from src.Settings import frameDuration


class Laser:
    def __init__(self, r, x1, y1, x2, y2, speed):
        self.front = CollidingBall(x1, y1, r)
        self.end = CollidingBall(x2, y2, r)

        self.front.moveModel.vx = speed
        self.front.moveModel.vy = speed
        self.end.moveModel.vx = speed
        self.end.moveModel.vy = speed

        self.length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.lineSprite = LineSprite(color=(255, 0, 255))
        self.multiLineSprite = MultiLineSprite(color=(255, 0, 255))

        self.framesUntilFlip = -1  # -1 means not waiting for flip, > 0 means executing flip, 0 means ending flip
        self.flipCoords = None

        self.collisionEpsilon = 5

        self.bounceImmunityFrames = 0
        self.maxBounceImmunityFrames = 30

        self.setupStartingSpeed(speed)

    def setupStartingSpeed(self, speed):
        normalVec = pointsNormalVector([self.end.moveModel.x, self.end.moveModel.y], [self.front.moveModel.x, self.front.moveModel.y])
        speedVec = extendVector([[0, 0], normalVec[:]], speed)
        self.front.moveModel.vx = speedVec[1][0]
        self.front.moveModel.vy = speedVec[1][1]
        self.end.moveModel.vx = speedVec[1][0]
        self.end.moveModel.vy = speedVec[1][1]

    def move(self, dt):
        self.front.move(1, 1, dt)
        self.end.move(1, 1, dt)
        self.flipCountDown()
        if self.bounceImmunityFrames != 0:
            self.bounceImmunityFrames -= 1

    def ifCollidesWithRCM(self, otherRCM):
        return otherRCM.ifCollides(self.front)

    def collidesWithSurface(self, surface):
        ptld = pointToLineDistance(surface, (self.front.moveModel.x, self.front.moveModel.y))
        if self.collisionEpsilon >= ptld and surfaceContainsPointShadow(surface, [self.front.moveModel.x, self.front.moveModel.y]):
            if self.bounceImmunityFrames == 0:
                self.reactToCollision(surface)

    def reactToCollision(self, flipSurface):
        """Bounces of surface defined by two points"""
        self.front.moveModel.vx, self.front.moveModel.vy = bounceVector((self.front.moveModel.vx, self.front.moveModel.vy), flipSurface[0], flipSurface[1])
        self.bounceImmunityFrames = self.maxBounceImmunityFrames
        self.flipCoords = (self.front.moveModel.x, self.front.moveModel.y)
        self.front.moveModel.x, self.front.moveModel.y = movePointAwayFromSurface(self.getFrontPoint(), flipSurface, 2)
        currentSpeed = sqrt(self.end.moveModel.vx ** 2 + self.end.moveModel.vy ** 2)
        self.framesUntilFlip = int(self.length / currentSpeed / frameDuration)

    def reactToRoundCollision(self, point):
        self.front.moveModel.x, self.front.moveModel.y = movePointAwayFromPoint(self.getFrontPoint(), point, 2)
        flipSurface = lineTangentToPoints(self.front.getPoint(), point)
        self.reactToCollision(flipSurface)

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
            p1 = (self.front.moveModel.x, self.front.moveModel.y)
            p2 = (self.flipCoords[0], self.flipCoords[1])
            p3 = (self.end.moveModel.x, self.end.moveModel.y)
            self.multiLineSprite.draw([p1, p2, p3])
        else:
            p1 = (self.front.moveModel.x, self.front.moveModel.y)
            p2 = (self.end.moveModel.x, self.end.moveModel.y)
            self.lineSprite.draw(p1, p2)

    def getFrontPoint(self):
        return self.front.moveModel.x, self.front.moveModel.y
