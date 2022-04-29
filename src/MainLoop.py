import random

import pygame
import sys
import time
from time import sleep

from src.AtomicObjects.Field import Field
from src.LaserUtility.Laser import Laser
from src.LaserUtility.LaserManager import LaserManager
from src.AtomicObjects.Mirror import Mirror
from src.Level import LevelSimulationManager
from src.Settings import frameDuration, xResolution, yResolution


def mainLoop():
    pygame.init()

    display = pygame.display.set_mode((xResolution, yResolution), 0, 32)
    level = LevelSimulationManager(display, Field(xResolution, yResolution))

    #level.addColumn(500, 300, 60)  # TESTING
    level.addColumn(700, 500, 20)
    #level.addColumn(800, 100, 30)
    #level.addColumn(700, 250, 30)

    laserManager = LaserManager(frameDuration, display)
    laserManager.createLaser(10, 150, 150, 100, 100, 150)  # test

    testLine = [(100, 100), (300, 50)]

    deb = 0
    while True:  # pygame tick for time coordination
        deb += 1
        if deb == 200:
            laserManager.laserList[0].reactToCollision(testLine) # INTENSIVE TESTING IN PROGRESS :)

        startTime = time.time()

        keys = pygame.key.get_pressed()
        if pygame.QUIT in [event.type for event in pygame.event.get()] or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if keys[pygame.K_p]: # makeshift pause
            while not keys[pygame.K_o]:
                keys = pygame.key.get_pressed()
                sleep(frameDuration)
                if pygame.QUIT in [event.type for event in pygame.event.get()] or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

        laserManager.move()
        level.update(keys)

        level.levelVisualManager.draw()
        laserManager.draw()  # needs changing: check LaserManager.py
        pygame.draw.line(display, (255, 255, 0), testLine[0], testLine[1], 10)  # test
        pygame.draw.circle(display, (255, 255, 0), (414, 414), 2)

        pygame.display.update()

        sleep(max(frameDuration + startTime - time.time(), 0))


if __name__ == "__main__":
    mainLoop()
