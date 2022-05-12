import math

import pygame
from src.Sprites.CircleSprite import CircleSprite
from src.AtomicObjects.Mirror import Mirror
from src.AtomicObjects.Movables import InertialObject
from src.Collisons.RoundCollisonModel import RoundCollisionModel
from src.Utility.EuclidianFunctions import lineTangentToPoints, bounceVector, movePointAwayFromSurface, shiftLineToPoint


class Player(InertialObject, RoundCollisionModel):
    """A player is a movable object that can be controlled by (yeah) the player."""
    def __init__(self, x, y, radius=50):
        InertialObject.__init__(self, x, y)
        RoundCollisionModel.__init__(self, x, y, r=50)

        self.dir_y = 0
        self.dir_x = 0
        self.rotation = 0
        self.mirror = Mirror(self.x, self.y, width=150, rotation=0)

        self.sprite = CircleSprite(radius, color=(255, 0, 0))

    def update(self, keys, dt):
        """Updates the player's position and rotation based on the keys pressed."""
        self.readKeys(keys)
        self.move(self.dir_x, self.dir_y, dt)

        self.mirror.setPosition(self.x + 60*math.cos(self.rotation), self.y + 60*math.sin(self.rotation))
        self.mirror.setRotation(self.rotation)

    def readKeys(self, keys):
        """Reads the keys and sets player's direction accordingly."""
        self.dir_y = keys[pygame.K_s] - keys[pygame.K_w]
        self.dir_x = keys[pygame.K_d] - keys[pygame.K_a]
        norm = (self.dir_x ** 2 + self.dir_y ** 2) ** 0.5
        if norm != 0:
            self.dir_x /= norm
            self.dir_y /= norm

        if not keys[pygame.K_SPACE]:
            cursor = pygame.mouse.get_pos()
            self.rotation = math.atan2((cursor[1] - self.y), (cursor[0] - self.x))

        if keys[pygame.K_LSHIFT]:
            self.setAcceleration(6000)
            self.setMaxSpeed(600)
        else:
            self.setAcceleration(3500)
            self.setMaxSpeed(350)

    def reactToCollision(self):
        self.vx *= -1
        self.vy *= -1

    def reactToRoundCollision(self, point):
        flipSurface = lineTangentToPoints(point, self.getPoint())
        flipSurface = shiftLineToPoint(flipSurface, point)
        self.reactToFlatCollision(flipSurface)

    def reactToFlatCollision(self, surface):
        self.vx, self.vy = bounceVector((self.vx, self.vy), surface[0], surface[1])
        self.x, self.y = movePointAwayFromSurface(self.getPoint(), surface, 4)

    def draw(self):
        """Draws the player and his mirror"""
        self.sprite.draw(self.x, self.y)
        self.mirror.draw()

    def getPosition(self):
        return self.x, self.y




