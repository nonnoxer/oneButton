import pygame
import pygame.font
pygame.init()
pygame.font.init()
import classes
import variables



class Main(object):
    def __init__(self):
        while not variables.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.done = True

            variables.screen.fill(variables.BGCOLOUR)

            

            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)

main = Main()
pygame.quit()
