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
        self.dy = 0
        self.timer = 0
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.rect.y > 0:
            self.dy -= 19.62 / 32
        if self.rect.bottom < variables.SIZEY:
            self.dy += 9.81 / 32
        if self.rect.y < 0 or self.rect.bottom > variables.SIZEY:
            self.dy = 0
            self.rect.clamp_ip(variables.screenrect)
        self.rect.y += self.dy
        if self.timer >= 8:
            variables.bullets.append(Bullet(5, self.rect.centerx, self.rect.centery))
            variables.bulletsGroup.add(variables.bullets[len(variables.bullets) - 1])
            self.timer = 0
        self.timer += 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Laser.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.centerx = x
        self.rect.centery = y
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        self.rect.x += 4

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Monster.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
        self.hp = 3
        self.dy = 0
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if self.hp == 2:
            self.img = pygame.image.load('assets/Monster injure.png')
        if self.hp == 1:
            self.img = pygame.image.load('assets/Monster dying.png')
        if self.hp == 0:
            self.kill()
            variables.enemies.remove(self)
        self.rect.x -= 1

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Monster 2.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
        self.hp = 1
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if self.hp <= 0:
            self.kill()
            variables.enemies.remove(self)
        self.rect.x -= 8
