import pygame
import sys
import time
from time import sleep

from src.Objects import *
from src.Settings import *

frameTime = frameDuration
windowX = xResolution
windowY = yResolution

def mainLoop():
    pygame.init()

    DISPLAY = pygame.display.set_mode((windowX, windowY), 0, 32)
    FIELD = Field(windowX, windowY)
    PLAYER = Player(300, 300)

    while True:
        startTime = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        PLAYER.readKeys(keys, FIELD)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        DISPLAY.fill((0, 0, 0))
        PLAYER.draw(DISPLAY)
        pygame.display.update()

        endTime = startTime + frameTime
        while time.time() < endTime:
            sleep(0.001)

