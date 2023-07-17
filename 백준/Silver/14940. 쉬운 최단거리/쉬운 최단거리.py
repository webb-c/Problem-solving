import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 2:
            distList[x][y] = 0
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                distList[nx][ny] = distList[x][y] + 1
                queue.append([nx, ny])
    return


n, m = map(int, input().split())
graph = []
visited = []
distList = []
for _ in range(n):
    visited.append([False]*m)
    distList.append([0]*m)
    line = list(map(int, input().split()))
    if 2 in line:
        j = line.index(2)
        i = _
    graph.append(line)

direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

bfs(i, j)
for i in range(n):
    for j in range(m):
        if distList[i][j] == 0 and graph[i][j] == 1:
            distList[i][j] = -1
        print(distList[i][j], end=" ")
    print()