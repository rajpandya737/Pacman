# Node class to be recursively used in the BFS algorithm
class Node:
    def __init__(self, x, y, prev=0):
        self.x = x
        self.y = y
        self.prev = prev

    def get_coords(self):
        return [self.x, self.y]

    def get_prev(self):
        return self.prev
