# Node class to be recursively used in the BFS algorithm
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    x: int
    y: int
    prev: Optional["Node"] = None  # Forward reference in quotes

    def get_coords(self) -> list[int]:
        return [self.x, self.y]

    def get_prev(self) -> Optional["Node"]:
        return self.prev
