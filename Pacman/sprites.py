import math
import random
import time
from abc import ABC

import pygame as pg

from config import (
    BLACK,
    BLOCK_LAYER,
    DOT_LAYER,
    GHOST_LAYER,
    PLAYER_LAYER,
    SPEED,
    TILESIZE,
    TM_X,
    TM_Y,
    WALLS,
    WALLS_2,
    WALLS_3,
    WALLS_4,
    WALLS_5,
)
from node import Node


class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Object(pg.sprite.Sprite, ABC):
    def __init__(self, game, layer, game_group, x, y):
        self.game = game
        self._layer = layer
        self.groups = self.game.all_sprites, game_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE


class Player(Object):
    def __init__(self, game, x, y):
        super().__init__(game, PLAYER_LAYER, game.pacman, x, y)
        # we want the players dimension to be slightly smaller so
        # that it can fit in the blocks easier

        self.width -= 2
        self.height -= 2

        self.image = self.game.pacman_spritesheet.get_sprite(
            0, 0, self.width, self.height
        )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = "right"
        self.frame = 0

        self.x_change = 0
        self.y_change = 0

        self.left = [
            self.game.pacman_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(
                32 * 2, 32, self.width, self.height
            ),
            self.game.pacman_spritesheet.get_sprite(
                32 * 3, 32, self.width, self.height
            ),
            self.game.pacman_spritesheet.get_sprite(
                32 * 2, 32, self.width, self.height
            ),
        ]

        self.right = [
            self.game.pacman_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(32, 32, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(0, 32, self.width, self.height),
        ]

        self.down = [
            self.game.pacman_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(
                32 * 2, 64, self.width, self.height
            ),
            self.game.pacman_spritesheet.get_sprite(
                32 * 3, 64, self.width, self.height
            ),
            self.game.pacman_spritesheet.get_sprite(
                32 * 2, 64, self.width, self.height
            ),
        ]

        self.up = [
            self.game.pacman_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(32, 64, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(0, 64, self.width, self.height),
        ]

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.y += self.y_change
        self.collide_blocks("y")
        self.rect.x += self.x_change
        self.collide_blocks("x")

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x_change -= SPEED
            self.facing = "left"
        if keys[pg.K_RIGHT]:
            self.x_change += SPEED
            self.facing = "right"
        if keys[pg.K_UP]:
            self.y_change -= SPEED
            self.facing = "up"
        if keys[pg.K_DOWN]:
            self.y_change += SPEED
            self.facing = "down"

    def collide_blocks(self, direction):
        hits = pg.sprite.spritecollide(self, self.game.blocks, False)
        if direction == "y":
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
        if direction == "x":
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

    def collide_enemy(self):
        hits = pg.sprite.spritecollide(self, self.game.ghosts, False)
        if hits:
            pg.mixer.music.stop()
            pg.mixer.init()
            sound = pg.mixer.Sound("assets/sound/PacManDeath.mp3")
            sound.play()
            self.death_animation()
            time.sleep(1)
            self.game.playing = False
            self.game.running = False

    def death_image(self):
        death_image = self.game.pacman_spritesheet.get_sprite(
            225, 0, self.width, self.height
        )
        black_image = self.game.pacman_spritesheet.get_sprite(
            213, 235, self.width, self.height
        )
        self.image = death_image
        time.sleep(0.25)
        self.game.draw()
        self.image = black_image
        self.game.draw()
        time.sleep(0.25)

    def death_animation(self):
        self.left = [
            self.game.pacman_spritesheet.get_sprite(174, 36, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(174, 78, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(174, 122, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(174, 168, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(174, 200, self.width, self.height),
        ]

        self.right = [
            self.game.pacman_spritesheet.get_sprite(132, 36, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(132, 78, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(132, 122, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(132, 168, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(132, 200, self.width, self.height),
        ]

        self.up = [
            self.game.pacman_spritesheet.get_sprite(162, 264, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(118, 264, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(72, 264, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(30, 264, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(0, 264, self.width, self.height),
        ]

        self.down = [
            self.game.pacman_spritesheet.get_sprite(182, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(142, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(98, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(60, 0, self.width, self.height),
            self.game.pacman_spritesheet.get_sprite(31, 0, self.width, self.height),
        ]

        if self.facing == "left":
            for i in range(5):
                self.image = self.left[i]
                time.sleep(0.25)
                self.game.draw()
            self.death_image()

        if self.facing == "right":
            for i in range(5):
                self.image = self.right[i]
                time.sleep(0.25)
                self.game.draw()
            self.death_image()

        if self.facing == "up":
            for i in range(5):
                self.image = self.up[i]
                time.sleep(0.25)
                self.game.draw()
            self.death_image()

        if self.facing == "down":
            for i in range(5):
                self.image = self.down[i]
                time.sleep(0.25)
                self.game.draw()
            self.death_image()

    def animate(self):
        if self.facing == "left":
            self.image = self.left[math.floor(self.frame)]
            self.frame += 0.2
            if self.frame > 3.6:
                self.frame = 0

        if self.facing == "right":
            self.image = self.right[math.floor(self.frame)]
            self.frame += 0.2
            if self.frame > 3.6:
                self.frame = 0

        if self.facing == "up":
            self.image = self.up[math.floor(self.frame)]
            self.frame += 0.2
            if self.frame > 3.6:
                self.frame = 0

        if self.facing == "down":
            self.image = self.down[math.floor(self.frame)]
            self.frame += 0.2
            if self.frame > 3.6:
                self.frame = 0


class Ghost(Object):
    def __init__(self, game, x, y, image_x, image_y, coords, ghost_letter):
        super().__init__(game, GHOST_LAYER, game.ghosts, x, y)
        self.image_x = image_x
        self.image_y = image_y
        self.image = self.game.ghost_spritesheet.get_sprite(
            self.image_x, self.image_y, self.width, self.height
        )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.x_change = 0
        self.y_change = 0
        self.facing = "right"
        self.move_loop = 0
        self.frame = 1
        self.path = []
        self.goal = (0, 0)
        self.start = True
        self.map = []
        # in this case, more mass means the ghosts are slower
        self.mass = 15
        self.coords = coords
        self.ghost_letter = ghost_letter

    def update(self):
        self.animate()
        # self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def valid(self, x, y):
        if (
            x >= 0
            and x <= TM_X - 1
            and y >= 0
            and y <= TM_Y - 1
            and self.map[x][y] != "W"
        ):
            return True
        return False

    def change_face(self, x, y):
        if x < self.coords[0]:
            self.facing = "left"
        elif x > self.coords[0]:
            self.facing = "right"
        elif y < self.coords[1]:
            self.facing = "up"
        elif y > self.coords[1]:
            self.facing = "down"

    def bfs(self, letter):
        x = 0
        y = 0
        while True:
            x = random.randrange(TM_X)
            y = random.randrange(TM_Y)

            if self.map[x][y] == ".":
                self.map[x][y] = "X"
                self.goal = (x, y)
                break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cur_x, cur_y = -1, -1
        tar_x, tar_y = -1, -1
        for i in range(TM_X):
            for j in range(TM_Y):
                if self.map[j][i] == letter:
                    cur_x, cur_y = i, j
                if self.map[j][i] == "X":
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
                if (
                    self.map[x + d[0]][y + d[1]] != "W"
                    and [x + d[0], y + d[1]] not in visited
                ):
                    n = Node(x + d[0], y + d[1], cur_node)
                    visited.append([x + d[0], y + d[1]])
                    queue.append(n)

    def movement(self, letter):
        level = self.game.level
        level_hash = {1: WALLS, 2: WALLS_2, 3: WALLS_3, 4: WALLS_4, 5: WALLS_5}
        if not self.path:
            self.map.clear()
            for row in level_hash[level][:]:
                self.map.append(list(row))
            self.map[self.coords[0]][self.coords[1]] = letter
            self.path = self.bfs(letter)

        if self.frame % self.mass == 0:
            y, x = self.path.pop()
            self.x = x * TILESIZE
            self.y = y * TILESIZE
            self.change_face(x, y)
            self.rect.x = self.x
            self.rect.y = self.y
            self.coords = (x, y)
            self.map[x][y] = letter
        self.frame += 1

    def animate(self):
        if self.facing == "right":
            self.image = self.game.ghost_spritesheet.get_sprite(
                self.image_x, self.image_y, self.width, self.height
            )

        if self.facing == "left":
            self.image = self.game.ghost_spritesheet.get_sprite(
                self.image_x + 32, self.image_y, self.width, self.height
            )

        if self.facing == "down":
            self.image = self.game.ghost_spritesheet.get_sprite(
                self.image_x + 64, self.image_y, self.width, self.height
            )

        if self.facing == "up":
            self.image = self.game.ghost_spritesheet.get_sprite(
                self.image_x + 96, self.image_y, self.width, self.height
            )

        self.movement(self.ghost_letter)


class Block(Object):
    def __init__(self, game, x, y):
        super().__init__(game, BLOCK_LAYER, game.blocks, x, y)
        self.image = self.game.terrain_spritesheet.get_sprite(
            0, 0, self.width, self.height
        )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.value = 1


class Dot(Object):
    def __init__(self, game, x, y):
        super().__init__(game, DOT_LAYER, game.dots, x, y)
        self.image = self.game.dot_spritesheet.get_sprite(
            32, 0, self.width, self.height
        )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.visible = True

    def update(self):
        hits = pg.sprite.spritecollide(self, self.game.pacman, False)
        if hits and self.visible is True:
            self.visible = False
            self.image = self.game.dot_spritesheet.get_sprite(0, 0, 1, 1)
            self.game.num_dots -= 1
