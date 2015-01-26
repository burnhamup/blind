from pygame import sprite
from blind.hero import Hero
from blind.input import Keyboard, Controller
from blind.maze import Wall
from blind.vibration import XinputVibration

__author__ = 'Chris'

class Level(object):
    def __init__(self):
        self.game_objects = sprite.Group()
        self.player = Hero(self)
        self.game_objects.add(self.player)
        self.walls = sprite.Group()
        for i in range(12):
            self.walls.add(Wall(32 + 32*i, 32, False))
            self.walls.add(Wall(32 + 32*i, 32*13, False))
            if i != 6 and i != 7:
                self.walls.add(Wall(32 + 32*i, 32*6, False))
            self.walls.add(Wall(32, 32 + 32*i, True))
            self.walls.add(Wall(32*13, 32 + 32*i, True))
        self.game_objects.add(self.walls)

        self.keyboard = Keyboard(self.player)
        self.controller = Controller(self.player)
        self.xinput = XinputVibration()

    def get_walls(self):
        return self.walls

    def draw(self, screen):
        for entity in self.game_objects:
            screen.blit(entity.image, entity.rect)

    def update(self):
        self.player.update()
        self.xinput.update()

    def event(self, event):
        self.keyboard.event(event)
        self.controller.event(event)

    def vibrate(self):
        self.xinput.vibrate(1, 2)



