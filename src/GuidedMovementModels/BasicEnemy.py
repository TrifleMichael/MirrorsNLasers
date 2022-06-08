from random import randrange

from src.AtomicObjects.Movables import NonInertialObject
from src.Collisons.CollisionFunctions import surfaceOfPolygonRoundCollision
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.GuidedMovementModels.EnemyStates import EnemyState
from src.Sprites.CircleSprite import CircleSprite
from src.Utility.EuclidianFunctions import pointsNormalVector, movePointAwayFromSurface, movePointAwayFromPoint, \
    pointToPointDistance, rotate2dLine


class BasicEnemy:
    def __init__(self, x, y, r, enemyManager):
        self.movementModel = NonInertialObject(x, y) # TODO: Add collision model
        self.collisionModel = RoundCollisionModel(x, y, r)
        self.sprite = CircleSprite(r)
        self.state = EnemyState.approachingPlayer
        self.enemyGuider = enemyManager

        self.movementModel.vx = 90
        self.movementModel.vy = 90
        self.circlingCountdown = 0

    def draw(self):
        self.sprite.draw(self.movementModel.x, self.movementModel.y)

    def getPoint(self):
        return self.movementModel.x, self.movementModel.y

    def changePosition(self, x, y):
        self.movementModel.x = x
        self.movementModel.y = y
        self.collisionModel.x = x
        self.collisionModel.y = y

    def move(self, dir_x, dir_y, dt):
        self.movementModel.move(dir_x, dir_y, dt)
        self.collisionModel.x = self.movementModel.x
        self.collisionModel.y = self.movementModel.y

    def reactToLaser(self, laser):
        self.enemyGuider.removeEnemy(self)

    def reactToWall(self, wall):
        self.state = EnemyState.standingStill
        collisionBody = surfaceOfPolygonRoundCollision(wall.collisionModel, self.collisionModel)
        if type(collisionBody[0]) is list or type(collisionBody[0]) is tuple:
            pts = movePointAwayFromSurface(self.getPoint(), collisionBody, 2)
            self.changePosition(pts[0], pts[1])
        else:
            pts = movePointAwayFromPoint(self.getPoint(), collisionBody, 2)
            self.changePosition(pts[0], pts[1])

    def reactToColumn(self, column):
        self.state = EnemyState.standingStill
        pts = movePointAwayFromPoint(self.getPoint(), column.getPoint(), 2)
        self.changePosition(pts[0], pts[1])


    def evaluateMove(self):
        if pointToPointDistance(self.enemyGuider.getPlayerLocation(), self.getPoint()) > 400:
            self.circlingCountdown = 0
            self.state = EnemyState.approachingPlayer
        elif pointToPointDistance(self.enemyGuider.getPlayerLocation(), self.getPoint()) < 250:
            self.circlingCountdown = 0
            self.state = EnemyState.escapingPlayer
        elif self.circlingCountdown <= 0:
            self.circlingCountdown = randrange(200, 400)
            if self.state == EnemyState.circlingPlayerLeft:
                self.state = EnemyState.circlingPlayerRight
            else:
                self.state = EnemyState.circlingPlayerLeft
        else:
            self.circlingCountdown -= 1


    def performMove(self, dt):
        if self.state == EnemyState.approachingPlayer:
            direction = pointsNormalVector(self.getPoint(), self.enemyGuider.getPlayerLocation())
            self.move(direction[0], direction[1], dt)
        if self.state == EnemyState.circlingPlayerRight:
            direction = pointsNormalVector(self.getPoint(), self.enemyGuider.getPlayerLocation())
            direction = rotate2dLine(direction, [0, 0], [0, 0], pi / 2)
            direction = direction[0]
            self.move(direction[0], direction[1], dt)
        if self.state == EnemyState.circlingPlayerLeft:
            direction = pointsNormalVector(self.getPoint(), self.enemyGuider.getPlayerLocation())
            direction = rotate2dLine(direction, [0, 0], [0, 0], -pi / 2)
            direction = direction[0]
            self.move(direction[0], direction[1], dt)
        if self.state == EnemyState.escapingPlayer:
            direction = pointsNormalVector(self.getPoint(), self.enemyGuider.getPlayerLocation())
            direction = [-direction[0], -direction[1]]
            self.move(direction[0], direction[1], dt)
