import pygame

from color import *


window = pygame.display.set_mode((480, 700))


class GameShow:

    def __init__(self):

        loading = pygame.image.load("images/loading.png")
        name = pygame.image.load("images/name.png")
        window.blit(loading, (-20, 100))
        window.blit(name, (20, 350))
        self.clock = pygame.time.Clock()
        while True:
            self.clock.tick(60)
            pygame.display.update()



































if __name__ == '__main__':
    g1 = GameShow()





