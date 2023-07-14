import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
maxHeight = 0
for _ in range(N):
    line = list(map(int, input().split()))
    maxHeight = max(maxHeight, max(line))
    graph.append(line)

result = 0
direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(x, y, height, visited):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if graph[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])


def get_region(height):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, height, visited)
                count += 1
    return count


for h in range(maxHeight+1):
    result = max(result, get_region(h))

print(result)
