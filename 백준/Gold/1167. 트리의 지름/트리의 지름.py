"""
1967과 차이점 : 똑같은데 이진트리가 아닌거?
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)  # 재귀제약

V = int(input())
tree = [[] for _ in range(V+1)]

def get_diameter():
    dist = [0 for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    visited[1] = True
    dfs(1, dist, visited)

    u = dist.index(max(dist))
    dist = [0 for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    visited[u] = True
    dfs(u, dist, visited)
    return max(dist)

# u번째 노드에 대한 dfs
def dfs(u, dist, visited):
    for v, w in tree[u]:
        if not visited[v]:
            dist[v] = dist[u] + w
            visited[v] = True
            dfs(v, dist, visited)

for _ in range(V):
    inList = list(map(int, input().split()))
    p = inList[0]
    for i in range(1, len(inList)-1, 2):
        c = inList[i]
        w = inList[i+1]
        tree[p].append([c, w])
        tree[c].append([p, w])
print(get_diameter())
