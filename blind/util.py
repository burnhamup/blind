import os
import pygame

img_dir = os.path.join(os.getcwd(), 'img')
TILE_SIZE = 32


def load_image(filename):
    full_filename = os.path.join(img_dir, filename)
    try:
        image = pygame.image.load(full_filename)
    except pygame.error:
        print "Cannot load image: %s" % full_filename
        raise
    image = image.convert()
    return image