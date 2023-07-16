import sys

input = sys.stdin.readline

N = int(input())
DP = [0 for _ in range(N+1)]
numList = [[1] for _ in range(N+1)]
for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    numList[i] = numList[i-1] + [i]
    if i % 2 == 0:
        j = i//2
        if DP[j]+1 < DP[i]:
            DP[i] = DP[j]+1
            numList[i] = numList[j] + [i]
    if i % 3 == 0:
        j = i//3
        if DP[j]+1 < DP[i]:
            DP[i] = DP[j]+1
            numList[i] = numList[j] + [i]

print(DP[N])
result = numList[N]
result.reverse()
for i in result:
    print(i, end=" ")
print()