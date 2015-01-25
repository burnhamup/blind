from pygame.sprite import Sprite
from blind.util import load_image


class Hero(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = load_image("placeholder.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)

