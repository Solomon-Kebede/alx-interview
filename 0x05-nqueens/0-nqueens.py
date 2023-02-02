#!/usr/bin/env python3
'''
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem.

    -Usage: nqueens N
        -If the user called the program with the wrong number of
        arguments, print Usage: nqueens N, followed by a new line, and
        exit with the status 1
    where N must be an integer greater or equal to 4
        -If N is not an integer, print N must be a number, followed by
        a new line, and exit with the status 1
        -If N is smaller than 4, print N must be at least 4, followed
        by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        -One solution per line
        -Format: see example
        -You don’t have to print the solutions in a specific order
    -You are only allowed to import the sys module
'''

from sys import argv


def nqueens(N):
    '''nqueens'''
    if N < 4:
        print('N must be at least 4')
        exit(1)
    elif N >= 4:
        if not isinstance(N, int):
            print('N must be a number')
            exit(1)
        print('HI')


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    else:
        N = eval(argv[1])
        nqueens(N)
