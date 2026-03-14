import time
from enum import Enum
import sys
import os

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



class AbsctractRender:
    def __init__(self, element):
        self.element = element
    


    def move_cursor(self, row, col):
        sys.stdout.write(f"\033[{row};{col}H")


    def render(self):
        pass

class RenderCanvas(AbsctractRender):
    def render(self):
        os.system("cls")





 
        self.move_cursor(1, 0)
        print("#"*(self.element.width + 2))



        self.move_cursor(self.element.height + 2, 0)
        print("#"*(self.element.width + 2))



        for i in range(self.element.height + 2):
            self.move_cursor(i, 0)
            print("#")
            self.move_cursor(i, self.element.width + 2)
            print("#")

        



        self.move_cursor(self.element.height + 5, 0)

        


            


if __name__ == "__main__":
    

    canvas1 = Canvas(2,4)
    renderer = RenderCanvas(canvas1)

    renderer.render()

