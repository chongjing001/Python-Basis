
import pygame

pygame.init()
"""
2.创建游戏窗口
display.set_mode(窗口大小) - 窗口大小是一个元组，有两个元素
"""
window = pygame.display.set_mode((400, 500))
# 将窗口填充指定的颜色
"""
fill(颜色) - fill((r,g,b))
计算机颜色：计算机三原色 - 红、绿、蓝 （rgb）
           颜色值是由三个数字组成，分别代码红、绿、蓝、数字范围是：0~255
python中的颜色是一个元组，元组中有三个颜色，分别是r,g,b
"""
window.fill((255, 255, 0))
# 将窗口展示到显示设备上
pygame.display.flip()

# 3.创建游戏循环
while True:
    # 4.检测事件
    for event in pygame.event.get():
        # 区分不同的事件，做出反应
        # 判断关闭按钮点击事件是否发生
        if event.type == pygame.QUIT:
            exit()
