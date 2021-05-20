#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import pygame, math
from pygame.locals import *

global screen

# definition of line by DDa Method
def lineDDA(xa, ya, xb, yb, color_, sprite_):
    dx = xb - xa 
    dy = yb - ya
    if ( abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xIncrement = dx/steps
    yIncrement = dy/steps
    x = xa
    y = ya
    pa_ = pygame.PixelArray(sprite_)
    pa_[int(x)][int(y)] = pygame.Color(255, 255, 0)
    for k in range(1,int(steps)):
        x = x + xIncrement
        y = y + yIncrement
        pa_[int(x)][int(y)] = color_
    del pa_ # I don't why ??
    
    
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
lineDDA(100.0, 10.0, 120.0, 200.0, pygame.Color(255, 0, 0), screen) 
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
    pygame.display.update()