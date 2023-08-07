import math
from sys import stdin
input = stdin.readline


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


n = int(input())
starList = [list(map(float, input().strip().split())) for _ in range(n)]
edges = []

for u, star_u in enumerate(starList):
    x1, y1 = star_u
    for v, star_v in enumerate(starList[u:]):
        if v == 0:
            continue
        x2, y2 = star_v
        w = get_distance(x1, y1, x2, y2)
        edges.append([w, u, u+v])
        edges.append([w, u+v, u])


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


def kruskal():
    weight = 0
    edges.sort()
    for w, u, v in edges:
        if find(u) == find(v):
            continue
        weight += w
        union(u, v)
    return weight


parent = list(range(n + 1))
result = kruskal()
print(result)