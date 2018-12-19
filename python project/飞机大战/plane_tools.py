
import random
import pygame
from color import *

# 设置一个屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 设置帧率常量
FRAME_PER_SEC = 60

ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneSprite(pygame.sprite.Sprite):
    """ """
    def __init__(self, image_name, speed=1, speed1=0):

        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed1 = speed1

    def update(self):
        self.rect.y += self.speed


class Background(PlaneSprite):

    def __init__(self, is_alt=False):
        super().__init__("images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Score(PlaneSprite):
    # def __init__(self, window):
    #     pygame.init()
    #     self.font = pygame.font.SysFont("SimHei", 50)
    #     self.text = self.font.render("分数：", True, Color.yellow)
    #     window.blit(self.text, (0, 0))
    pass

class MyPlane(PlaneSprite):

    def __init__(self):
        super().__init__("images/hero1.png", 0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 80
        # 子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        # 设置英雄水平移动速度
        self.rect.x += self.speed
        # y
        self.rect.y += self.speed1
        # 控制英雄移动区域
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):
        for i in range(0, 3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)



class Bullet(PlaneSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet.png", -4)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()



class Enemy(PlaneSprite):
    """敌机"""

    def __init__(self):
        # 1.调用父类方法创建敌机精灵  并添加图片
        super().__init__("./images/enemy0.png")
        # 2.指定敌机初始随机速度
        self.speed = random.randint(1, 3)
        # 3.初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类，保持垂直飞行
        super().update()
        # 2.判断是否飞出屏幕，是则从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机已自毁")
            # kill方法可以将精灵从精灵组中移除
            self.kill()

    def __del__(self):
        print("坐标 %s" % self.rect)


class GameShow:

    def __init__(self):
        self.window = pygame.display.set_mode(SCREEN_RECT.size)
        self.loading = pygame.image.load("images/loading.png")
        self.name = pygame.image.load("images/name.png")
        self.window.blit(self.loading, (20, 100))
        # self.window.fill((255, 255, 255))
        self.window.blit(self.name, (20, 230))
        pygame.display.update()










