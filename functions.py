board = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9, 0, 1, 2, 3],
    [4, 5, 6, 7, 8, 9, 0, 1, 2],
    [3, 4, 5, 6, 7, 8, 9, 0, 1],
    [2, 3, 4, 5, 6, 7, 8, 9, 0]
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
