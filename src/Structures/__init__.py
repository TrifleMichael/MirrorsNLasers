from abc import ABC, abstractmethod


class Structure(ABC):
    """Abstract class for all sprites. Forces child classes to implement draw."""

    @abstractmethod
    def draw(self, *args, **kwargs):
        pass


class StructureManager:
    """Manages the structures"""

    def __init__(self):
        self.structureList = []

    def add(self, structure):
        self.structureList.append(structure)

    def update(self, *args):
        pass

    def draw(self):
        for structure in self.structureList:
            structure.draw()
