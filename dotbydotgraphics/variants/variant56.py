#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2013, The Profitware Group'

from dotbydotgraphics.library.brezenkhem import draw_line_brezenkhem as draw_line
from dotbydotgraphics.library.circle import draw_circle


def draw(width, height):
    """Draws rectangle with circle in it crossed by three-pointed star"""

    # Set points
    points = [(100, 100), (width - 100, height - 100)]
    point_top_left = points[0]
    point_bottom_left = (points[0][0], points[1][1])
    point_bottom_right = points[1]
    point_top_right = (points[1][0], points[0][1])
    point_middle = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
    point_middle_top = (point_middle[0], points[0][1])

    # Draw rectangle
    for point in draw_line(point_top_left, point_bottom_left):
        yield point
    for point in draw_line(point_bottom_left, point_bottom_right):
        yield point
    for point in draw_line(point_bottom_right, point_top_right):
        yield point
    for point in draw_line(point_top_right, point_top_left):
        yield point

    # Draw circle
    radius = int(min(abs(points[0][1] - points[1][1]), abs(points[1][0] - points[0][0])) / 3)
    for point in draw_circle(point_middle, radius):
        yield point

    # Circle for three-pointed star
    radius = int(min(abs(points[0][1] - points[1][1]), abs(points[1][0] - points[0][0])) / 7)
    i = 0
    for point in draw_circle(point_middle, radius):
        if i == 90:
            for line_point in draw_line(point, point_bottom_right):
                yield line_point
            for line_point in draw_line(point, point_bottom_left):
                yield line_point
        if i == 210:
            for line_point in draw_line(point, point_bottom_left):
                yield line_point
            for line_point in draw_line(point, point_middle_top):
                yield line_point
        if i == 330:
            for line_point in draw_line(point, point_bottom_right):
                yield line_point
            for line_point in draw_line(point, point_middle_top):
                yield line_point
        i += 1
