import math

import pygame
from src.Sprites.CircleSprite import CircleSprite
from src.AtomicObjects.Mirror import Mirror
from src.AtomicObjects.Movables import InertialObject
from src.Collisons.RoundCollisonModel import RoundCollisionModel


class PlayerSimulationManager(InertialObject, RoundCollisionModel):  # (InertialObject, RoundCollisionModel)
    def __init__(self, DISPLAY, x, y, r, field):
        InertialObject.__init__(self, x, y)
        RoundCollisionModel.__init__(self, x, y, r)
        self.playerVisualManager = PlayerVisualManager(DISPLAY, self.x, self.y)

        self.dir_y = 0
        self.dir_x = 0

        self.rotation = 0
        self.mirror = Mirror(self.x, self.y, 150, 0, DISPLAY)

        self.field = field

    def update(self, keys, dt):  # shadowing nazwy dziedziczonych
        self.readKeys(keys)
        self.move(self.dir_x, self.dir_y, dt)
        self.stayInField()

        self.mirror.setPosition(self.x + 70*math.cos(self.rotation), self.y + 70*math.sin(self.rotation))
        self.mirror.setRotation(self.rotation)
        self.updateVisualManager()

    def readKeys(self, keys):
        self.dir_y = keys[pygame.K_s] - keys[pygame.K_w]
        self.dir_x = keys[pygame.K_d] - keys[pygame.K_a]
        norm = (self.dir_x ** 2 + self.dir_y ** 2) ** 0.5
        if norm != 0:
            self.dir_x /= norm
            self.dir_y /= norm

        cursor = pygame.mouse.get_pos()
        self.rotation = math.atan2((cursor[1] - self.y), (cursor[0] - self.x))

    def stayInField(self):
        # temporary, map will be surrounded by walls
        if self.field.width < self.x + self.r:
            self.x = self.field.width - self.r
            self.vx *= -1
        if self.field.height < self.y + self.r:
            self.y = self.field.height - self.r
            self.vy *= -1
        if self.x - self.r < 0:
            self.x = self.r
            self.vx *= -1
        if self.y - self.r < 0:
            self.y = self.r
            self.vy *= -1
        #  self.y = max(self.y - self.r, 0) delete this line

    def reactToCollision(self):
        self.vx *= -1
        self.vy *= -1

    def updateVisualManager(self):  # updates sprite position
        self.playerVisualManager.update(self.x, self.y)
        self.mirror.visualManager.update(*self.mirror.getSurface())

    def draw(self):  # draws sprite
        self.playerVisualManager.draw()
        self.mirror.visualManager.draw()

    def getPosition(self):
        return self.x, self.y


class PlayerVisualManager:
    def __init__(self, display, x, y):
        self.playerSprite = CircleSprite(x, y, 50, display)
        self.x = x  # initialized in update()
        self.y = y

    def draw(self):
        self.playerSprite.draw()

    def update(self, x, y):
        self.x = x
        self.y = y
        self.playerSprite.update(x, y)
