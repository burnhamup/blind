import math
from pygame.sprite import Sprite, spritecollideany
from blind.util import load_image


class Hero(Sprite):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    FORWARD = 4
    BACKWARD = 5
    DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
    MOTIONS = [FORWARD, BACKWARD]
    #TODO Move this elsewhere
    TILE_SIZE = 32

    def __init__(self, level):

        Sprite.__init__(self)
        self.images = {
            self.UP: load_image("zph1_bk1.gif"),
            self.LEFT: load_image("zph1_lf1.gif"),
            self.RIGHT: load_image("zph1_rt1.gif"),
            self.DOWN: load_image("zph1_fr1.gif")
        }
        self.direction = self.DOWN
        self.image = self.images[self.DOWN]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.motion = {direction: False for direction in Hero.MOTIONS}
        self.speed = 2
        self.level = level
        self.moving_towards_distance = 0
        self.moving_towards_speed = 0

    def move(self, direction, start):
        if not self.is_moving():
            if direction in [self.LEFT, self.RIGHT] and start:
                if direction == self.LEFT:
                    self.direction = (self.direction - 1) % 4
                if direction == self.RIGHT:
                    self.direction = (self.direction + 1) % 4
        if direction in [self.UP, self.DOWN]:
            motion = self.FORWARD if direction == self.UP else self.BACKWARD
            self.motion[motion] = start

        # self.level.sound.play_ping(direction)


    def update(self):
        self.image = self.images[self.direction]
        old_location = self.rect.copy()
        if self.is_moving():
            speed = self.moving_towards_speed

            if self.direction == self.UP:
                self.rect.move_ip(0, -speed)
            elif self.direction == self.DOWN:
                self.rect.move_ip(0, speed)
            elif self.direction == self.LEFT:
                self.rect.move_ip(-speed, 0)
            elif self.direction == self.RIGHT:
                self.rect.move_ip(speed, 0)
            self.moving_towards_distance -= abs(speed)
        else:
            if any(self.motion.values()):
                self.moving_towards_distance = self.TILE_SIZE
                self.moving_towards_speed = self.speed
                if self.motion[self.BACKWARD]:
                    self.moving_towards_speed /= -2

            # if spritecollideany(self, self.level.get_walls()):
            #     self.rect = old_location
            #     self.level.vibrate()

    def is_moving(self):
        return self.moving_towards_distance > 0








