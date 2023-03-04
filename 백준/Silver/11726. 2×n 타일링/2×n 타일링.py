import sys
input = sys.stdin.readline

N = int(input())
DP = [0, 1, 2] + [0]*(N-2)
for i in range(3, N+1) :
    DP[i] = DP[i-2]+DP[i-1]
print(DP[N]%10007)