import pygame.draw


class MultiLineSprite:
    def __init__(self, pointList, display):
        self.pointList = pointList
        self.color = (255, 0, 255)
        self.display = display

    def draw(self):
        for i in range(len(self.pointList)-1):
            pygame.draw.line(self.display, self.color, (self.pointList[i][0], self.pointList[i][1]), (self.pointList[i+1][0], self.pointList[i+1][1]), 5)

    def update(self, pointList):
        self.pointList = pointList
