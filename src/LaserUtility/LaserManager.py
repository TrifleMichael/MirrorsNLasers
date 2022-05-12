class LaserManager:
    """Manages the lasers"""
    def __init__(self,):
        self.laserList = []

    def add(self, laser):
        self.laserList.append(laser)

    def update(self, dt):
        for laser in self.laserList:
            laser.move(dt)

    def draw(self):
        for laser in self.laserList:
            laser.draw()