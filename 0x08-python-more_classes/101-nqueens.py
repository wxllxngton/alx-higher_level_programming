#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    # without attacking any other queens on the board
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, board, row):
    # Recursive function to solve the N-queens problem
    if row == N:
        # All queens have been placed, print the solution
        print(board)
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(N, board, row + 1)


if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [-1] * N

    # Solve the N-queens problem
    solve_nqueens(N, board, 0)
