import pygame

from src.Sprites.RectangleSprite import RectangleSprite
from src import display, xResolution, yResolution


class Banner:
    def __init__(self, text):
        self.font = pygame.font.SysFont("monospace", 40)

        self.text = self.font.render(text, True, (255,255,255))
        self.textRect = self.text.get_rect()
        self.textRect.center = ((xResolution / 2), (yResolution / 2))

        self.bg = RectangleSprite(xResolution//2, yResolution//3, color=(0,0,139))


    def draw(self):
        self.bg.draw(xResolution//4, yResolution//3)
        display.blit(self.text, self.textRect)