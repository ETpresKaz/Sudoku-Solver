def check_row_by_row(board):
    for row in board:
        if len(row) != 9 or any(not isinstance(num, int) for num in row):
            return False
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return board

def get_columns(board, num):
    if num < 1 or num > 9:
        print("Invalid column number")
        return []
    return [row[num - 1] for row in board]

def check_columns(board):
    for i in range(1, 10):
        column = get_columns(board, i)
        if sorted(column) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return board

def get_square(board, x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Invalid square")
        return []
    return [board[i][j] for i in range(3*x, 3*x + 3) for j in range(3*y, 3*y + 3)]

def check_squares(board):
    for i in range(3):
        for j in range(3):
            square = get_square(board, i, j)
            if sorted(square) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
    return True

def check_sudoku(board):
    if check_row_by_row(board) and check_columns(board) and check_squares(board):
        return True
    return False


def is_valid_move(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):

    def find_empty_cell():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    empty_cell = find_empty_cell()
    if not empty_cell:
        return board

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return board
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(row)


board_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

board_2 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

board_3 = [
    [0, 8, 0, 4, 0, 5, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 4],
    [6, 0, 1, 0, 4, 0, 0, 2, 0],
    [0, 9, 2, 0, 0, 1, 0, 0, 5],
    [0, 0, 0, 9, 0, 7, 0, 0, 0],
    [0, 0, 0, 1, 0, 9, 0, 7, 6],
    [0, 2, 0, 7, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

board_4 = [
    [5, 0, 0, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 0, 9, 5, 3, 0, 8],
    [0, 9, 8, 3, 4, 2, 5, 0, 7],
    [8, 5, 9, 0, 6, 1, 4, 2, 0],
    [4, 0, 6, 8, 5, 3, 7, 0, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 0],
    [0, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 0, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 0, 8, 0, 1, 7, 9]
]

board_5 = [
    [5, 3, 4, 0, 7, 0, 0, 0, 0],
    [0, 7, 2, 1, 9, 5, 0, 0, 8],
    [1, 9, 8, 0, 4, 0, 5, 0, 7],
    [8, 0, 9, 7, 0, 1, 0, 2, 3],
    [4, 2, 6, 0, 5, 3, 7, 0, 1],
    [7, 0, 3, 0, 2, 4, 8, 5, 0],
    [9, 6, 1, 0, 3, 7, 0, 8, 0],
    [0, 8, 7, 4, 0, 9, 6, 3, 0],
    [3, 4, 5, 0, 8, 6, 1, 0, 9]
]

board_6 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 0],  
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 3, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 4],
    [0, 0, 7, 0, 0, 0, 0, 0, 0]
]
print(print_board(solve_sudoku(board_1)))
print(print_board(solve_sudoku(board_2)))
print(print_board(solve_sudoku(board_3)))
print(print_board(solve_sudoku(board_4)))
print(print_board(solve_sudoku(board_5)))
print(print_board(solve_sudoku(board_6)))

