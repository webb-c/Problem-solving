import sys
input = sys.stdin.readline
INF = int(1e9)   # float("inf") 쓰면 안됨

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [INF]*(N+1)
for _ in range(M) :
    source, dest, weight = map(int, input().split())
    graph[source].append([dest, weight])

def bellman_ford(start):
    dist[start] = 0
    flag = False
    for _ in range(N):
        flag = False
        for source in range(1, N+1):
            for dest, weight in graph[source] :
                if dist[source] != INF and dist[dest] > dist[source] + weight:
                    dist[dest] = dist[source] + weight
                    flag = True
    if flag: return True
    else : return False

ret = bellman_ford(1)
if ret : print(-1)
else :
    for i in range(2, N+1) :
        if dist[i] == INF : print(-1)
        else : print(dist[i])