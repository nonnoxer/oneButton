import pygame
import pygame.font
pygame.init()
pygame.font.init()
import variables

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Jumper.png')
    def draw(self):
        pass
    def update(self):
        pass
