import pygame
from blind.util import TILE_SIZE


class Wall(object):
    VERTICAL_WALL = pygame.Surface([2,32])
    HORIZONTAL_WALL = pygame.Surface([32,2])


class Maze(object):
    VERTICAL = 0
    HORIZONTAL = 1
    def __init__(self, width, height):
        self.maze = [[[False, False] for i in range(height+1)] for i in range(width+1)]
        for i in range(width):
            self.maze[i][0][self.HORIZONTAL] = True
            self.maze[i][height][self.HORIZONTAL] = True
        for i in range(height):
            self.maze[0][i][self.VERTICAL] = True
            self.maze[width][i][self.VERTICAL] = True

    def draw(self, screen):
        blit_count = 0
        for col_index, col in enumerate(self.maze):
            for row_index, row in enumerate(col):
                if row[self.VERTICAL]:
                    screen.blit(Wall.VERTICAL_WALL, (col_index * TILE_SIZE, row_index * TILE_SIZE))
                    blit_count += 1
                if row[self.HORIZONTAL]:
                    screen.blit(Wall.HORIZONTAL_WALL, (col_index * TILE_SIZE, row_index * TILE_SIZE))
                    blit_count += 1

