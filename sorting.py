import random

import pygame as pg
from random import randrange
import random
import numpy as np
import sys
import pygame
print('<Q> <W>  --  для изменения направления сортировки, <S>  --  запустить/остановить сортировку, <R>  --  создать новые столбцы')
count = int(input('количество столбцов от 1 до 1600        '))
sorts = False
scale = 1600 / count
rects = list()
left = False
right = True
color = (255, 0, 0)
sc = pg.display.set_mode((1800, 900))
clock = pygame.time.Clock()


def events():
    global sorts, left, right
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if sorts:
                    sorts = False
                else: sorts = True
            elif event.key == pygame.K_r:
                rectangles()
            elif event.key == pygame.K_q:
                left = True
                right = False
            elif event.key == pygame.K_w:
                left = False
                right = True
def draw():
    global rects
    x = 100
    for y in rects:
        if sorts:
            color = (255, 0, 0)
            pg.draw.rect(sc, color, (x, y, 1600/count, 900 - y))
        else:
            color = (0, 0, 0)
            pg.draw.rect(sc, color, (x, y, 1600/count, 900 - y))
        x += 1600/count
def rectangles():
    global rects, c
    rects.clear()
    for i in range(0, count):
        rects.append(i * 800/count)
    random.shuffle(rects)
def sort():
    global rects
    for i, rect in enumerate(rects):
        for i1, rect_1 in enumerate(rects):
            if left:
                if rect < rect_1:
                    rects[i] = rect_1
                    rects[i1] = rect
                    # pygame.draw.rect(sc, (255, 0, 0), (100 + (i * 1600 / count), rects[i], 1600 / count, 900 - rects[i]))
                    break
            elif right:
                if rect > rect_1:
                    rects[i] = rect_1
                    rects[i1] = rect
                    # pygame.draw.rect(sc, (255, 0, 0), (100 + (i * 1600 / count), rects[i], 1600 / count, 900 - rects[i]))
                    break
rectangles()

while True:
    sc.fill((255, 255, 255))
    events()
    draw()
    if sorts:
        sort()
    clock.tick()
    pygame.display.set_caption(f'{clock.get_fps()}')
    pg.display.flip()