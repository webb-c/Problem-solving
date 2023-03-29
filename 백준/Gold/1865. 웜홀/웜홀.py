import sys
input = sys.stdin.readline
INF = int(1e9)   # float("inf") 쓰면 안됨

def bellman_ford(start, graph, dist, N) :
    dist[start] = 0
    for i in range(N):
        for s in range(1, N+1):
            for e, time in graph[s] :
                if dist[e] > dist[s]+time :
                    dist[e] = dist[s]+time
                    if i == N-1 :
                        return False
    return True

TC = int(input())
for t in range(TC) :
    answer = "YES"
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [INF]*(N+1)
    for _ in range(M) :
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    for _ in range(W) :
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])
    if bellman_ford(1, graph, dist, N) : answer = "NO"
    print(answer)