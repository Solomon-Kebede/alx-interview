#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix

You are not allowed to import any module
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    -Prototype: def rotate_2d_matrix(matrix):
    -Do not return anything. The matrix must be edited in-place.
    -You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    matrix_size = len(matrix)
    matrix_copy = []
    # Base matrix for deep copy
    for i in range(matrix_size):
        matrix_copy.append([0] * matrix_size)
    # Deep copy of matrix
    for row_index in range(matrix_size):
        for column_index in range(matrix_size):
            matrix_copy[row_index][column_index] = matrix[
                (matrix_size - 1) - column_index
            ][row_index]
    # Edit old matrix in-place
    for row_index in range(matrix_size):
        for column_index in range(matrix_size):
            matrix[row_index][column_index] = matrix_copy[
                row_index
            ][column_index]
