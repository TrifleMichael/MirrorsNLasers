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
            enemy.evaluateMove(dt)

    def addEnemy(self, enemy):
        self.enemyList.append(enemy)

    def draw(self):
        for enemy in self.enemyList:
            enemy.draw()
