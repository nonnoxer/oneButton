import pygame
import pygame.font
pygame.init()
pygame.font.init()
import classes
import variables

player = classes.Jumper(32, 64, 0, 0, 0, 0, 1)
map = classes.Map('maps/main.txt')
print(variables.map)

class Main(object):
    def __init__(self):
        while not variables.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.done = True

            variables.screen.fill(variables.BGCOLOUR)

            variables.screen.blit(player.draw(), (player.rect.x, player.rect.y))
            player.update()

            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)

main = Main()
pygame.quit()
