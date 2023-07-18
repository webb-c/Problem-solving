import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    count = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if graph[nx][ny] != "X" and not visited[nx][ny]:
                if graph[nx][ny] == "P":
                    count += 1
                visited[nx][ny] = True
                queue.append([nx, ny])
    if count == 0:
        count = "TT"
    return count


N, M = map(int, input().split())
graph = []
visited = []
for _ in range(N):
    line = list(input().strip())
    visited.append([False]*M)
    graph.append(line)
    if "I" in line:
        i = _
        j = line.index("I")
direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited[i][j] = True
print(bfs(i, j))