import pygame

from color import *

pygame.init()

window = pygame.display.set_mode((500, 500))

login_picture = pygame.image.load("images/login.png")

window.fill(Color.rand_color())
new_login = pygame.transform.scale(login_picture, (80, 80))
window.blit(new_login, (30, 10))


def draw_square(color, site):
    """
    绘制矩形
    :param color: 颜色
    :param site: 矩形大小和位置 例：（x, y, width, height）
    :return:
    """
    pygame.draw.rect(window, color, site)


draw_square(Color.green, (160, 150, 200, 30))
draw_square(Color.rand_color(), (160, 230, 200, 30))
draw_square(Color.rand_color(), (170, 340, 160, 30))


def font_module(str1, place, size):
    """
    绘制文本内容
    :param str1:内容
    :param place: 坐标
    :return:
    """
    font = pygame.font.SysFont("SimHei", size)
    text = font.render(str1, True, Color.rand_color())
    window.blit(text, place)


font_module("欢迎来到管理系统", (180, 20), 20)
font_module("账号：", (180, 160), 15)
font_module("密码：", (180, 240), 15)
font_module("登录", (230, 350), 15)


def enter_sys():
    enter_picture = pygame.image.load("images/enter.png")
    new_enter = pygame.transform.scale(enter_picture, (500, 500))
    window.blit(new_enter, (0, 0))
    font_module("登陆成功", (210, 250), 30)

    pygame.display.update()


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 170 <= event.pos[0] <= 330 and 340 <= event.pos[1] <= 370:
                print("登陆中...", event.pos)
                enter_sys()
