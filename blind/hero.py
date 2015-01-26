from pygame.sprite import Sprite, spritecollideany
from blind.util import load_image


class Hero(Sprite):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
    def __init__(self, level):

        Sprite.__init__(self)
        self.image = load_image("placeholder.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.directions = {direction: False for direction in Hero.DIRECTIONS}
        self.speed = 2
        self.level = level

    def move(self, direction, start):
        self.directions[direction] = start

    def update(self):
        old_location = self.rect.copy()
        if self.directions[Hero.UP]:
            self.rect.move_ip(0, -self.speed)
        if self.directions[Hero.DOWN]:
            self.rect.move_ip(0, self.speed)
        if self.directions[Hero.LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.directions[Hero.RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if spritecollideany(self, self.level.get_walls()):
            self.rect = old_location
            self.level.vibrate()









