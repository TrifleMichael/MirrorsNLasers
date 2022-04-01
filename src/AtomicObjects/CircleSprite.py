import pygame


class CircleSprite:
    def __init__(self, r):
        self.r = r
        self.color = (255, 0, 0)

    def draw(self, DISPLAY, x, y):
        pygame.draw.circle(DISPLAY, self.color, (x, y), self.r)
