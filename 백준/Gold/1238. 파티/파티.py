"""
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append([v, t])


def dijkstra(start, shortestDist):
    shortestDist[start] = 0  # 자기자신까지 거리는 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        dist, node = heapq.heappop(queue)
        if shortestDist[node] < dist:
            continue
        for nNode, weight in graph[node]:  # 현재 노드에서 갈 수 있는 다른 노드
            nDist = dist + weight
            if nDist < shortestDist[nNode]:
                shortestDist[nNode] = nDist
                heapq.heappush(queue, [nDist, nNode])


backShortestDist = [INF for _ in range(N+1)]
totalShortestDist = [-INF for _ in range(N+1)]

# 컴백
dijkstra(X, backShortestDist)

for i in range(1, N+1):
    goShortestDist = [INF for _ in range(N+1)]
    dijkstra(i, goShortestDist)
    totalShortestDist[i] = goShortestDist[X]+backShortestDist[i]

print(max(totalShortestDist))
