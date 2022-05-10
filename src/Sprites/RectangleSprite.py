import pygame


class RectangleSprite:
    def __init__(self, DISPLAY, width, height):
        self.DISPLAY = DISPLAY
        self.width = width
        self.height = height
        self.color = (0, 255, 255)
        self.x = None
        self.y = None

    def draw(self):
        pygame.draw.rect(self.DISPLAY, self.color, (self.x, self.y, self.width, self.height))

    def update(self, x, y):
        self.x = x
        self.y = y