import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
visited = [False]*(N+1)
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = True

def dfs(v) :
    visited[v] = True
    print(v, end=" ")
    for i in range(1, N+1) :
        if not visited[i] and graph[v][i] :
            dfs(i)

def bfs(v) :
    queue = deque()
    queue.append(v)
    while queue :
        n = queue.popleft()
        visited[n] = False # 재활용
        print(n, end=" ")
        for i in range(1, N+1) :
            if visited[i] and graph[n][i]:
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)