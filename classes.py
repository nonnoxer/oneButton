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
        self.mult = []
    def draw(self):
        self.surface = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
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
        if self.timer >= variables.interval // 10:
            for i in self.mult:
                if i == 0:
                    variables.bullets.append(Bullet(5, self.rect.centerx, self.rect.centery, 0))
                    variables.bulletsGroup.add(variables.bullets[len(variables.bullets) - 1])
                else:
                    variables.bullets.append(Bullet(5, self.rect.centerx, self.rect.centery, i))
                    variables.bulletsGroup.add(variables.bullets[len(variables.bullets) - 1])
                    variables.bullets.append(Bullet(5, self.rect.centerx, self.rect.centery, -i))
                    variables.bulletsGroup.add(variables.bullets[len(variables.bullets) - 1])
            self.timer = 0
        self.mult = range(variables.score // 100 + 1)
        self.timer += 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, size, x, y, dy):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Laser.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.centerx = x
        self.rect.centery = y
        self.dy = dy
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        self.rect.x += 4
        self.rect.y += self.dy

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, size, x, y, hp, dx):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Monster.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
        self.hp = hp
        self.orihp = hp
        self.dy = 0
        self.dx = dx
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if self.hp == 0:
            self.kill()
            variables.enemies.remove(self)
            variables.score += variables.score // 100 + 1
        elif self.hp / self.orihp <= 1 / 3:
            self.img = pygame.image.load('assets/Monster dying.png')
        elif self.hp / self.orihp <= 2 / 3:
            self.img = pygame.image.load('assets/Monster injure.png')
        self.rect.x -= self.dx

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, size, x, y, hp, dx):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Monster 2.png')
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        self.rect.x = x
        self.rect.y = y
        self.hp = hp
        self.orihp = hp
        self.dx = dx
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        if self.hp <= 0:
            self.kill()
            variables.enemies.remove(self)
            variables.score += variables.score // 100 + 1
        self.rect.x -= self.dx

class BGImage(object):
    def __init__(self, img, x, y, size, dx):
        self.img = pygame.image.load(img)
        self.trux = x
        self.truy = y
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        self.trux += self.dx
        self.rect.x = self.trux
