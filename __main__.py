import pygame
import sys
import time
from time import sleep

from src.GuidedMovementModels.BasicEnemy import BasicEnemy
from src.Enums import ScreenCorner
from src.LevelBuilder import LevelBuilder
from src.Settings import frameDuration

from src.Gui.gui import Gui
from src.Gui.Banner import Banner


def mainLoop():
    level_files = ['lvls/3.json', 'lvls/1.json', 'lvls/2.json']
    lvl_number = 0
    level = None

    startBanner = Banner("Press space to start")
    deadBanner = Banner("You died!")
    winBanner = Banner("You won!")

    startBanner.draw()
    pygame.display.update()
    await_space()

    while True:
        if level and level.player.win:
            lvl_number += 1
        level = LevelBuilder().build(level_files[lvl_number])
        gui = Gui(150, 50, ScreenCorner.TOP_LEFT)

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

            if level.player.win or not level.player.alive:
                if keys[pygame.K_SPACE]:
                    break
                level.update(keys=None)
            else:
                level.update(keys)
            level.draw()
            gui.update(f"Lvl: {lvl_number+1} HP: {level.player.hp}")
            gui.draw()
            if level.player.win:
                winBanner.draw()
            if not level.player.alive:
                deadBanner.draw()

            pygame.display.update()

            sleep(max(frameDuration + startTime - time.time(), 0))


def await_space():
    while True:
        keys = pygame.key.get_pressed()
        if pygame.QUIT in [event.type for event in pygame.event.get()] or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_SPACE]:
            return True
        sleep(frameDuration)


if __name__ == "__main__":
    mainLoop()


