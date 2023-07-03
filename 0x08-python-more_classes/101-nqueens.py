"""
101-nqueens.py

This module implements a solution for the N-queens problem using a recursive backtracking algorithm.

The N-queens problem is a classic puzzle where the goal is to place N queens on an N×N chessboard such that no two queens threaten each other. In other words, no two queens should share the same row, column, or diagonal.

This module provides functions to check if a queen can be placed at a given position without attacking any other queens and recursively solve the N-queens problem.

Usage: python3 101-nqueens.py N

    N: Size of the chessboard and the number of queens to be placed. Must be at least 4.

Example usage: python3 101-nqueens.py 8
"""

import sys

def is_safe(board, row, col):
    """
    Check if a queen can be placed at the given position on the board without attacking any other queens.
    
    Args:
        board (list): Current state of the board with queens placed.
        row (int): Current row being considered.
        col (int): Current column being considered.
        
    Returns:
        bool: True if it is safe to place a queen at the given position, False otherwise.
    """
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(N, board, row):
    """
    Recursive function to solve the N-queens problem.
    
    Args:
        N (int): Size of the board.
        board (list): Current state of the board with queens placed.
        row (int): Current row being considered.
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
