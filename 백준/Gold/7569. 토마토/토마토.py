import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[]]
h = 0
for i in range(N*H) :
    line = list(map(int, input().split()))
    if i != 0 and i%N == 0 :
        tomato.append([])
        h+=1
    tomato[h].append(line)
direct = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)] # 위 아래 왼 오 앞 뒤
queue = deque([]) # 익은 토마토 목록
for i in range(H) :
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])
day = 0
# BFS
while queue :
    z, x, y = queue.popleft()
    for i in range(6) :
        dz, dx, dy = direct[i][0], direct[i][1], direct[i][2]
        if 0 <= z+dz < H and 0 <= x+dx < N and 0 <= y+dy < M and tomato[z+dz][x+dx][y+dy] == 0 :
            tomato[z+dz][x+dx][y+dy] = tomato[z][x][y] + 1 # 날짜를 갱신하는 의미
            queue.append([z+dz, x+dx, y+dy])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0 :
                print(-1)
                exit(0)
            day = max(day, tomato[i][j][k])

print(day-1)