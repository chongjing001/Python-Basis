import pygame

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
while True:

    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    hero_rect.y -= 1

    if hero_rect.y <= -124:
        hero_rect.y = 700

    screen.blit(bg,(0,0))  # 覆盖飞机
    screen.blit(hero,hero_rect)
    # 4.更新显示
    pygame.display.update()



pygame.quit()
