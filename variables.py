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
zero_to_two = [(7,190,184), (196,255,249), 0, 0, 0, 'assets/tree tiny.png', 'assets/tree small.png', 'assets/tree medium.png', 'assets/tree large.png', 'assets/day cloud.png']
three_to_five = [(84,94,117), (184,179,233), 0, 0, 0, 'assets/night tiny.png', 'assets/night small.png', 'assets/night medium.png', 'assets/night large.png', 'assets/night cloud.png']
six_to_never = [(162,62,72), (255,60,56), 0, 0, 0, 'assets/ded tiny.png', 'assets/ded small.png', 'assets/ded medium.png', 'assets/ded large.png', 'assets/thunder cloud.png']

SIZEX = 960
SIZEY = 540
SIZE = (SIZEX, SIZEY)
CAPTION = "One Button"
FRAMERATE = 60

screen = pygame.display.set_mode(SIZE)
screenrect = screen.get_rect()
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 16)
bigfont = pygame.font.SysFont('Consolas', 32)
music = pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.play(-1)

done = False

bullets = []
bulletsGroup = pygame.sprite.Group()
enemies = []
enemiesGroup = pygame.sprite.Group()
timer = 0
score = 0
interval = 80
palette = []
bg = [[], [], [], [], [], []]
mode = 0
lives = 3
