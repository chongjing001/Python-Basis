
import pygame

pygame.init()
window = pygame.display.set_mode((480, 600))

"""
系统字体
pygame.font.SysFont(字体名，字体大小，是否加粗=False，是否倾斜=False) - 返回字体对象


"""
window.fill((255, 255, 255))
font = pygame.font.SysFont("SimHei", 15)

ziti = pygame.font.get_fonts()
for i in ziti:
    print(i)

"""
2.根据字体创建文字对象
"""
text = font.render("你好", True, (255, 0, 0))

# 将文字渲染到窗口上
window.blit(text, (100, 100))

pygame.display.update()













while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

