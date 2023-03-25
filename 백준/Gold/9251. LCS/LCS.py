import sys
input = sys.stdin.readline

strA = list(input().rstrip())
strB = list(input().rstrip())
DP = [[0]*(len(strB)+1) for _ in range(len(strA)+1)]

for i, a in enumerate(strA) :
    for j, b in enumerate(strB) :
        if a == b :
            DP[i-1][j-1] = DP[i-2][j-2] + 1
        else :
            DP[i-1][j-1] = max(DP[i-1][j-2], DP[i-2][j-1])

print(max(max(DP)))