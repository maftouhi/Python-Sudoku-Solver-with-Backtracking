sudoku_board = [
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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')


def find_empty(baord):
    for i in range(len(baord)):
        for j in range(len(baord[1])):
            if baord[i][j] == 0:
                return i, j
    return None


def validation(board, num, pos):
    # In Row
    for j in range(len(board[1])):
        if board[pos[0]][j] == num and j != pos[1]:
            return False

    # In Column
    for j in range(len(board)):
        if board[j][pos[1]] == num and j != pos[0]:
            return False

    # In Box
    boxY = pos[0] // 3
    boxX = pos[1] // 3

    for j in range(boxY * 3, boxY + 3):
        for i in range(boxX * 3, boxX + 3):
            if board[j][i] == num and (j, i) != pos:
                return False

    return True  # No Duplicate


def solve(board):
    if not find_empty(board):
        return True
    else:
        x, y = find_empty(board)
        for i in range(1, 10):
            if validation(board, i, (x, y)):
                board[x][y] = i

                if solve(board):
                    return True
                board[x][y] = 0
    return False


solve(sudoku_board)
print_board(sudoku_board)