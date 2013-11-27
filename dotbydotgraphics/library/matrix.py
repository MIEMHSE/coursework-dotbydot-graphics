#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2013, The Profitware Group'

from math import sin, cos


def matrix_multiply(a, b):
    """Matrix multiplication"""
    zip_b = zip(*b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def rotate_point_over_point_by_angle(point1, point2, angle):
    """Rotate point over point by specified angle"""
    rotation_matrix = lambda theta: [[cos(theta), sin(theta)],
                                     [-sin(theta), cos(theta)]]
    point_old = (point1[0] - point2[0], point1[1] - point2[1])
    point_new = zip(*matrix_multiply(rotation_matrix(angle), zip(*[point_old])))[0]
    return int(point_new[0] + point2[0]), int(point_new[1] + point2[1])


def reflect_point_over_point(point1, point2, horizontal, vertical):
    """reflect point over point"""
    reflect_matrix = lambda reflect_horizontal, reflect_vertical: \
        [[-1 if reflect_horizontal else 1, 0],
         [0, -1 if reflect_vertical else 1]]
    point_old = (point1[0] - point2[0], point1[1] - point2[1])
    point_new = zip(*matrix_multiply(reflect_matrix(horizontal, vertical),
                                     zip(*[point_old])))[0]
    return int(point_new[0] + point2[0]), int(point_new[1] + point2[1])


def scale_point_over_point_by_fraction(point1, point2, fraction_x, fraction_y):
    """Scale point over point by specified x- and y- fractions"""
    scaling_matrix = lambda sx, sy: [[sx, 0],
                                     [0, sy]]
    point_old = (point1[0] - point2[0], point1[1] - point2[1])
    point_new = zip(*matrix_multiply(scaling_matrix(fraction_x, fraction_y), zip(*[point_old])))[0]
    return int(point_new[0] + point2[0]), int(point_new[1] + point2[1])
