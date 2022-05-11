from abc import ABC, abstractmethod

from src.LaserUtility.Laser import Laser


class Manager(ABC):
    @abstractmethod
    def add(self, *args):
        pass

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

    def add(self, laser):
        self.laserList.append(laser)

    def update(self, dt):
        for laser in self.laserList:
            laser.move(dt)

    def draw(self):
        for laser in self.laserList:
            laser.draw()


class StructureManager(Manager):  # TODO
    """Manages the structures"""
    def __init__(self,):
        self.structureList = []

    def add(self, structure):
        self.structureList.append(structure)

    def update(self, *args):
        pass

    def draw(self):
        for structure in self.structureList:
            structure.draw()
