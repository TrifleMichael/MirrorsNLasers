import pygame
from src.AtomicObjects.CircleSprite import CircleSprite
from src.AtomicObjects.Collidables import Collidable
from src.AtomicObjects.Movables import InertialObject


class PlayerSimulationManager(InertialObject, Collidable):
    def __init__(self, DISPLAY, x, y):
        super().__init__(x, y)
        self.playerVisualManager = PlayerVisualManager(DISPLAY)

        self.dir_y = 0
        self.dir_x = 0

    def update(self, keys, dt):
        self.readKeys(keys)
        self.move(self.dir_x, self.dir_y, dt)

        self.updateVisualManager()

    def readKeys(self, keys):
        self.dir_y = keys[pygame.K_s] - keys[pygame.K_w]
        self.dir_x = keys[pygame.K_d] - keys[pygame.K_a]
        norm = (self.dir_x**2 + self.dir_y**2)**0.5
        if norm != 0:
            self.dir_x /= norm
            self.dir_y /= norm


    def updateVisualManager(self):  # updates sprite position
        self.playerVisualManager.update(self.x, self.y)

    def draw(self):  # draws sprite
        self.playerVisualManager.draw()


class PlayerVisualManager:
    def __init__(self, DISPLAY):
        self.playerSprite = CircleSprite(50)
        self.DISPLAY = DISPLAY
        self.x = None  # initialized in update()
        self.y = None

    def draw(self):
        self.playerSprite.draw(self.DISPLAY, self.x, self.y)

    def update(self, x, y):
        self.x = x
        self.y = y
