import pygame


class CircleSprite:
    def __init__(self, x, y, r, display):
        self.x = x
        self.y = y
        self.r = r
        self.color = (255, 0, 0)
        self.display = display

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.r)

    def update(self, x, y):
        self.x = x
        self.y = y
