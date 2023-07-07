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


print_board(board)

