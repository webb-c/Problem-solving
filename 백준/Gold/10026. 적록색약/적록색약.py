import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
art = [ list(input()) for _ in range(N) ]
visited = [[False] * N for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 왼 오 앞 뒤

def bfs(x, y, color, RG):
    if RG and color == 'R' : color = 'G'
    queue = deque([[x, y]])
    while queue :
        x, y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4) :
                nx, ny = x+direct[i][0], y+direct[i][1]
                if 0 <= nx < N and 0 <= ny < N :
                    ncolor = art[nx][ny]
                    if RG and ncolor == 'R': ncolor = 'G'
                    if ncolor == color : queue.append([nx, ny])  # 같은 색이면 이어줌

# 정상
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] :
            color = art[i][j]
            bfs(i, j, color, False)
            count += 1
# 색약
visited = [[False] * N for _ in range(N)]
countRG = 0
for i in range(N) :
    for j in range(N) :
        if not visited[i][j] :
            color = art[i][j]
            bfs(i, j, color, True)
            countRG += 1

print(count, countRG)