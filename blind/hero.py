import math
import pygame
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
        self.x_float, self.y_float = self.rect.x, self.rect.y
        self.directions = {direction: False for direction in Hero.DIRECTIONS}
        self.speed = 2
        self.rotation_speed = math.pi / 2
        self.level = level
        self.angle = 0.0
        self.x_angle = math.cos(self.angle)
        self.y_angle = math.sin(self.angle)

    def move(self, direction, start):
        if direction in [self.LEFT, self.RIGHT] and start:
            if direction == self.LEFT:
                self.angle -= self.rotation_speed
            if direction == self.RIGHT:
                self.angle += self.rotation_speed
            print math.degrees(self.angle)
            self.x_angle = math.cos(self.angle)
            self.y_angle = math.sin(self.angle)
        elif direction in [self.UP, self.DOWN]:
            self.directions[direction] = start
        # self.level.sound.play_ping(direction)

    def update(self):
        old_location = self.rect.copy()
        old_x_float, old_y_float = self.x_float, self.y_float
        if self.directions[Hero.UP]:
            self.x_float += self.speed * self.x_angle
            self.y_float += self.speed * self.y_angle
        if self.directions[Hero.DOWN]:
            self.x_float -= self.speed * self.x_angle
            self.y_float -= self.speed * self.y_angle

        self.rect.x, self.rect.y = self.x_float, self.y_float

        if spritecollideany(self, self.level.get_walls()):
            self.rect = old_location
            self.x_float, self.y_float = old_x_float, old_y_float
            self.level.vibrate()
    def is_moving(self):
        return any(self.directions.values())









