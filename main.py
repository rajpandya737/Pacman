import pygame as pg
import numpy as np
from config import *
from sprites import *
import sys

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Pacman')
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.clock = pg.time.Clock()
        #self.font = pg.font.Font('Arial', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('assets/sprites/pac_sprites.png')
        self.terrain_spritesheet = Spritesheet('assets/sprites/pac_wall.jpg')
        self.ghost_spritesheet = Spritesheet('assets/sprites/pac_sprites.png')


    def new(self):
        self.playing = True

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.ghosts = pg.sprite.LayeredUpdates()
        #self.player = Player(self, 1, 2)
        self.createTilemap()
    
    def events(self):
        #gets key presses
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def createTilemap(self):
        #displays the tiles according to the map written in the config file
        for i , row in enumerate(TILEMAP):
            for j, col in enumerate(row):
                if col == 'W':
                    Block(self, j, i)
                if col == 'U':
                    Player(self, j, i)
                if col == 'I':
                    Inky(self, j, i)
                if col == 'P':
                    Pinky(self, j, i)
                if col == 'B':
                    Blinky(self, i, j)
                if col == 'C':
                    Clyde(self, i, j)
    
    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pg.display.update()


    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        


if __name__ == '__main__':
    game = Game()
    game.new()
    while game.running:
        game.main()

    pg.quit()
    exit()