


import pygame

pygame.init()


window = pygame.display.set_mode((400, 600))

# window.fill((255, 255, 0))
"""
显示图片

"""
bg = pygame.image.load("images/laoke.png")
"""
3.获取图片的大小
图片对象.get_size() - 获取图片大小，返回值是一个元组：（width,height）
"""

# 渲染图片
window.blit(bg, (0, 0))

pygame.display.update()


while True:
    # 4.检测事件
    for event in pygame.event.get():
        # 区分不同的事件，做出反应
        # 判断关闭按钮点击事件是否发生
        if event.type == pygame.QUIT:
            exit()