import pygame
import pygame.font
pygame.init()
pygame.font.init()
import classes
import variables

button = classes.Button(304, 304, 32)
sentries = []
sentries.append(classes.Sentry(100, 100))

class Main(object):
    def __init__(self):
        while not variables.done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sentries.append(classes.Sentry(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                if event.type == pygame.QUIT:
                    variables.done = True

            variables.screen.fill(variables.BGCOLOUR)

            variables.screen.blit(button.draw(), (button.rect.x, button.rect.y))
            for i in sentries:
                variables.screen.blit(i.draw(), (i.rect.x, i.rect.y))
                i.update()

            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)

main = Main()
pygame.quit()
