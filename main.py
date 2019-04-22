import pygame
import pygame.font
pygame.init()
pygame.font.init()
import classes
import variables

player = classes.Player(32, 64, variables.SIZEY - 32)

class Main(object):
    def __init__(self):
        while not variables.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    variables.done = True

            variables.screen.fill(variables.BGCOLOUR)

            for i in variables.bullets:
                variables.screen.blit(i.draw(), (i.rect.x, i.rect.y))
                i.update()
                if i.rect.right < 0 or i.rect.left > variables.SIZEX or i.rect.top > variables.SIZEY:
                    variables.bullets.remove(i)
            for i in variables.enemies:
                variables.screen.blit(i.draw(), (i.rect.x, i.rect.y))
                i.update()
            variables.screen.blit(player.draw(), (player.rect.x, player.rect.y))
            player.update()

            if variables.timer >= 48:
                variables.enemies.append(classes.Enemy(32, variables.SIZEX, variables.SIZEY - 32))
                variables.timer = 0
            variables.timer += 1

            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)

main = Main()
pygame.quit()
