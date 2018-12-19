import pygame

pygame.init()

screen = pygame.display.set_mode((480,700))


bg = pygame.image.load("./images/background.png")

screen.blit(bg,(0,0))


# 绘制主角飞机
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(180,520))
pygame.display.update()

# 游戏循环
# 创建时钟对象
clock = pygame.time.Clock()
# 1.记录飞机的初始位置
hero_rect = pygame.Rect(180,520,100,124)
while True:
    # 指定刷新帧率
    clock.tick(60)
    # 2.修改飞机位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -124:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(bg,(0,0))  # 覆盖飞机
    screen.blit(hero,hero_rect)
    # 4.更新显示
    pygame.display.update()



pygame.quit()
