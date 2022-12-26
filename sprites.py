import pygame as pg
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x,y,width,height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.facing = 'right'

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.character_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.frame = 0
        

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.rect.x += self.x_change
        self.collide_blocks('x')

        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x_change -=SPEED
            self.facing = 'left'
        elif keys[pg.K_RIGHT]:
            self.x_change+=SPEED
            self.facing = 'right'
        elif keys[pg.K_UP]:
            self.y_change-=SPEED
            self.facing = 'up'
        elif keys[pg.K_DOWN]:
            self.y_change+=SPEED
            self.facing = 'down'




    def collide_blocks(self, direction):
        
        hits = pg.sprite.spritecollide(self, self.game.blocks, False)
        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

    def collide_enemy(self):
        hits = pg.sprite.spritecollide(self, self.game.ghosts, False)
        if hits:
            #maybe game over screen in future
            self.game.playing = False
            self.game.running = False




    def animate(self):
        left = [self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(32*2,32, self.width, self.height),
                    self.game.character_spritesheet.get_sprite(32*3,32, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(32*2,32, self.width, self.height) ]

        right = [self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(0,32, self.width, self.height),
                    self.game.character_spritesheet.get_sprite(32,32, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(0,32, self.width, self.height) ]

        down = [self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(32*2,64, self.width, self.height),
                    self.game.character_spritesheet.get_sprite(32*3,64, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(32*2,64, self.width, self.height) ]

        up = [self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(0,64, self.width, self.height),
                    self.game.character_spritesheet.get_sprite(32,64, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(0,64, self.width, self.height) ]



        if self.facing == 'left':
            self.image = left[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0


        if self.facing == 'right':
            self.image = right[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0


        if self.facing == 'up':
            self.image = up[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0


        if self.facing == 'down':
            self.image = down[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0

class Ghost(pg.sprite.Sprite):
    def __init__(self):
        self._layer = GHOST_LAYER
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = 'up'
        self.move_loop = 0

    def update(self):
        self.rect.x+=self.x_change
        self.rect.y+=self.y_change
        self.x_change = 0
        self.y_change = 0
    

class Blinky(Ghost):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.groups = self.game.all_sprites, self.game.ghosts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = self.game.ghost_spritesheet.get_sprite(0,96, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,96, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,96, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,96, self.width, self.height)
            
        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,96, self.width, self.height)


class Inky(Ghost):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.groups = self.game.all_sprites, self.game.ghosts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = self.game.ghost_spritesheet.get_sprite(0,128, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,128, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,128, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,128, self.width, self.height)
            
        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,128, self.width, self.height)

class Clyde(Ghost):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.groups = self.game.all_sprites, self.game.ghosts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = self.game.ghost_spritesheet.get_sprite(0,160, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,160, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,160, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,160, self.width, self.height)

        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,160, self.width, self.height)




class Pinky(Ghost):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.groups = self.game.all_sprites, self.game.ghosts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = self.game.ghost_spritesheet.get_sprite(0,192, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,192, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,192, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,192, self.width, self.height)

        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,192, self.width, self.height)





class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.terrain_spritesheet.get_sprite(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y




class Dot(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = DOT_LAYER
        self.groups = self.game.all_sprites, self.game.dots
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.dot_spritesheet.get_sprite(32,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    





