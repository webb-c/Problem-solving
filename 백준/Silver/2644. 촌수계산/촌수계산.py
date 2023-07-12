import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())  # 부모 자식 관계
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]


def dfs(u, dist, visited):
    for v in graph[u]:
        if not visited[v]:
            dist[v] = dist[u] + 1
            visited[v] = True
            dfs(v, dist, visited)


dfs(p1, dist, visited)
result = dist[p2]
if result == 0:
    result = -1
print(result)