#!/usr/bin/python3
"""
this is the file implementation for task 1
"""


def matrix_divided(matrix, div):
    """ this is my function to divide a matrix"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for umurongo in range(len(matrix)):
        for individ in umurongo:
            if not isinstance(matrix[umurongo][individ], (int, float)):
                return (msg)
            matrix[umurongo][individ] /= div
    return matrix
