import pygame


class LineSprite:
    def __init__(self, p1, p2, display, color=None):
        self.p1 = p1
        self.p2 = p2
        self.color = color or (255, 0, 255)
        self.display = display

    def draw(self):
        pygame.draw.line(self.display, self.color, self.p1, self.p2, 5)

    def update(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
