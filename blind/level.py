from pygame import sprite
from blind.hero import Hero
from blind.maze import Wall

__author__ = 'Chris'

class Level(object):
    def __init__(self):
        self.game_objects = sprite.Group()
        self.game_objects.add(Hero())
        for i in range(12):
            self.game_objects.add(Wall(32 + 32*i, 32, False))
            self.game_objects.add(Wall(32 + 32*i, 32*13, False))
            if i != 6 and i != 7:
                self.game_objects.add(Wall(32 + 32*i, 32*6, False))
            self.game_objects.add(Wall(32, 32 + 32*i, True))
            self.game_objects.add(Wall(32*13, 32 + 32*i, True))



    def draw(self, screen):
        for entity in self.game_objects:
            screen.blit(entity.image, entity.rect)


