#!/usr/bin/python3
"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of list of integers"""
    if n <= 0:
        return []

    x = [[1]]
    while len(x) != n:
        tri = x[-1]
        y = [1]
        for i in range(len(tri) - 1):
            y.append(tri[i] + tri[i + 1])
        y.append(1)
        x.append(y)
    return x
