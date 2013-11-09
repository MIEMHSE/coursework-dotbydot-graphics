#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2013, The Profitware Group'

from sys import exit
from time import sleep

import pygame
from pygame import *

from dotbydotgraphics.variants.variant56 import draw as draw_variant56


WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#000000"
DRAW_COLOR = "#FFFFFF"


def draw_all(surface):
    for point in draw_variant56(WIN_WIDTH, WIN_HEIGHT):
        pygame.draw.circle(surface, Color(DRAW_COLOR), point, 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("dotbydot-graphics :: variant56")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                exit(0)
        draw_all(bg)
        screen.blit(bg, (0, 0))
        pygame.display.update()
        sleep(1)


if __name__ == "__main__":
    main()
