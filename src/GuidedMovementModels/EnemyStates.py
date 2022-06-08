from enum import Enum


class EnemyState(Enum):
    standingStill = 1
    approachingPlayer = 2
    circlingPlayerRight = 3
    circlingPlayerLeft = 4
    escapingPlayer = 5