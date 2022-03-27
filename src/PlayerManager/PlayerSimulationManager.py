from src.PlayerManager.PlayerVisualManager import PlayerVisualManager


class PlayerSimulationManager:
    def __init__(self, DISPLAY, x, y):
        self.x = x
        self.y = y
        self.playerVisualManager = PlayerVisualManager(DISPLAY)

    def updateVisualManager(self):  # updates sprite position
        self.playerVisualManager.update(self.x, self.y)

    def draw(self):  # draws sprite
        self.playerVisualManager.draw()
        