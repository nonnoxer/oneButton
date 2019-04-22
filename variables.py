import pygame
import pygame.font
pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOUR = WHITE

SIZEX = 960
SIZEY = 540
SIZE = (SIZEX, SIZEY)
CAPTION = "One Button"
FRAMERATE = 60

screen = pygame.display.set_mode(SIZE)
screenrect = screen.get_rect()
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

done = False

bullets = []
bulletsGroup = pygame.sprite.Group()
enemies = []
enemiesGroup = pygame.sprite.Group()
interval = 96
timer = 0
