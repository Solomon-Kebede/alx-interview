#!/usr/bin/python3

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


def solveNQueens(n):
    '''Leetcode soln: solveNQueens'''
    ans = []
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def dfs(i, board):
        if i == n:
            ans.append(board)
            return

        for j in range(n):
            if cols[j] or diag1[i + j] or diag2[j - i + n - 1]:
                continue
            cols[j] = diag1[i + j] = diag2[j - i + n - 1] = True
            dfs(i + 1, board + ['.' * j + 'Q' + '.' * (n - j - 1)])
            cols[j] = diag1[i + j] = diag2[j - i + n - 1] = False

    dfs(0, [])
    return ans


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
            solutions = solveNQueens(N)
            for solution in solutions:
                result = []
                # print(solution)
                for positions in solution:
                    # print(positions)
                    row_index = solution.index(positions)
                    for row in positions:
                        if row == 'Q':
                            # print([row_index, positions.index(row)])
                            result.append([row_index, positions.index(row)])

                print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    else:
        N = eval(sys.argv[1])
        nqueens(N)
