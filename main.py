#my code sucks

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
            if variables.mode == 0:
                variables.screen.fill(variables.WHITE)
                variables.screen.blit(pygame.image.load('assets/One Button.png'), (380, 170))
                variables.screen.blit(variables.bigfont.render('One Button', False, variables.BLACK), (390, 238))
                variables.screen.blit(variables.font.render('Press SPACE to start', False, variables.BLACK), (390, 270))
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    variables.mode = 1
            elif variables.mode == 1:
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

                for i in variables.bg:
                    for j in i:
                        variables.screen.blit(j.draw(), (j.rect.x, j.rect.y))
                        j.update()
                        if j.rect.right < 0:
                            i.remove(j)
                for i in variables.bullets:
                    variables.screen.blit(i.draw(), (i.rect.x, i.rect.y))
                    i.update()
                    if i.rect.x > variables.SIZEX:
                        i.kill()
                        variables.bullets.remove(i)
                for i in variables.enemies:
                    variables.screen.blit(i.draw(), (i.rect.x, i.rect.y))
                    i.update()
                    if i.rect.right < 0:
                        i.kill()
                        variables.enemies.remove(i)
                        variables.score -= variables.score // 100 + 1
                        variables.lives -= 1
                variables.screen.blit(player.draw(), (player.rect.x, player.rect.y))
                player.update()

                ef_collide = pygame.sprite.groupcollide(variables.enemiesGroup, variables.bulletsGroup, False, True, pygame.sprite.collide_mask)
                ef_collide_enemies = ef_collide.keys()
                ef_collide_bullets = ef_collide.values()
                for i in ef_collide_enemies:
                    i.hp -= 1
                for i in ef_collide_bullets:
                    variables.bullets.remove(i[0])

                prob = random.randint(0, 199)
                if prob >= 199:
                    variables.bg[0].append(classes.BGImage('assets/star.png', variables.SIZEX, random.randint(0, 404), 8, -0.1))
                elif prob >= 198:
                    variables.bg[1].append(classes.BGImage(variables.palette[9], variables.SIZEX, random.randint(0, 238), 64, -0.2))
                elif prob >= 196:
                    variables.bg[2].append(classes.BGImage(variables.palette[5], variables.SIZEX, 404, 8, -0.4))
                elif prob >= 194:
                    variables.bg[3].append(classes.BGImage(variables.palette[6], variables.SIZEX, 428, 16, -0.8))
                elif prob >= 192:
                    variables.bg[4].append(classes.BGImage(variables.palette[7], variables.SIZEX, 444, 32, -1.6))
                elif prob >= 190:
                    variables.bg[5].append(classes.BGImage(variables.palette[8], variables.SIZEX, 444, 64, -3.2))
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
                if variables.lives <= 0:
                    variables.mode = 2
                if variables.score < 0:
                    variables.score = 0
                variables.screen.blit(variables.font.render('Score: ' + str(variables.score), False, variables.BLACK), (0, 0))
                variables.screen.blit(variables.font.render('Lives: ' + str(variables.lives), False, variables.BLACK), (0, 16))
            elif variables.mode == 2:
                variables.screen.fill(variables.WHITE)
                variables.screen.blit(variables.bigfont.render('Game Over', False, variables.BLACK), (390, 238))
                variables.screen.blit(variables.font.render('Final Score: ' + str(variables.score), False, variables.BLACK), (390, 270))
                variables.screen.blit(variables.font.render('Press SPACE to restart', False, variables.BLACK), (390, 286))
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    variables.bullets = []
                    variables.bulletsGroup = pygame.sprite.Group()
                    variables.enemies = []
                    variables.enemiesGroup = pygame.sprite.Group()
                    variables.timer = 0
                    variables.score = 0
                    variables.interval = 80
                    variables.palette = []
                    variables.bg = [[], [], [], [], [], []]
                    variables.mode = 1
                    variables.lives = 3
            pygame.display.flip()
            variables.clock.tick(variables.FRAMERATE)


if __name__ == '__main__':
    main = Main()
    pygame.quit()
