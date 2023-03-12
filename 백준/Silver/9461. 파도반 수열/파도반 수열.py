import sys
input = sys.stdin.readline

T = int(input())
nList = [ int(input()) for _ in range(T)]
maxN = max(nList)
dp = [ 0 for _ in range(maxN) ]
if len(dp) < 2 : dp[0] = 1
if len(dp) < 3 : dp[0] = dp[1] = 1
if len(dp) < 4 : dp[0] = dp[1] = dp[2] = 1
if len(dp) >= 4 :
    dp[0] = dp[1] = dp[2] = 1
    for i in range(maxN-3):
        dp[i+3] = dp[i] + dp[i+1]

for n in nList :
    print(dp[n-1])