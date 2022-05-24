from src.AtomicObjects.Movables import NonInertialObject
from src.Collisons.CollisionFunctions import surfaceOfPolygonRoundCollision
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.GuidedMovementModels.EnemyStates import EnemyState
from src.Sprites.CircleSprite import CircleSprite
from src.Utility.EuclidianFunctions import pointsNormalVector


class BasicEnemy:
    def __init__(self, x, y, r, enemyManager):
        self.movementModel = NonInertialObject(x, y) # TODO: Add collision model
        self.collisionModel = RoundCollisionModel(x, y, r)
        self.sprite = CircleSprite(r)
        self.state = EnemyState.approachingPlayer
        self.enemyGuider = enemyManager

        self.movementModel.vx = 150
        self.movementModel.vy = 150

    def draw(self):
        self.sprite.draw(self.movementModel.x, self.movementModel.y)

    def getPoint(self):
        return self.movementModel.x, self.movementModel.y

    def move(self, dir_x, dir_y, dt):
        self.movementModel.move(dir_x, dir_y, dt)
        self.collisionModel.x = self.movementModel.x
        self.collisionModel.y = self.movementModel.y

    def reactToWall(self, wall):
        print("Enemy hit the wall")


    def evaluateMove(self, dt):
        if self.state == EnemyState.approachingPlayer:
            direction = pointsNormalVector(self.getPoint(), self.enemyGuider.getPlayerLocation())
            self.move(direction[0], direction[1], dt)

