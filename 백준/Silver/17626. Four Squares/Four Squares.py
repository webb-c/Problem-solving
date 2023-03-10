import sys
input = sys.stdin.readline

n = int(input())
dp = [ i for i in range(n+1) ]
for i in range(1, n+1):
    for j in range(1, int(i**0.5)+1):
        # 자연수 i를 표현하는데 사용 되는 제곱수는 j에 대한 제곱수를 대신 쓴 것과 비교하여 계산할 수 있다. 
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])