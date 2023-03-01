#Node used for bfs search for the ghosts
class Node:
    def __init__(self, x, y, prev=0):
        self.x = x
        self.y = y
        self.prev = prev
    def get_coords(self):
        return [self.x, self.y]
    def get_prev(self):
        return self.prev