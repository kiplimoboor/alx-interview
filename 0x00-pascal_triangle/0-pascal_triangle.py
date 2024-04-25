#!/usr/bin/python3
"""Module implementing pascal's triangle"""


def pascal_triangle(n):
    """
    Creates a pascal triangle with a given n rows

    Args:
        n [int]: the height of the triangle
    Returns:
        triangle [list]: a list of lists that is the triangle
    """

    if n <= 0:
        return [[]]
    triangle = [[1]]

    for _ in range(1, n):
        row = []
        prev = [0] + triangle[-1] + [0]
        row = [prev[i] + prev[i+1] for i in range(len(prev) - 1)]
        triangle.append(row)

    return triangle
