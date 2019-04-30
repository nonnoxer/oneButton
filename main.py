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
            if variables.score >= 600:
                variables.palette = variables.six_to_never
            elif variables.score >= 300:
                variables.palette = variables.three_to_five
            else:
                variables.palette = variables.zero_to_two
            for i in range(3):
                variables.palette[i + 2] = (variables.palette[0][0] + (i + 1) * 10, variables.palette[0][1] + (i + 1) * 10, variables.palette[0][2] + (i + 1) * 10)
            pygame.draw.rect(variables.screen, variables.palette[1], (0, 0, 960, 412))
            pygame.draw.rect(variables.screen, variables.palette[4], (0, 412, 960, 32))
            pygame.draw.rect(variables.screen, variables.palette[3], (0, 444, 960, 32))
            pygame.draw.rect(variables.screen, variables.palette[2], (0, 476, 960, 32))
            pygame.draw.rect(variables.screen, variables.palette[0], (0, 508, 960, 32))

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
                    variables.enemies.append(classes.Enemy1(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), (variables.score // 100 + 1) * 3, variables.score // 100 + 1))
                    variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
                    if variables.timer % (variables.interval * 5) == 0:
                        variables.enemies.append(classes.Enemy2(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), variables.score // 100 + 1, (variables.score // 100 + 1) * 4))
                        variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
                        variables.timer = 0
            else:
                variables.enemies.append(classes.Enemy1(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), (variables.score // 100 + 1) * 3, variables.score // 100 + 1))
                variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
                variables.enemies.append(classes.Enemy2(32, variables.SIZEX, random.randint(0, variables.SIZEY - 32), variables.score // 100 + 1, (variables.score // 100 + 1) * 4))
                variables.enemiesGroup.add(variables.enemies[len(variables.enemies) - 1])
            variables.timer += 1

            variables.interval = 80 - variables.score // 10
            variables.screen.blit(variables.font.render('Score: ' + str(variables.score), False, variables.BLACK), (0, 16))

            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)

main = Main()
pygame.quit()
