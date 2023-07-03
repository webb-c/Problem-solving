import sys

input = sys.stdin.readline
N = int(input())
coordinate = [list(map(int, input().split())) for _ in range(N)]
coordinate.append(coordinate[0])
area = 0
for i in range(N):
    area += coordinate[i][0] * coordinate[i + 1][1]
    area -= coordinate[i + 1][0] * coordinate[i][1]
result = round(area / 2, 1)
print(max(result, -1 * result))