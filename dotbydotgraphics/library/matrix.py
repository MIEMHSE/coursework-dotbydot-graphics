#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2013, The Profitware Group'


from math import sin, cos


def matrix_multiply(a, b):
    zip_b = zip(*b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]


rotation_matrix = lambda theta: [[cos(theta), sin(theta)],
                                 [-sin(theta), cos(theta)]]


def rotate_point_by_angle(point, angle):
    return zip(*matrix_multiply(rotation_matrix(angle), zip(*[point])))[0]


def rotate_point_over_point_by_angle(point1, point2, angle):
    point_old = (point1[0] - point2[0], point1[1] - point2[1])
    point_new = rotate_point_by_angle(point_old, angle)
    return int(point_new[0] + point2[0]), int(point_new[1] + point2[1])