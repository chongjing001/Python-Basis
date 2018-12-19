import pygame

from color import *


window = pygame.display.set_mode((400, 280))
window1 = pygame.display.set_mode((500, 500))
fps = 60

class Login:
    def __init__(self):
        self.clock = pygame.time.Clock()
        bg = pygame.image.load("images/qq.png")

        enter = pygame.image.load("images/login.png")

    def layout(self):
        new_bg = pygame.transform.scale(self.bg, (400, 280))
        window.blit(new_bg, (0, 0))




    def font_module(self, str1, place, size):
        """
        绘制文本内容
        :param str1:内容
        :param place: 坐标
        :return:
        """
        font = pygame.font.SysFont("SimHei", size)
        text = font.render(str1, True, Color.rand_color())
        window.blit(text, place)

    def draw_square(self, window, color, site):
        """
        绘制矩形
        :param color: 颜色
        :param site: 矩形大小和位置 例：（x, y, width, height）
        :return:
        """
        pygame.draw.rect(window, color, site)


    @staticmethod
    def update():
        pygame.display.update()




if __name__ == '__main__':
    pygame.init()
    l1 = Login()
    while True:
        l1.clock.tick = fps
        l1.layout()
        Login.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if 170 <= event.pos[0] <= 330 and 340 <= event.pos[1] <= 370:
                        print("登陆中...", event.pos)





