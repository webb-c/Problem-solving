# 230701 백준
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]  # 경로압축 (direct-root)

def union(a, b):
    pA = find(a)
    pB = find(b)
    if pA == pB:
        return
    if pA < pB:
        parent[pB] = pA
    else:
        parent[pA] = pB

# 크루스칼
def kruskal():
    weight = 0
    edges.sort()
    for w, u, v in edges:
        if find(u) == find(v):
            continue
        weight += w
        union(u, v)
    return weight


# 프림
# def prim():


# input
V, E = map(int, input().split())
parent = list(range(V + 1))
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append([w, u, v])

result = kruskal()
# result = prim()
print(result)
