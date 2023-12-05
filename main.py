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
            self.handler()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill("gray")

    def handler(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()


class Button:
    def __init__(self, x, y, w, h, text=""):
        self.image = pg.Surface(x, y)
        self.rect = pg.Rect(x, y, w, h)
        self.color = "white"
        self.text = text
        self.text_surface = font.reader(text, True, self.color)
        self.act = False

    def update(self):
        width = ...
        self.rect.w = width
        ...

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        ...


class txt_box:
    def __init__(self):
        pass


if __name__ == "__main__":
    pg_calc()