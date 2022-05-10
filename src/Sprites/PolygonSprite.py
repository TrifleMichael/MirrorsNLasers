import pygame.draw


class PolygonSprite:
    def __init__(self, display, segmentList, color):
        self.segmentList = segmentList
        self.display = display
        self.color = color

    def draw(self):
        pygame.draw.polygon(self.display, self.color, self.segmentList)