import sys
import heapq
input = sys.stdin.readline
INF = float("inf")

N = int(input())
edge = [[-1]*N for _ in range(N)]
distList = [INF]*N

M = int(input())
for _ in range(M) :
    start, end, weight = map(int, input().split())
    if -1 < edge[start-1][end-1] <= weight : continue
    edge[start-1][end-1] = weight

start, end = map(int, input().split())
distList[start-1] = 0
heap = []
heapq.heappush(heap, (0, start-1))
while heap :
    dist, node = heapq.heappop(heap)
    if distList[node] < dist : continue
    for nNode, weight in enumerate(edge[node]) :
        if weight < 0 : continue
        nDist = dist + weight
        if nDist < distList[nNode] :
            distList[nNode] = nDist
            heapq.heappush(heap, (nDist, nNode))
print(distList[end-1])