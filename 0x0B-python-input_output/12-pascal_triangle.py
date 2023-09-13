#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle"""
    tri_angle = []
    if n <= 0:
        return tri_angle
    if n == 0:
        return [[1]]

    tri_angle = [[1]]
    for i in range(n-1):
        tri_angle.append([a+b for a, b in zip([0] + tri_angle[-1], tri_angle[-1] + [0])])
    return tri_angle
