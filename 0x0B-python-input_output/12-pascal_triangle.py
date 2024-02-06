#!/usr/bin/python3
"""this will be the task 12 file"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row."""
    if n <= 0:
        return []
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                element = 1
            else:
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
        triangle.append(row)
    return triangle

