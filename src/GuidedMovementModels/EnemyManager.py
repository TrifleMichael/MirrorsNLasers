from src import display
from src.GuidedMovementModels.BasicEnemy import BasicEnemy
from src.Utility.EuclidianFunctions import pointsNormalVector, extendVector, sumVectors, shiftVector


class EnemyManager:
    def __init__(self, level):
        self.level = level
        self.enemyList = []
        self.LASER_LENGTH = 30

    def getPlayerLocation(self):
        return self.level.player.getPoint()

    def update(self, dt):
        for enemy in self.enemyList:
            enemy.performMove(dt)  # Enemy must move before evaluating move, as evaluation can update during game loop
            enemy.evaluateMove()

    def addEnemy(self, enemy):
        self.enemyList.append(enemy)

    def draw(self):
        for enemy in self.enemyList:
            enemy.draw()

    def removeEnemy(self, enemy):
        self.enemyList.remove(enemy)
        self.level.collisionManager.enemyList.remove(enemy)

    def shootLaserAtPlayer(self, enemy):
        enemyPosition = enemy.getPoint()
        normalVec = pointsNormalVector(enemyPosition, self.getPlayerLocation())
        vecAtEnemyPosition = [[enemyPosition[0], enemyPosition[1]],
                              [enemyPosition[0] + normalVec[0], enemyPosition[1] + normalVec[1]]]
        vecAtEnemyPosition = extendVector(vecAtEnemyPosition, self.LASER_LENGTH)
        shiftedVector = [[0, 0], [normalVec[0], normalVec[1]]]
        shiftedVector = extendVector(shiftedVector, enemy.collisionModel.r + 5)

        resultVector = shiftVector(vecAtEnemyPosition, shiftedVector[1][0], shiftedVector[1][1])
        laserVector = [resultVector[1], resultVector[0]]

        self.level.addLaser(laserVector)



