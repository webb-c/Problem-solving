# 230701 백준
import sys
from collections import deque

input = sys.stdin.readline
# 누가봐도 BFS
direct = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


def bfs(i, j):
    islandQ = deque()
    islandQ.append([i, j])
    while islandQ:
        r, c = islandQ.pop()
        for i in range(8):
            dr, dc = direct[i]
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and squareMap[nr][nc] == 1:
                squareMap[nr][nc] = 0
                islandQ.append([nr, nc])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    squareMap = [list(map(int, input().split())) for _ in range(h)]
    islandNum = 0
    for i in range(h):
        for j in range(w):
            if squareMap[i][j] != 0:
                bfs(i, j)
                squareMap[i][j] = 0
                islandNum += 1
    print(islandNum)
