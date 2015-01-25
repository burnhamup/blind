from pygame.locals import *
import pygame

class Game(object):
    WIN_WIDTH = 640
    WIN_HEIGHT = 480
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WIN_WIDTH, Game.WIN_HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False

        pygame.quit()
