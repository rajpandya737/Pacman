import pygame as pg
from config import *
import math
import random
from node import *


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

        self.groups = self.game.all_sprites, self.game.pacman
        pg.sprite.Sprite.__init__(self, self.groups)

        #self.groups = self.game.all_sprites
        #pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE-2
        self.height = TILESIZE-2
        self.facing = 'right'
        self.frame = 0

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.pacman_spritesheet.get_sprite(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        
        self.left = [self.game.pacman_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(32*2,32, self.width, self.height),
                    self.game.pacman_spritesheet.get_sprite(32*3,32, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(32*2,32, self.width, self.height) ]

        self.right = [self.game.pacman_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(0,32, self.width, self.height),
                    self.game.pacman_spritesheet.get_sprite(32,32, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(0,32, self.width, self.height) ]

        self.down = [self.game.pacman_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(32*2,64, self.width, self.height),
                    self.game.pacman_spritesheet.get_sprite(32*3,64, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(32*2,64, self.width, self.height) ]

        self.up = [self.game.pacman_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(0,64, self.width, self.height),
                    self.game.pacman_spritesheet.get_sprite(32,64, self.width, self.height), 
                    self.game.pacman_spritesheet.get_sprite(0,64, self.width, self.height) ]

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
        if keys[pg.K_RIGHT]:
            self.x_change+=SPEED
            self.facing = 'right'
        if keys[pg.K_UP]:
            self.y_change-=SPEED
            self.facing = 'up'
        if keys[pg.K_DOWN]:
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

        if self.facing == 'left':
            self.image = self.left[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0

        if self.facing == 'right':
            self.image = self.right[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0

        if self.facing == 'up':
            self.image = self.up[math.floor(self.frame)]
            self.frame+=0.2
            if self.frame > 3.6:
                self.frame = 0

        if self.facing == 'down':
            self.image = self.down[math.floor(self.frame)]
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
        self.facing = 'right'
        self.move_loop = 0
        self.frame = 1
        self.path = []
        self.goal = (0,0)
        self.start = True
        self.map = []
        #in this case, more mass means the ghosts are slower
        self.mass = 15

    def update(self):
        self.animate()
        #self.movement()
        self.rect.x+=self.x_change
        self.rect.y+=self.y_change
        self.x_change = 0
        self.y_change = 0
    
    def valid(self, x, y):
        if x >=0 and x <=TM_X-1 and y >=0 and y <= TM_Y-1 and self.map[x][y] !='W':
            return True
        return False
        
    def change_face(self, x, y):
        if x < self.coords[0]:
            self.facing = 'left'
        elif x > self.coords[0]:
            self.facing = 'right'
        elif y < self.coords[1]:
            self.facing = 'up'
        elif y > self.coords[1]:
            self.facing = 'down'
    
    def bfs(self, letter):
        x = 0
        y = 0
        while True:
            x = random.randrange(TM_X)
            y = random.randrange(TM_Y)

            if self.map[x][y] == '.':
                self.map[x][y] = 'X'
                self.goal = (x,y)
                break

        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        cur_x, cur_y = -1, -1
        tar_x, tar_y = -1, -1
        for i in range(TM_X):
            for j in range(TM_Y):
                if self.map[j][i] == letter:
                    cur_x, cur_y = i, j
                if self.map[j] [i] == 'X':
                    tar_x, tar_y = i, j
        start = Node(cur_x, cur_y, 0)
        visited = [[cur_x, cur_y]]
        queue = [start]
        while queue:
            cur_node = queue.pop(0)
            x, y = cur_node.get_coords()
            if x == tar_x and y == tar_y:
                path = []
                while True:
                    path.append(cur_node.get_coords())
                    cur_node = cur_node.get_prev()
                    if cur_node == 0:
                        return path
            for d in directions:
                if self.map[x+d[0]][y+d[1]] !='W' and [x+d[0], y+d[1]] not in visited:
                    n = Node(x+d[0], y+d[1], cur_node)
                    visited.append([x+d[0], y+d[1]])
                    queue.append(n)

    def movement(self, letter):
        if not self.path:
            self.map.clear()
            for row in WALLS[:]:
                self.map.append(list(row))
            self.map[self.coords[0]][self.coords[1]] = letter
            self.path = self.bfs(letter)
        
        if self.frame % self.mass == 0:
            y,x = self.path.pop()
            #print(x,y)
            self.x = x * TILESIZE
            self.y = y * TILESIZE
            self.change_face(x,y)
            self.rect.x = self.x
            self.rect.y = self.y
            self.coords = (x,y)
            self.map[x][y] = letter
        self.frame+=1



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
        self.coords = (8,9)


    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,96, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,96, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,96, self.width, self.height)
            
        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,96, self.width, self.height)
        
        self.movement('B')






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
        self.coords = (6,9)


    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,128, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,128, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,128, self.width, self.height)
            
        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,128, self.width, self.height)
        
        self.movement('I')

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
        self.coords = (12,9)


    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,160, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,160, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,160, self.width, self.height)

        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,160, self.width, self.height)
        self.movement('C')



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
        self.coords = (10, 9)



    def animate(self):
        if self.facing == 'right':
            self.image = self.game.ghost_spritesheet.get_sprite(0,192, self.width, self.height)

        if self.facing == 'left':
            self.image = self.game.ghost_spritesheet.get_sprite(32,192, self.width, self.height)

        if self.facing == 'down':
            self.image = self.game.ghost_spritesheet.get_sprite(64,192, self.width, self.height)

        if self.facing == 'up':
            self.image = self.game.ghost_spritesheet.get_sprite(96,192, self.width, self.height)
        self.movement('P')


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
        self.value = 1




class Dot(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.visible = True
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
    
    def update(self):
        hits = pg.sprite.spritecollide(self, self.game.pacman, False)
        if hits and self.visible is True:
            self.visible = False
            self.image = self.game.dot_spritesheet.get_sprite(0,0, 1, 1)
            self.game.num_dots-=1










