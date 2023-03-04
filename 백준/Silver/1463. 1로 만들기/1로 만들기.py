import sys
input = sys.stdin.readline

N = int(input())
DP = [0]*N
for i in range(1, N) :
    num = i+1
    DP[i] = DP[i-1] + 1 # 1을 뺀다.
    if num % 2 == 0 :
        DP[i] = min(DP[i], DP[(num//2)-1] + 1) # 2로 나눈다.
    if num % 3 == 0 :
        DP[i] = min(DP[i], DP[(num//3)-1] + 1) # 3으로 나눈다.
print(DP[N-1])