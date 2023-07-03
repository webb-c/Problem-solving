"""
Tic! Tac! Toe! by TAK x Corbin
https://www.youtube.com/watch?v=h5hMNF3kDm0
"""

import sys
input = sys.stdin.readline

def game_win(EL):
    for i in range(3):
        # 가로
        if board[i * 3] == EL and board[i * 3 : (i + 1) * 3].count(EL) == 3:
            return True
        # 세로
        if board[i] == EL and board[i] == board[i + 3] == board[i + 6]:
            return True
    # 대각선
    if board[4] == EL:
        if board[0] == board[4] == board[8]:
            return True
        if board[2] == board[4] == board[6]:
            return True
    return False

while True:
    board = input().strip()
    result = "invalid"
    isFull = False
    if board == "end":
        break
    clear = board.count("O")
    fail = board.count("X")
    if clear == fail or clear + 1 == fail:
        clearWin = game_win("O")
        failWin = game_win("X")
        if clearWin and failWin:
            result = "invalid"
        elif clearWin:
            # clear ? win
            if clear == fail:
                result = "valid"
        elif failWin:
            # fail ? win
            if clear + 1 == fail:
                result = "valid"
        elif board.count(".") == 0:
            result = "valid"

    print(result)
