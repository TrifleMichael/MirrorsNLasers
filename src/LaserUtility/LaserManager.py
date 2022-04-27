from src.LaserUtility.Laser import Laser


class LaserManager:
    def __init__(self, dt, display):
        self.dt = dt
        self.display = display
        self.laserList = []

    def createLaser(self, r, x1, y1, x2, y2, speed):
        self.laserList.append(Laser(r, x1, y1, x2, y2, speed, self.dt, self.display))

    def move(self):
        for laser in self.laserList:
            laser.move()

    def draw(self):  # stand in, LevelVisualManager should handle drawing sprites
        for laser in self.laserList:
            laser.draw()
