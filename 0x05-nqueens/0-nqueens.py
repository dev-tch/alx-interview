#!/usr/bin/python3
""" module with goal to resolve the probleme N queens"""
import sys
import re


def valid_args():
    """ validate args passed to resolve problem N queens """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    arg_nb_queens = sys.argv[1]
    pattern = r'\d+'
    m = re.fullmatch(pattern, arg_nb_queens, flags=0)
    if not m:
        print("N must be a number")
        sys.exit(1)
    N = int(arg_nb_queens)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def can_place_queen(matrix, row, col):
    """ check if we can place queen in (row, col)"""
    for i in range(row):
        valid_position = any(
            [
                matrix[i] == col,
                matrix[i] - i == col - row,
                matrix[i] + i == col + row
            ]
            )
        if valid_position:
            return False
    return True


def add_queen_to_matrix(matrix, row):
    """ print each solution in one line + place new queen """
    if row == N:
        print([[i, matrix[i]] for i in range(N)])
        return
    for col in range(N):
        if can_place_queen(matrix, row, col):
            matrix[row] = col
            # search another position for new queen
            add_queen_to_matrix(matrix, row + 1)


def compute_nqueens(N):
    """print all solutions for N queens problem"""
    # init matrix will  one row all values -1
    matrix = [-1] * N
    add_queen_to_matrix(matrix, 0)


if __name__ == "__main__":
    N = valid_args()
    compute_nqueens(N)
