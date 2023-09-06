#!/usr/bin/python3

"""
N-Queens Solver Module
"""

import sys

def is_safe(board, row, col):
    """
    Check if a queen can be placed at the given position
    without attacking any other queens on the board.

    Args:
        board (list[int]): List representing the current board state.
        row (int): The current row to check.
        col (int): The current column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row):
    """
    Recursive function to solve the N-queens problem.

    Args:
        N (int): The size of the chessboard (N x N).
        board (list[int]): List representing the current board state.
        row (int): The current row being considered.

    Prints:
        Solutions to the N-queens problem, one solution per line.
    """
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
