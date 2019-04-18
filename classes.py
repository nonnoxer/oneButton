import pygame
import pygame.font
pygame.init()
pygame.font.init()
import variables

class Jumper(pygame.sprite.Sprite):
    def __init__(self, size, x, y, vx, vy, ax, ay):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Jumper 0.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.pressed = 0
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.pressed == 0:
            self.ay *= -1
            self.pressed = 1
        elif not pygame.key.get_pressed()[pygame.K_SPACE]:
            self.pressed = 0
        self.rect.y += self.vy
        self.vy += self.ay
        if (self.vy < 10 and self.ay > 0) or (self.vy > -10 and self.ay < 0):
            self.vy += self.ay
        else:
            if self.ay > 0:
                self.vy = 10
            elif self.ay < 0:
                self.vy = -10
        self.rect.x += self.vx
        self.vx += self.ax
        if (self.rect.bottom >= 640 and self.ay > 0) or (self.rect.top <= 0 and self.ay < 0):
            self.vy = 0
        self.rect.clamp_ip(variables.screenrect)

class Map(object):
    def __init__(self, file):
        self.file = open(file, 'r')
        self.contents = self.file.readlines()
        self.stuff = []
        for i in self.contents:
            i = i.replace('\n', '')
            self.stuff.append(list(i))
            for j in i:
                variables.map.append(Tile(j))

class Tile(pygame.sprite.Sprite):
    def __init__(self, typ):
        pygame.sprite.Sprite.__init__(self)

        self.typ = typ
