from sys import stdin
N, M, Q = map(int, stdin.readline().split())
vList = [0] * (N+M)
for _ in range(Q):
    op, i, v = map(int, stdin.readline().split())
    if op == 1: vList[i-1] += v
    else: vList[N+i-1] += v
for i in range(N):
    for j in range(M):
        print(vList[i]+vList[N+j], end=" ")
    print()