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

        self.pacman_spritesheet = Spritesheet('assets/sprites/pac_sprites.png')
        self.terrain_spritesheet = Spritesheet('assets/sprites/pac_wall.jpg')
        self.ghost_spritesheet = Spritesheet('assets/sprites/pac_sprites.png')
        self.dot_spritesheet = Spritesheet('assets/sprites/dots.jpg')
        self.num_dots = 0
        music = pg.mixer.music.load('assets/sound/PacManMusic.mp3')
        pg.mixer.music.play(-1)


    def new(self):
        self.playing = True

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.pacman = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.ghosts = pg.sprite.LayeredUpdates()
        self.dots = pg.sprite.LayeredUpdates()

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
                elif col == 'U':
                    Player(self, j, i)
                elif col == 'I':
                    Inky(self, j, i)
                elif col == 'P':
                    Pinky(self, j, i)
                elif col == 'B':
                    Blinky(self, j, i)
                elif col == 'C':
                    Clyde(self, j, i)
                elif col == '.':
                    self.num_dots+=1
                    Dot(self, j, i)
    
    def check_dots(self):
        if self.num_dots == 0:
            self.playing = False
            self.running = False

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
            self.check_dots()
            self.draw()



if __name__ == '__main__':
    game = Game()
    game.new()
    while game.running:
        game.main()

    pg.quit()
    exit()