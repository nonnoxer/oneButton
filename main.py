import pygame
import pygame.font
pygame.init()
pygame.font.init()
import classes
import variables
import random

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
                    i.kill()
                    variables.bullets.remove(i)
            for i in variables.enemies:
                variables.screen.blit(i.draw(), (i.rect.x, i.rect.y))
                i.update()
                if i.rect.right < 0:
                    i.kill()
                    variables.enemies.remove(i)
                    variables.score -= variables.score // 100 + 1
            variables.screen.blit(player.draw(), (player.rect.x, player.rect.y))
            player.update()

            ef_collide = pygame.sprite.groupcollide(variables.enemiesGroup, variables.bulletsGroup, False, True, pygame.sprite.collide_mask)
            ef_collide_enemies = ef_collide.keys()
            ef_collide_bullets = ef_collide.values()
            for i in ef_collide_enemies:
                i.hp -= 1
            for i in ef_collide_bullets:
                variables.bullets.remove(i[0])

            if variables.interval > 0:
                if variables.timer % variables.interval == 0:
                    variables.enemies.append(classes.Enemy1(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), (variables.score // 100 + 1) * 2, variables.score // 100 + 1))
                    variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
                    if variables.timer % (variables.interval * 5) == 0:
                        variables.enemies.append(classes.Enemy2(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), variables.score // 100 * 1 + 1, (variables.score // 100 + 1) * 4))
                        variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
                        variables.timer = 0
            else:
                variables.enemies.append(classes.Enemy1(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), (variables.score // 100 + 1) * 2, variables.score // 100 + 1))
                variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
                variables.enemies.append(classes.Enemy2(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), variables.score // 100 * 1 + 1, (variables.score // 100 + 1) * 4))
                variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
            variables.timer += 1

            variables.interval = 80 - variables.score // 10
            print(variables.score)

            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)

main = Main()
pygame.quit()
