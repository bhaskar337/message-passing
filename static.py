import pygame
from config import *

import time


class Static:
    def __init__(self, path, x, y, width, height):

        self.static = pygame.image.load(path)
        self.static = pygame.transform.scale(self.static, (width, height))
        self.posx = x
        self.posy = y

    def render(self):
        screen.blit(self.static, (self.posx, self.posy))
