
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 640))
game_ground = pygame.image.load("images/background.png")
snake_head = pygame.image.load("images/laoke.png")
screen.blit(game_ground, (0, 0))
screen.blit(snake_head, (400, 500))
pygame.display.update()
snake_rect = pygame.Rect(400, 500, 27, 104)


clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            exit()

    snake_rect.y -= 10

    screen.blit(snake_head, snake_rect)

    pygame.display.update()


















