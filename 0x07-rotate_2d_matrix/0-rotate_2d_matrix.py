#!/usr/bin/python3
"""
module to rotate matrix
"""


def matrix_transposed(A):
    """ transpose matrix A """
    size = len(A)
    for row in range(size):
        for col in range(row + 1, size):
            A[row][col], A[col][row] = A[col][row], A[row][col]


def matrix_reversed(A):
    """ reverse matrix A """
    i = 0
    j = len(A) - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1


def rotate_2d_matrix(matrix):
    """ rotate matrix 90 degrees clockwise """
    matrix_reversed(matrix)
    matrix_transposed(matrix)
