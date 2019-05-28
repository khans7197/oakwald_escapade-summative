import pygame
#import random
from Tree_class import Tree

pygame.init()

height = 750
width = 750
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')
# colours
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
Tree_x = 0
Tree_y = 0
close = True

clear = []
#this is map 0 is nothing 1 is wall
map1 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111111111111111',
]
map2 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111110000011111',
]
map3 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '000000000000001',
    '000000000000001',
    '000000000000001',
    '000000000000001',
    '000000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111110000011111',
]
map4 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '000000000000000',
    '000000000000000',
    '000000000000000',
    '000000000000000',
    '000000000000000',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111110000011111',
]
lvl_type = 1

final_level = []
while close:
    if lvl_type == 1:
        final_level.append(clear)
        final_level.append(map1)
    if lvl_type == 2:
        final_level.append(clear)
        final_level.append(map2)
    if lvl_type == 3:
        final_level.append(clear)
        final_level.append(map3)
    if lvl_type == 4:
        final_level.append(clear)
        final_level.append(map4)


print(lvl_type)


for row in final_level:
    for col in row:
        if col == '1':
            Tree((Tree_x, Tree_y))
        if col == '0':
            floor((Floor_x, Floor_y))
    Tree_y += 50
    Tree_x = 0






while close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    screen.fill(WHITE)
    pygame.display.flip()