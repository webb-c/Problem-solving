# 230629 백준
import sys
from collections import deque
import copy

input = sys.stdin.readline

direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs():
    global maxSafeArea
    testMap = copy.deepcopy(labMap)
    queue = copy.deepcopy(virusQ)
    # bfs
    while queue:
        r, c = queue.pop()
        for i in range(4):
            dr, dc = direct[i]  # 이동방향
            nr, nc = r + dr, c + dc  # 새로운 위치
            if 0 <= nr < N and 0 <= nc < M and testMap[nr][nc] == 0:
                testMap[nr][nc] = 2
                queue.append([nr, nc])  # 새로운 바이러스
    safeArea = sum(row.count(0) for row in testMap)
    maxSafeArea = max(maxSafeArea, safeArea)


def select_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if labMap[i][j] == 0:
                labMap[i][j] = 1
                select_wall(count + 1)
                labMap[i][j] = 0


N, M = map(int, input().split())
labMap = [list(map(int, input().split())) for _ in range(N)]
virusQ = deque()
# virus; bfs의 시작지점 queue에 append
for i in range(N):
    for j in range(M):
        if labMap[i][j] == 2:
            virusQ.append([i, j])

maxSafeArea = 0
select_wall(0)
print(maxSafeArea)
