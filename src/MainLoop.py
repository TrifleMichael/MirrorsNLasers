import pygame
import sys
import time
from time import sleep

from src.Level import LevelSimulationManager
from src.Settings import frameDuration, xResolution, yResolution


def mainLoop():
    pygame.init()

    display = pygame.display.set_mode((xResolution, yResolution), 0, 32)
    level = LevelSimulationManager(display, xResolution, yResolution)

    while True:
        startTime = time.time()

        keys = pygame.key.get_pressed()
        if pygame.QUIT in [event.type for event in pygame.event.get()] or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        display.fill((0, 0, 0))
        level.update(keys)
        level.levelVisualManager.draw()
        pygame.display.update()

        sleep(max(frameDuration + startTime - time.time(), 0))



mainLoop()