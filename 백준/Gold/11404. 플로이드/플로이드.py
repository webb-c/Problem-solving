import sys

input = sys.stdin.readline
INF = 9999999

def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n = int(input())
m = int(input())
dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
floyd()
for a in range(1, n + 1):
    for b in range(1, n + 1):
        weight = dist[a][b]
        if weight == INF:
            weight = 0
        print(weight, end=" ")
    print()
