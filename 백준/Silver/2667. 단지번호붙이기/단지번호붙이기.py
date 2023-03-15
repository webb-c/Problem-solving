import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
MAP = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]
visited = [[False]*N for _ in range(N)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(x, y) :
    count = 1
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x+move[i][0], y+move[i][1]
            if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                count += 1
                queue.append([nx, ny])
    return count

hList = []
for i in range(N) :
    for j in range(N) :
        if MAP[i][j] == 1 and not visited[i][j] :
            hList.append(bfs(i, j))

hList.sort()
print(len(hList))
for h in hList : print(h)