#!/usr/bin/python3
import sys

# Check the command line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    # Parse the integer argument
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check that N is at least 4
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# A utility function to print a solution
def print_solution(board):
    for row in board:
        print(" ".join(row))

# A utility function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

# A recursive function to solve the N Queens problem
def solve_n_queens(board, col, solutions):
    # If all queens are placed, add the solution to the list of solutions
    if col == n:
        solutions.append([row[:] for row in board])
        return

    # Try placing a queen in each row of this column
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            solve_n_queens(board, col + 1, solutions)
            board[row][col] = "."

# Solve the N Queens problem and print all solutions
board = [["." for _ in range(n)] for _ in range(n)]
solutions = []
solve_n_queens(board, 0, solutions)
for solution in solutions:
    print_solution(solution)
    print()
