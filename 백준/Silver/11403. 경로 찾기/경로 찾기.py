import sys
input = sys.stdin.readline

N = int(input())
graph = [ list(map(int, input().split())) for i in range(N)]
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if graph[i][k] and graph[k][j] : graph[i][j] = 1
for line in graph :
    print(' '.join(map(str, line)))