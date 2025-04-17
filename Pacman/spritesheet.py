import pygame as pg
from config import BLACK


class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite
