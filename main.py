import pygame as pg
from pygame.locals import *
import numpy as np
import sys

WIDTH = 300
HEIGHT = 340


class pg_calc:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Sample")
        screen = pg.display.set_mode((WIDTH, HEIGHT))

        running = True
        while running:
            self.update()
            self.draw(screen)
            pg.display.update()
            self.hundler()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill("gray")

    def hundler(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()


if __name__ == "__main__":
    pg_calc()