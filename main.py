import pygame as pg
from pygame.locals import *
import numpy as np
import sys


class py_calc:
    def __init__(self, master):
        super().__init__(master)

        self.master = master


def main():
    pg.init()
    screen = pg.display.set_mode((300, 340))  # Window generation
    screen.fill("gray")

    while 1:
        pg.display.set_caption("Sample")
        pg.display.update()

    # Event processing
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()


if __name__ == "__main__":
    main()