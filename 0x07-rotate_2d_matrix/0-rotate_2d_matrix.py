#!/usr/bin/python3
"""
Testing 0x07 - Rotate 2D Matrix

You are not allowed to import any module
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    -Prototype: def rotate_2d_matrix(matrix):
    -Do not return anything. The matrix must be edited in-place.
    -You can assume the matrix will have 2 dimensions and will not be empty.
"""
'''
    c1 c2 c3
    ---------
r1 = 1  2  3
r2 = 4  5  6
r3 = 7  8  9


c1r1 = c1r3
c2r1 = c1r2
c3r1 = c1r1

c1r2 = c2r3
c2r2 = c2r2
c3r2 = c2r1

c1r3 = c3r3
c2r3 = c3r2
c3r3 = c3r1
------------------
r0c0 = r2c0
r0c1 = r1c0
r0c2 = r0c0

r1c0 = r2c1
r1c1 = r1c1
r1c2 = r0c1

r2c0 = r2c2
r2c1 = r1c2
r2c2 = r0c2
------------------
'''
def rotate_2d_matrix(matrix):
	"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
	matrix_size = len(matrix)
	# print(matrix)
	# print(id(matrix))
	matrix_copy = []
	for i in range(matrix_size):
		matrix_copy.append([0] * matrix_size)
	print(matrix_copy)
	# print(id(matrix), id(matrix_copy))
	# print(f"{matrix[0]} => {id(matrix[2])}")
	# matrix.reverse()
	# print(f"{matrix[0]} => {id(matrix[0])}")
	for row_index in range(matrix_size):
		for column_index in range(matrix_size):
			# print(f"({row_index}, {column_index}) = ({(matrix_size - 1) - column_index}, {row_index})")
			matrix_copy[row_index][column_index] = matrix[(matrix_size - 1) - column_index][row_index]
		print()
	print(matrix_copy)
