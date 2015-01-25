from pygame.locals import *
import pygame

from blind.level import Level


class Game(object):
    WIN_WIDTH = 640
    WIN_HEIGHT = 480


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.WIN_WIDTH, Game.WIN_HEIGHT))
        self.running = True

        # Create The Backgound
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        self.level = Level()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False
            self.screen.blit(self.background, (0, 0))
            self.level.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

