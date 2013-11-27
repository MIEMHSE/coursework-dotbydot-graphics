#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2013, The Profitware Group'

from math import pi
from sys import exit

import pygame
from pygame import *

from dotbydotgraphics.variants.variant56 import draw as draw_variant56
from dotbydotgraphics.library.matrix import rotate_point_over_point_by_angle, \
    scale_point_over_point_by_fraction, reflect_point_over_point


WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#FFFFFF"
DRAW_COLOR = "#000000"
ROTATION_ANGLE = pi / (180.0 / 30.0)
SCALE_X_FRACTION = 0.1
SCALE_Y_FRACTION = 0.1


def draw_all(surface, **kwargs):
    center_point = (int(WIN_WIDTH / 2), int(WIN_HEIGHT / 2))
    for point in draw_variant56(WIN_WIDTH, WIN_HEIGHT):
        point = rotate_point_over_point_by_angle(point, center_point, kwargs['angle'])
        point = reflect_point_over_point(point, center_point,
                                         kwargs['reflect_horizontal'], kwargs['reflect_vertical'])
        point = scale_point_over_point_by_fraction(point, center_point,
                                                   kwargs['scale_x'], kwargs['scale_y'])
        pygame.draw.circle(surface, Color(DRAW_COLOR), point, 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("dotbydot-graphics :: variant56")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    current_data_dict = {
        'angle': 0,
        'reflect_horizontal': False,
        'reflect_vertical': False,
        'scale_x': 1,
        'scale_y': 1
    }

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                exit(0)
            if e.type == KEYDOWN:
                key_symbol = e.unicode
                # r - rotate counterclockwise, R - rotate clockwise
                if key_symbol in ('r', 'R'):
                    if key_symbol == 'r':
                        current_data_dict['angle'] += ROTATION_ANGLE
                    else:
                        current_data_dict['angle'] -= ROTATION_ANGLE
                    if current_data_dict['angle'] < 0:
                        current_data_dict['angle'] = 2 * pi + current_data_dict['angle']
                    if 2 * pi - ROTATION_ANGLE / 2 < current_data_dict['angle'] and \
                            current_data_dict['angle'] < 2 * pi + ROTATION_ANGLE / 2:
                        current_data_dict['angle'] = 0
                # h or H - reflect horizontally
                if key_symbol in ('h', 'H'):
                    current_data_dict['reflect_horizontal'] = \
                        not current_data_dict['reflect_horizontal']
                # v or V - reflect vertically
                if key_symbol in ('v', 'V'):
                    current_data_dict['reflect_vertical'] = \
                        not current_data_dict['reflect_vertical']
                # x - overscale by x-axis, X - underscale by X-axis
                if key_symbol in ('x', 'X'):
                    if key_symbol == 'x':
                        current_data_dict['scale_x'] += SCALE_X_FRACTION
                    if key_symbol == 'X' and current_data_dict['scale_x'] > SCALE_X_FRACTION:
                        current_data_dict['scale_x'] -= SCALE_X_FRACTION
                # y - overscale by y-axis, Y - underscale by Y-axis
                if key_symbol in ('y', 'Y'):
                    if key_symbol == 'y':
                        current_data_dict['scale_y'] += SCALE_Y_FRACTION
                    if key_symbol == 'Y' and current_data_dict['scale_y'] > SCALE_Y_FRACTION:
                        current_data_dict['scale_y'] -= SCALE_Y_FRACTION
                bg.fill(Color(BACKGROUND_COLOR))
        draw_all(bg, **current_data_dict)
        screen.blit(bg, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
