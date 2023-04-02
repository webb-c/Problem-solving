import sys
input = sys.stdin.readline

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0: break

    board = []
    for i in range(R):
        row = input().strip()
        board.append(row)

    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
                print("*", end='')
                continue
            count = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '*':
                    count += 1
            print(count, end='')
        print()