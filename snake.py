import time
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class SnakeBody:
    def __init__(self, x, y, direction=Direction.RIGHT):
        self.x = x
        self.y = y
        self.direction = direction



class Canvas:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snakes = [Snake()]

class Snake:
    def __init__(self):
        self.body = [SnakeBody(5, 5)]



