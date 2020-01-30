import pygame
from util import randomize_color, sequencial_color, box
import math
import random
from time import sleep
from time import time

"""
this is honestly some of my worst code, im writing this during class bc class is boring 

i was writing fast, some small aspects are hard coded. this was stupid of me 

comments are sub par
"""

pygame.init()
figure_size = 500
window = pygame.display.set_mode((figure_size, figure_size))

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

floorTop = 50 # distance from the bottom
player = box(100, floorTop)

floor = [box(-15, 0, h = figure_size)]

dis = 12.5 # distance between each block
for i in range(1, math.ceil(figure_size/dis)):
    colo = sequencial_color(floor[i-1].color, step = 20)
    floor.append(box(i*dis, 0, color = colo, h = figure_size))

floorVelo = 5
floorLen = len(floor)


player = box(50, figure_size-floorTop-100)
keys = pygame.key.get_pressed()
playerVelo = 0
veloJump = -50
grav = 50 # gravity on player
dt= .1

gapDistance = 100
def bar_gen(xpos):
    topPos = random.randint(round(figure_size/10), round(figure_size*2/5))
    topbar = box(xpos, 0, h = topPos, w = 25)
    bottombar = box(xpos, topPos + gapDistance , h = figure_size - topPos - gapDistance, w= 25)

    return [topbar, bottombar]


bars = []
bar_separation = 200
for i in range(3):
    bars.append(bar_gen(figure_size+i*700))# multiplying by -1 so we still have a list of 3 but they are irelivant to the fig


score = 0
t = time()
active = True
run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        run = False

    if keys[pygame.K_SPACE] and t < time() - .1:
        t = time()
        playerVelo += veloJump

    playerVelo += grav*dt

    player.y += playerVelo*dt

    # draw section

    window.fill((0, 0, 0))

    for i in range(len(bars)):
        for box in bars[i]:
            box.x -= floorVelo
        if bars[i][0].x < figure_size - bar_separation + floorVelo and bars[i][0].x > figure_size - bar_separation - floorVelo:
            xpos = figure_size
            topPos = random.randint(round(figure_size / 10), round(figure_size * 2 / 5))
            newIndex =(i+2)%3
            bars[newIndex][0].x = xpos
            bars[newIndex][0].h = topPos
            bars[newIndex][1].x = xpos
            bars[newIndex][1].y = topPos + gapDistance
            bars[newIndex][1].h = figure_size - topPos - gapDistance

        if bars[i][0].x + 25 > player.x and bars[i][0].x < player.x:
            if bars[i][0].h > player.y or bars[i][0].h + gapDistance - 25 < player.y:
                floorVelo = 0
                playerVelo = 500
                # i am not ending the loop bc the the loop will end when the player hits the ground
            else:

                score+=1

        if player.y > figure_size:
            sleep(1)
            run = False


    for bar in bars:
            for box in bar:
                pygame.draw.rect(window, box.color, (box.x, box.y, box.w, box.h))

    pygame.draw.rect(window, player.color, (player.x, player.y, player.w, player.h))
    draw_text(window, "Score: {}".format(score), 40, 100, 20)
    pygame.display.update()

