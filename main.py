# implement sudoku solver using backtracking algorithm
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def possible(x, y, n):
    global board
    for i in range(0, 9):
        if board[x][i] == n:
            return False
    for i in range(0, 9):
        if board[i][y] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[x0 + i][y0 + j] == n:
                return False
    return True


def solve():
    global board
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        board[x][y] = n
                        solve()
                        board[x][y] = 0
                return
    print_board(board)
    return


solve()
