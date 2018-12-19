
from random import randint


class Color:
    white = (255,255,255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def rand_color():
        num = randint(0, 255)
        num2 = randint(0, 255)
        num3 = randint(0, 255)
        return (num, num2, num3)













