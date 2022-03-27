import pygame


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class InertialObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.acc = 0.7
        self.slowing = 0.5
        self.maxV = 10

    def move(self, field, directions):
        if 0 < self.x + self.vx < field.width:
            self.x += self.vx
        else:
            self.vx = 0

        if 0 < self.y + self.vy < field.height:
            self.y += self.vy
        else:
            self.vy = 0

        if directions[0] and self.vy - self.acc > -self.maxV:
            self.vy -= self.acc
        if directions[1] and self.vx + self.acc < self.maxV:
            self.vx += self.acc
        if directions[2] and self.vy + self.acc < self.maxV:
            self.vy += self.acc
        if directions[3] and self.vx - self.acc > -self.maxV:
            self.vx -= self.acc

        if abs(self.vx) - self.slowing > 0:
            self.vx -= abs(self.vx) / self.vx * self.slowing
        else:
            self.vx = 0

        if abs(self.vy) - self.slowing > 0:
            self.vy -= abs(self.vy) / self.vy * self.slowing
        else:
            self.vy = 0


class NonInertialObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = 10

    def move(self, field, directions):
        if directions[0] and self.y - self.v > 0:
            self.y -= self.v
        if directions[1] and self.x + self.v < field.width:
            self.x += self.v
        if directions[2] and self.y + self.v < field.height:
            self.y += self.v
        if directions[3] and self.x - self.v > 0:
            self.x -= self.v


class Player(InertialObject):
    def __init__(self, x, y):
        InertialObject.__init__(self, x, y)
        self.sprite = CircleSprite(50)

    def readKeys(self, keys, field):
        directions = [keys[pygame.K_w], keys[pygame.K_d], keys[pygame.K_s], keys[pygame.K_a]]
        self.move(field, directions)

    def draw(self, DISPLAY):
        self.sprite.draw(DISPLAY, self.x, self.y)


class CircleSprite:
    def __init__(self, r):
        self.r = r
        self.color = (255, 0, 0)

    def draw(self, DISPLAY, x, y):
        pygame.draw.circle(DISPLAY, self.color, (x, y), self.r)


class RectangleSprite:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (0, 255, 0)

    def draw(self, DISPLAY, x, y):
        pygame.draw.rect(DISPLAY, self.color, (x, y, self.width, self.height))
