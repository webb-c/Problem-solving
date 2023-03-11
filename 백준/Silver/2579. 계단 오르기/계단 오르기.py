import sys
input = sys.stdin.readline

n = int(input())
score = [ int(input()) for _ in range(n) ]
dp = [ 0 for i in range(n) ]
dp[0] = score[0]
if 2 <= n : dp[1] = score[0] + score[1]
for i in range(2, n):
    dp[i] = max(dp[i-2], dp[i-3]+score[i-1]) + score[i] # 이전이전(+현재) or 이전이전이전+(이전+현재)
print(dp[n-1])