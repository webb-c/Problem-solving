# 230630 백준
import sys
import heapq

INF = 999999999
input = sys.stdin.readline


def dijkstra(st):
    global shortestPath
    shortestPath[st] = 0  # 자기자신까지 거리는 0
    queue = []
    heapq.heappush(queue, [0, st])

    while queue:
        dist, node = heapq.heappop(queue)
        if shortestPath[node] < dist:
            continue
        for nNode, weight in graph[node]:  # 현재 노드에서 갈 수 있는 다른 노드
            nDist = dist + weight
            if nDist < shortestPath[nNode]:
                shortestPath[nNode] = nDist
                heapq.heappush(queue, [nDist, nNode])


V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])  # 더 큰 weight가 들어오면 버리고 싶은데 비효율적인가?

shortestPath = [INF for _ in range(V + 1)]
dijkstra(K)
for i in range(1, V + 1):
    dist = shortestPath[i]
    if dist == INF:
        dist = "INF"
    print(dist)
