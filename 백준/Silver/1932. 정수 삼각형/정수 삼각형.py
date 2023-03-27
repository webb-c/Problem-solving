import sys
input = sys.stdin.readline

N = int(input())
triangle = [ list(map(int, input().split())) for _ in range(N) ]
L = 2
for i in range(1, N) :
    for j in range(L) :
        if j == 0 : triangle[i][j] = triangle[i][j] + triangle[i-1][j] # 제일 왼쪽
        elif i == j : triangle[i][j] = triangle[i][j] + triangle[i-1][j-1] #제일 오른쪽
        else :
            triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j] # 2가지 case중에서 더 큰 값
    L += 1
print(max(triangle[-1]))