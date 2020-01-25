import pygame
import random
from util import randomize_color, box
pygame.init()
figure_size = 500
window = pygame.display.set_mode((figure_size, figure_size))
score = 0

x, y, w, h = (50, 50, 25, 25)
velo = 2
color = (255, 0, 0)
direction = 'down'

boxs = [box(x, y), box(x, y-25), box(x, y-50), box(x, y-75)]

apple = box(250, 250)

run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # checking to see if the box is hitting the apple
    if abs(boxs[0].x - apple.x) <= 25 and abs(boxs[0].y - apple.y) <= 25:
        apple.x = random.randint(25, figure_size - 25)
        apple.y = random.randint(25, figure_size - 25)
        hold = boxs[len(boxs) - 1]
        boxs.append(box(hold.x, hold.y))
        velo += 1
        score += 1

    if keys[pygame.K_LEFT] and direction != 'right':
        direction = 'left'

    if keys[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'

    if keys[pygame.K_DOWN] and direction != 'up':
        direction = 'down'

    if keys[pygame.K_UP] and direction != 'down':
        direction = 'up'

    if keys[pygame.K_q]:
        run = False

    if direction == 'down':
        for i in range( len(boxs)-1, 0, -1):
            boxs[i].x = boxs[i - 1].x
            boxs[i].y = boxs[i - 1].y
            boxs[i].color = boxs[i - 1].color
        boxs[0].y += velo
        boxs[0].color = randomize_color()
    if direction == 'up':
        for i in range(len(boxs)-1, 0, -1):
            boxs[i].x = boxs[i - 1].x
            boxs[i].y = boxs[i - 1].y
            boxs[i].color = boxs[i - 1].color

        boxs[0].y -= velo
        boxs[0].color = randomize_color()
    if direction == 'left':
        for i in range( len(boxs)-1, 0, -1):
            boxs[i].x = boxs[i - 1].x
            boxs[i].y = boxs[i - 1].y
            boxs[i].color = boxs[i - 1].color

        boxs[0].x -= velo
        boxs[0].color = randomize_color()

    if direction == 'right':
        for i in range( len(boxs)-1, 0, -1):
            boxs[i].x = boxs[i - 1].x
            boxs[i].y = boxs[i - 1].y
            boxs[i].color = boxs[i - 1].color

        boxs[0].x += velo
        boxs[0].color = randomize_color()

    text = pygame.font.SysFont("comicsansms", 50).render("Score: "+str(score), True, (255, 255, 255))
    window.blit(text, [0,0])




    #'checking overlap'
    for i in range(1, len(boxs)):
        if abs(boxs[0].x - boxs[i].x) < velo and abs(boxs[0].y - boxs[i].y) < velo:
            run = False

    window.fill((0, 0, 0))

    for i in range(0, len(boxs)):
        pygame.draw.rect(window, boxs[i].color, (boxs[i].x, boxs[i].y, boxs[i].w, boxs[i].h))
    pygame.draw.rect(window, apple.color, (apple.x, apple.y, apple.w, apple.h))
    pygame.display.update()




pygame.quit()

