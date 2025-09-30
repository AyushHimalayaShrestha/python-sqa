# Sudoku board validator
def is_valid_sudoku(board):
    for row in board:
        if len(set(row)) != len(row):  # check row duplicates
            return False
    for col in zip(*board):
        if len(set(col)) != len(col):  # check column duplicates
            return False
    return True

sudoku = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7]
]
print("Valid Sudoku?" , is_valid_sudoku(sudoku))
