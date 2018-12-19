import pygame
from plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480,700))


bg = pygame.image.load("./images/background.png")

screen.blit(bg,(0,0))


# 绘制主角飞机
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(180,520))
pygame.display.update()


clock = pygame.time.Clock()

hero_rect = pygame.Rect(180,520,100,124)

# 创建敌机的精灵
enemy0 = GameSprite("./images/enemy0.png")
enemy1 = GameSprite("./images/enemy0.png",2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy0,enemy1)


while True:

    clock.tick(60)
    # 捕获事件
    for event in pygame.event.get():
        print(event)
        # 判断事件类型是否为退出
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            # 卸载所以模块
            pygame.quit()

            exit()

    hero_rect.y -= 1

    if hero_rect.y <= -124:
        hero_rect.y = 700

    screen.blit(bg,(0,0))  # 覆盖飞机
    screen.blit(hero,hero_rect)

    # 让精灵组调用两个方法
    # 1.update  让组中所有精灵更新位置
    enemy_group.update()

    # 2.draw  在screen上绘制所有精灵
    enemy_group.draw(screen)




    # 4.更新显示
    pygame.display.update()



pygame.quit()
