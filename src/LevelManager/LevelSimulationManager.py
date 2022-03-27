from src.LevelManager.LevelVisualManager import LevelVisualManager


class LevelSimulationManager:
    def __init__(self, DISPLAY, width, height):
        self.levelVisualManager = LevelVisualManager(DISPLAY, width, height)
        self.width = width
        self.height = height

    def updateVisualManager(self):
        pass  # stand holder function, might want to change background in the future
