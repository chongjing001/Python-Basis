import pygame

pygame.init()

screen = pygame.display.set_mode((480,700))

# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.bilt 绘制图像
screen.blit(bg,(0,0))
# 3.update 更新图像显示
pygame.display.update()

# 绘制主角飞机
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(180,520))
pygame.display.update()

# 游戏循环
# 创建时钟对象
clock = pygame.time.Clock()
i = 0
while True:
    # 指定刷新帧率
    clock.tick(60)
    print(i)
    i += 1
    pass

pygame.quit()
