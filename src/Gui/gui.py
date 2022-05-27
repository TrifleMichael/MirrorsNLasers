import pygame

from src.Sprites.RectangleSprite import RectangleSprite
from src.Enums import ScreenCorner
from src import display


class Gui:
    def __init__(self, width, height, corner: ScreenCorner):
        self.bg = RectangleSprite(width, height, color=(70, 30, 40))
        self.x, self.y = corner.point()
        self.x -= width if not corner.isLeft() else 0
        self.y -= height if not corner.isTop() else 0

        self.font = pygame.font.SysFont("monospace", int(height * 0.8))
        self.msg_text = "msg"
        self.msg = self.font.render(self.msg_text, True, (255, 255, 255))

    def update(self, msg_text):
        if msg_text != self.msg_text:
            self.msg_text = msg_text
            self.msg = self.font.render(self.msg_text, True, (255, 255, 255))

    def draw(self):
        self.bg.draw(self.x, self.y)
        display.blit(self.msg, (self.x + 10, self.y))