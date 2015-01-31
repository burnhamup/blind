import logging
from pygame import joystick

from pygame.locals import *
from blind.hero import Hero


class Keyboard(object):
    def __init__(self, player):
        self.player = player

    def event(self, event):
        logging.debug('Firing event')
        if event.type == KEYDOWN or event.type == KEYUP:
            pressing_down = event.type == KEYDOWN
            if event.key == K_DOWN:
                self.player.move(Hero.DOWN, pressing_down)
            elif event.key == K_UP:
                self.player.move(Hero.UP, pressing_down)
            elif event.key == K_LEFT:
                self.player.move(Hero.LEFT, pressing_down)
            elif event.key == K_RIGHT:
                self.player.move(Hero.RIGHT, pressing_down)

class Controller(object):
    def __init__(self, player):
        self.player = player
        joystick.init()
        self.left_right_axis = None
        if joystick.get_count():
            self.joystick = joystick.Joystick(0)
            self.joystick.init()

    def event(self, event):
        if event.type in (JOYBUTTONDOWN, JOYBUTTONUP, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION):
            if event.joy != self.joystick.get_id():
                return
        if event.type == JOYAXISMOTION:
            print "%s %s" % (event.axis, event.value)
            if event.axis == 0:
                direction = None
                if event.value < -.5:
                    direction = Hero.LEFT
                if event.value > .5:
                    direction = Hero.RIGHT
                if direction != self.left_right_axis:
                    if direction:
                        self.player.move(direction, True)
                    else:
                        self.player.move(self.left_right_axis, False)
                self.left_right_axis = direction
            if event.axis == 1:
                self.player.move(Hero.UP, event.value < -.5)
                self.player.move(Hero.DOWN, event.value > .5)
        if event.type == JOYHATMOTION:
            right, up = event.value
            self.player.move(Hero.LEFT, right == -1)
            self.player.move(Hero.RIGHT, right == 1)
            self.player.move(Hero.UP, up == 1)
            self.player.move(Hero.DOWN, up == -1)


