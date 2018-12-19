import pygame
from plane_sprites import *

class PlaneGame():
    """飞机大战主程序"""
    def __init__(self):


        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)


        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法创建精灵和精灵组
        self.__creat_sprites()

        # 设置定时器事件---创建敌机1毫秒
        pygame.time.set_timer(ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def __creat_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建主角飞机的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)




    def star_game(self):
        print("游戏开始。。。")
        while True:

            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.时间监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__updeta_sprites()
            # 5.更新显示
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ENEMY_EVENT:
                print("刷新敌机...")
                # 创建敌机
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # 1.使用事件监听控制移动
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
        # 2.使用键盘模块--按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断按键索引值
        if keys_pressed[pygame.K_d]:
            print("向右移动...")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_a]:
            self.hero.speed = -2
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


    def __updeta_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        #
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()




if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.star_game()