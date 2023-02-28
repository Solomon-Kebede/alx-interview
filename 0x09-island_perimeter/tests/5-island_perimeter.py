#!/usr/bin/python3
"""
Island Perimeter

Create a function `def island_perimeter(grid):` that
returns the perimeter of the island described in `grid`:
    - grid is a list of list of integers:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - `grid` is rectangular, with its width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn’t
    connected to the water surrounding the island).
"""


'''
           |  top_cell     |
----------------------------------------
left_cell  |  current_cell | right_cell
----------------------------------------
           |  bottom_cell  |
'''


def island_perimeter(grid):
    '''returns the perimeter of
    the island in the grid'''
    total_perimeter = 0
    water = 0
    land = 1
    for row_index in range(len(grid)):
        r = row_index
        row = grid[r]
        if land not in row:
            continue
        for column_index in range(len(row)):
            c = column_index
            free_perimeter = 0
            current_cell = grid[r][c]
            if current_cell == 1:
                top_row_index = r - 1
                bottom_row_index = r + 1
                left_column_index = c - 1
                right_column_index = c + 1

                if top_row_index < 0:
                    free_perimeter += 1
                else:
                    top_cell = grid[top_row_index][column_index]
                    if top_cell != land:
                        free_perimeter += 1

                if bottom_row_index >= len(grid):
                    free_perimeter += 1
                else:
                    bottom_cell = grid[bottom_row_index][column_index]
                    if bottom_cell != land:
                        free_perimeter += 1

                if left_column_index < 0:
                    free_perimeter += 1
                else:
                    left_cell = grid[row_index][left_column_index]
                    if left_cell != land:
                        free_perimeter += 1

                if right_column_index >= len(row):
                    free_perimeter += 1
                else:
                    # try:
                    #     right_cell = grid[row_index][right_column_index]
                    # except:
                    #     print(f'ri = {row_index} rci = {right_column_index}')
                    # right_cell = grid[0][0]
                    right_cell = grid[row_index][right_column_index]
                    if right_cell != land:
                        free_perimeter += 1
            total_perimeter = total_perimeter + free_perimeter
    return (total_perimeter)


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
