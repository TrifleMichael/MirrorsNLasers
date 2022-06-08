from src import display
from src.GuidedMovementModels.BasicEnemy import BasicEnemy


class EnemyManager:
    def __init__(self, level):
        self.level = level
        self.enemyList = []

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
