import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] += line[j]

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()
