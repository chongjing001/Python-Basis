
import pygame
from plane_tools import *


class PlaneGame:


    def __init__(self):
        print("游戏初始化...")
        self.window = pygame.display.set_mode(SCREEN_RECT.size)

        # 创建游戏时钟
        self.clock = pygame.time.Clock()


        self.creat_sprites()

        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)





    def creat_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建主角飞机的精灵和精灵组
        self.hero = MyPlane()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.enemy_group = pygame.sprite.Group()





    def event_judge(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if 30 <= event.pos[0] <= 459 and 300 <= event.pos[1] <= 384:
                    pass

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            elif event.type == ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)


        # 2.使用键盘模块--按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断按键索引值
        if keys_pressed[pygame.K_d]:
            print("向右移动...")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_a]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_w]:
            self.hero.speed1 = -3
        elif keys_pressed[pygame.K_s]:
            self.hero.speed1 = 2

        else:
            self.hero.speed = 0


    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group,True,True)
        # 敌机撞毁英雄机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        # 判断列表是否有内容
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()


    def update_tools(self):
        self.back_group.update()
        self.back_group.draw(self.window)

        self.hero_group.update()
        self.hero_group.draw(self.window)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.window)

        self.enemy_group.update()
        self.enemy_group.draw(self.window)



    def start_game(self):
        while True:
            print("游戏开始...")
            self.clock.tick(FRAME_PER_SEC)
            GameShow()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    while True:
                        self.clock.tick(FRAME_PER_SEC)

                        self.event_judge()

                        self.__check_collide()

                        self.update_tools()

                        pygame.display.update()


    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
































if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
