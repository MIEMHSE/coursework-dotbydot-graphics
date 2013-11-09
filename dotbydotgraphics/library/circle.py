#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2013, The Profitware Group'

from math import sin, cos, pi


def draw_circle(point, radius):
    """Draws circle by points tuple and radius"""
    for i in xrange(0, 360):
        x = point[0] + int(radius * cos(pi / 180 * i))
        y = point[1] + int(radius * sin(pi / 180 * i))
        yield (x, y)
