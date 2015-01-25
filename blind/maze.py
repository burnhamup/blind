import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    VERTICAL_WALL = pygame.Surface([2,32])
    HORIZONTAL_WALL = pygame.Surface([32,2])

    def __init__(self, x, y, is_vertical=False):
        Sprite.__init__(self)
        if is_vertical:
            self.image = Wall.VERTICAL_WALL
        else:
            self.image = Wall.HORIZONTAL_WALL
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
