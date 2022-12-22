#!/usr/bin/python3

'''
Create a function `def pascal_triangle(n):` that returns
a list of lists of integers representing the Pascal’s triangle of `n`:
    - Returns an empty list if `n <= 0`
    - You can assume `n` will be always an integer
'''


def sum_list(list_array):
    '''Add all elements of a list'''
    total_sum = 0
    for item in list_array:
        total_sum += item
    return total_sum


def split_list(master_list):
    '''Split a list into a list of
    lists containing the current item
    and the next item'''
    computations = len(master_list) - 1
    new_list = []
    for i in range(computations):
        new_list.append([master_list[i], master_list[i + 1]])
    return new_list


def pascal_triangle(n):
    '''Generate a list of lists of the
    Pascal Triangle upto n'''
    outer_list = []
    if n <= 0:
        return outer_list
    elif n == 1:
        outer_list.append([1])
        return outer_list
    elif n == 2:
        outer_list = pascal_triangle(n - 1)
        outer_list.append([1, 1])
        return outer_list
    elif n >= 3:
        tmp = [1]
        outer_list = pascal_triangle(n - 1)
        new_list = outer_list[-1]
        for i in split_list(new_list):
            tmp.append(sum_list(i))
        tmp.append(1)
        outer_list.append(tmp)
        return outer_list
