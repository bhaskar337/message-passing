import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
TITLE = 'Message Passing'
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)
YELLOW = (0, 55, 250)
GRASS_GREEN = (102, 187, 106)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()



