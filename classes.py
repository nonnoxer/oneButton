import pygame
import pygame.font
pygame.init()
pygame.font.init()
import variables

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Button.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.img)
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
    def draw(self):
        self.surface.blit(self.img, (0, 0))
        return self.surface

class Sentry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original = pygame.image.load('assets/Sentry.png')
        self.img = self.original
        self.orirect = self.img.get_rect()
        self.orirect.centerx = x
        self.orirect.centery = y
        self.rect = self.img.get_rect()
        self.rect.centerx = self.orirect.centerx
        self.rect.centery = self.orirect.centery
        self.mask = pygame.mask.from_surface(self.img)
        self.a = 1
    def draw(self):
        self.surface = pygame.Surface((self.rect.bottom, self.rect.right), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
        self.surface.blit(self.img, (0, 0))
        return self.surface
    def update(self):
        self.img = pygame.transform.rotate(self.original, self.a) #dont even know what i did it just works lol
        self.rect = self.img.get_rect()
        self.rect.centerx = self.orirect.centerx
        self.rect.centery = self.orirect.centery
        self.a = self.a + 1
        if self.a == 360:
            self.a = 0
