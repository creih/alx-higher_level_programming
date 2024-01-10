#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [[0] * len(r) for r in matrix]
    for element_c in range(len(matrix)):
        for element_r in range(len(matrix[element_c])):
            new_mat[element_c][element_r] = matrix[element_c][element_r]
    return new_mat
