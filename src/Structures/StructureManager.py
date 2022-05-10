from src.Structures.Wall import Wall


class StructureManager:
    def __init__(self, DISPLAY, levelSimulationManager):
        self.display = DISPLAY
        self.levelSimulationManager = levelSimulationManager

    def readSaveFile(self, PATH):
        file = None  # Reads some file
        line = None  # Read line from file
        self.addWall(self.interpretWallData(line))

    def interpretWallData(self, wallData):
        pass
        # return x, y, width, height

    def addWall(self, x, y, width, heigth):
        # INTERPRETS SOME OUTSIDE INPUT
        self.levelSimulationManager.addWall(x, y, width, heigth)
