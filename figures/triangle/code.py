import math
__all__ = ['triangle_perimeter', 'triangle_area']
a, b, c = 7, 2, 8


def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_area(a, b, c):
    return math.sqrt(((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))
