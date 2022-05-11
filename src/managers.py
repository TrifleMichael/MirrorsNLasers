from abc import ABC, abstractmethod

from src.LaserUtility.Laser import Laser


class Manager(ABC):
    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def draw(self, *args):
        pass


class LaserManager(Manager):
    """Manages the lasers"""
    def __init__(self,):
        self.laserList = []

    def createLaser(self, r, x1, y1, x2, y2, speed):
        self.laserList.append(Laser(r, x1, y1, x2, y2, speed))

    def update(self, dt):
        for laser in self.laserList:
            laser.move(dt)

    def draw(self):
        for laser in self.laserList:
            laser.draw()


class StructureManager(Manager): # TODO
    """Manages the structures"""
    def __init__(self,):
        self.structureList = []

    def update(self, *args):
        pass

    def draw(self, *args):
        pass