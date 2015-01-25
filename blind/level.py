from pygame import sprite
from blind.hero import Hero

__author__ = 'Chris'

class Level(object):
    def __init__(self):
        self.game_objects = sprite.Group()
        self.game_objects.add(Hero())

    def draw(self, screen):
        for entity in self.game_objects:
            screen.blit(entity.image, entity.rect)


