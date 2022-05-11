import pygame
import sys
import time
from time import sleep

from src.LevelBuilder import LevelBuilder
from src.Settings import frameDuration, xResolution, yResolution


def mainLoop():
    level = LevelBuilder().getTestLevel()

    while True:
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
        level.draw()
        pygame.display.update()

        sleep(max(frameDuration + startTime - time.time(), 0))


if __name__ == "__main__":
    mainLoop()


