import random
import pygame

# 设置一个屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 800)
# 设置帧率常量
FRAME_PER_SEC = 60
# 创建敌机定时器常量
ENEMY_EVENT = pygame.USEREVENT
# 发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战的游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化的方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 垂直移动
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        # 1.调用父类的方法实现精灵的创建
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，如果是则需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法实现
        super().update()
        # 判断背景位置
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
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



class Hero(GameSprite):
    """主角飞机"""

    def __init__(self):
        super().__init__("./images/hero1.png", 0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 30
        # 子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        # 设置英雄水平移动速度
        self.rect.x += self.speed
        # 控制英雄移动区域
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):
        for i in range(0, 3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet.png", -4)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
