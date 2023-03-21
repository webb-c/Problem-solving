import sys
input = sys.stdin.readline

N = int(input())
costR = []
costG = []
costB = []
for _ in range(N) :
    R, G, B = map(int, input().split())
    costR.append(R)
    costG.append(G)
    costB.append(B)
for i in range(1, N) :
    costR[i] += min(costG[i-1], costB[i-1])
    costG[i] += min(costR[i-1], costB[i-1])
    costB[i] += min(costR[i-1], costG[i-1])
print(min(costR[N-1], costG[N-1], costB[N-1]))