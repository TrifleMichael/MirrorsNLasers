import pygame
import sys
import time
from time import sleep

from src.AtomicObjects.Field import Field
from src.Level import LevelSimulationManager
from src.Settings import frameDuration, xResolution, yResolution
from src.Structures.StructureManager import StructureManager



def mainLoop():
    pygame.init()

    display = pygame.display.set_mode((xResolution, yResolution), 0, 32)

    level = LevelSimulationManager(display, Field(xResolution, yResolution), frameDuration)
    # structureManager = StructureManager(display, levelSimulationManager) # TODO: Add interpreting input

    level.addWall(500, 500, 100, 200)

    level.addColumn(xResolution-50, yResolution-50, 20)  # TESTING
    level.createLaser(10, 150, 150, 100, 100, 150)  # test

    while True:  # pygame tick for time coordination

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

        level.update(keys)

        level.levelVisualManager.draw()
        level.laserManager.draw()  # TODO: needs changing: check LaserManager.py

        pygame.display.update()

        sleep(max(frameDuration + startTime - time.time(), 0))


if __name__ == "__main__":
    mainLoop()
