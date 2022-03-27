import pygame


class RectangleSprite:
    def __init__(self, DISPLAY, width, height):
        self.DISPLAY = DISPLAY
        self.width = width
        self.height = height
        self.color = (0, 255, 0)

    def draw(self, x, y):
        pygame.draw.rect(self.DISPLAY, self.color, (x, y, self.width, self.height))