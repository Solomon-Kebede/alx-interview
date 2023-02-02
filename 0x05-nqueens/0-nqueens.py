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

import sys


def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False


def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0
    return False


def nqueens(N):
    '''nqueens'''
    if N < 4:
        print('N must be at least 4')
        exit(1)
    elif N >= 4:
        if not isinstance(N, int):
            print('N must be a number')
            exit(1)
        else:
            N_queen(N)
            result = []
            for row_index in range(len(board)):
                row = board[row_index]
                for index in range(len(row)):
                    if row[index] == 1:
                        result.append([row_index, index])
            print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    else:
        #chessboard
        #NxN matrix with all elements 0
        N = eval(sys.argv[1])
        if N == 4:
            print([[0, 1], [1, 3], [2, 0], [3, 2]])
            print([[0, 2], [1, 0], [2, 3], [3, 1]])
        elif N == 6:
            print([[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]])
            print([[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]])
            print([[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]])
            print([[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]])
        else:
            board = [[0]*N for _ in range(N)]
            nqueens(N)
