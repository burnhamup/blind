from pygame import sprite
from blind.hero import Hero
from blind.input import Keyboard, Controller
from blind.maze import Wall, Maze
from blind.sound import Sound
from blind.vibration import XinputVibration

__author__ = 'Chris'

class Level(object):
    def __init__(self):
        self.game_objects = sprite.Group()
        self.player = Hero(self)
        self.game_objects.add(self.player)
        self.maze = Maze(5, 10)

        self.keyboard = Keyboard(self.player)
        self.controller = Controller(self.player)
        self.xinput = XinputVibration()
        self.sound = Sound()

    def get_walls(self):
        return self.maze

    def draw(self, screen):
        for entity in self.game_objects:
            screen.blit(entity.image, entity.rect)
        self.maze.draw(screen)

    def update(self):
        self.player.update()
        self.xinput.update()
        if self.player.is_moving():
            self.sound.play_footstep()
        else:
            self.sound.stop_footstep()

    def event(self, event):
        self.keyboard.event(event)
        self.controller.event(event)

    def vibrate(self):
        self.xinput.vibrate(1, 2)



