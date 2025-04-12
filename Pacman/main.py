import pygame as pg

from config import (
    BLACK,
    FPS,
    TILEMAP,
    TILEMAP_2,
    TILEMAP_3,
    TILEMAP_4,
    TILEMAP_5,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from sprites import Blinky, Block, Clyde, Dot, Inky, Pinky, Player, Spritesheet


class Game:
    def __init__(self):
        # initialize game window, get sprite images, etc
        pg.init()
        pg.display.set_caption("Pacman")
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

        self.pacman_spritesheet = Spritesheet("assets/sprites/pac_sprites.png")
        self.terrain_spritesheet = Spritesheet("assets/sprites/pac_wall.jpg")
        self.ghost_spritesheet = Spritesheet("assets/sprites/pac_sprites.png")
        self.dot_spritesheet = Spritesheet("assets/sprites/dots.jpg")
        self.num_dots = 0
        self.level = 1
        pg.mixer.music.load("assets/sound/PacManMusic.mp3")
        pg.mixer.music.play(-1)

    def new(self):
        # New game creating the map and sprites
        self.playing = True
        self.num_dots = 0

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.pacman = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.ghosts = pg.sprite.LayeredUpdates()
        self.dots = pg.sprite.LayeredUpdates()

        self.create_tilemap()

    def events(self):
        # gets key presses
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def create_tilemap(self):
        # displays the tiles according to the map written in the config file
        hash = {1: TILEMAP, 2: TILEMAP_2, 3: TILEMAP_3, 4: TILEMAP_4, 5: TILEMAP_5}
        for i, row in enumerate(hash[self.level]):
            for j, col in enumerate(row):
                if col == "W":
                    Block(self, j, i)
                elif col == "U":
                    Player(self, j, i)
                elif col == "I":
                    Inky(self, j, i)
                elif col == "P":
                    Pinky(self, j, i)
                elif col == "B":
                    Blinky(self, j, i)
                elif col == "C":
                    Clyde(self, j, i)
                elif col == ".":
                    self.num_dots += 1
                    Dot(self, j, i)

    def check_dots(self):
        # Checks if all the dots are eaten and if so, creates a new level
        if self.num_dots == 0:
            self.level += 1
            if self.level <= 5:
                self.new()
            else:
                self.running = False
                exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        # Draw / render
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


if __name__ == "__main__":
    game = Game()
    game.new()
    while game.running:
        game.main()

    pg.quit()
    exit()
