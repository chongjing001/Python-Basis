import pygame
from color import *

pygame.init()
window = pygame.display.set_mode((480, 600))

window.fill((255, 255, 255))

"""
画直线

"""

pygame.draw.line(window, Color.yellow, (0, 0), (400, 600), 10)

points = [(10, 10), (50, 60), (50, 150), (300, 150), (500, 700)]
pygame.draw.lines(window, Color.blue, False, points)

"""
画圆
circle(画在哪儿，颜色，圆心坐标，半径)
"""

pygame.draw.circle(window, Color.rand_color(), (200, 200), 80, 1)

"""
画弧线

"""

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


