import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 왼 오 앞 뒤
queue = deque([]) # 익은 토마토 목록
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

# BFS
while queue :
    x, y = queue.popleft()
    for i in range(4) :
        dx, dy = direct[i][0], direct[i][1]
        if 0 <= x+dx < N and 0 <= y+dy < M and tomato[x+dx][y+dy] == 0 :
            tomato[x+dx][y+dy] = tomato[x][y] + 1 # 날짜를 갱신하는 의미
            queue.append([x+dx, y+dy])

day = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 :
            print(-1)
            exit(0)
        day = max(day, tomato[i][j])

print(day-1)