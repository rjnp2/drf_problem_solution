def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == "Q":
            return False
    
    return True

def solve_n_queens_util(board, row, N):
    if row >= N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = "Q"
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = '.'
    
    return False

# Example usage:
N = 4  # Change this to the desired board size
board = [['.' for _ in range(N)] for _ in range(N)]

if not solve_n_queens_util(board, 0, N):
    print("Solution does not exist")
else:
    print(board)