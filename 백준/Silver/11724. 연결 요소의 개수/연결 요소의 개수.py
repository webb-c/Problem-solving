import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
visited = [ False for _ in range(N+1) ]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue :
        u = queue.popleft()
        for v in graph[u] :
            if not visited[v] :
                visited[v] = True
                queue.append(v)
    return 1

count = 0
for start in range(1, N+1) :
    if not visited[start] :
        count += bfs(start)
print(count)