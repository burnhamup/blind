import logging
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