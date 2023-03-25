import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
edge = [[] for _ in range(N+1)]
parents = [0]*(N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

def bfs(edge, v, parents):
    queue = deque([v])
    while queue:
        n = queue.popleft()
        for i in edge[n]:
            if parents[i] == 0:
                parents[i] = n
                queue.append(i)

bfs(edge, 1, parents)
for i in range(2, N+1):
    print(parents[i])