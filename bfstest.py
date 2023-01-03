
from collections import deque
import random

class Node:
    def __init__(self, x, y, prev=0):
        self.x = x
        self.y = y
        self.prev = prev
    def get_coords(self):
        return [self.x, self.y]
    def get_prev(self):
        return self.prev




def valid(map, x, y):
    global map_x
    global map_y
    if x >=0 and x <=map_x-1 and y >=0 and y <= map_y-1 and map[x][y] !='W':
        return True
    return False


map_x = 20
map_y = 20
new_map = [
'WWWWWWWWWWWWWWWWWWWW',
'W........W.........W',
'W.WW.WWW.W.WWWW.WW.W',
'W..................W',
'W.WW.W.WWWWW.W.WWW.W',
'W....W...W.........W',
'WWWW.WWW.W.WWWWWWWWW',
'WWWW...........WWWWW',
'WWWW.WWWW-WWWW.WWWWW',
'W....W....B..W.....W',
'W.WWWWWWWWWWWWWWWW.W',
'W.WWW..........WWW.W',
'W.....WWWWWWWW.....W',
'WWWWW..........WWWWW',
'W.....WWWWWWWW.....W',
'W.WWWW...W....WWWW.W',
'W.WWWW.W.W.WW.WWWW.W',
'W.WWWW.W.W.WW.WWWW.W',
'W..................W',
'WWWWWWWWWWWWWWWWWWWW'
]

map = []
for row in new_map:
    map.append(list(row))

while True:
        x = random.randrange(len(map[0]))
        y = random.randrange(len(map))
        new_map = []
        for row in map:
            new_map.append(list(row))

        if map[x][y] == '.':
            map[x][y] = 'X'
            break

directions = [(-1,0), (1,0), (0, -1), (0, 1)]
cur_x, cur_y = -1, -1
tar_x, tar_y = -1, -1
for i in range(map_x):
    for j in range(map_y):
        if map[i][j] == 'B':
            cur_x, cur_y = i, j
        if map[i] [j] == 'X':
            tar_x, tar_y = i, j
start = Node(cur_x, cur_y, 0)

visited = [start]
found = False
queue = [start]

print('time')

while queue:
    cur_node = queue.pop(0)
    x, y = cur_node.get_coords()
    if x == tar_x and y == tar_y:
        path = []
        while True:
            path.append(cur_node.get_coords())
            cur_node = cur_node.get_prev()
            if cur_node == 0:
                print(path)
                found = True
                break
    if found is True:
        break
    for d in directions:
        if valid(map, x+d[0], y+d[1]) and [x+d[0], y+d[1]] not in visited:
            n = Node(x+d[0], y+d[1], cur_node)
            visited.append([x+d[0], y+d[1]])
            queue.append(n)







