import pygame
import pygame.font
pygame.init()
pygame.font.init()
import variables

class Player(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Player.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
        self.timer = 0
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if pygame.mouse.get_pressed()[0] and self.timer >= 24:
            variables.bullets.append(Bullet(5, self.rect.centerx, self.rect.centery, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            self.timer = 0
        self.timer += 1
        self.rect.clamp_ip(variables.screenrect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, size, x, y, targx, targy):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Laser.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.centerx = x
        self.dx = (targx - x) / 32
        self.dy = (targy - y) / 32
        self.rect.centery = y
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.dy += 9.81 / 32

class Enemy(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Monster.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        self.rect.x -= 1
