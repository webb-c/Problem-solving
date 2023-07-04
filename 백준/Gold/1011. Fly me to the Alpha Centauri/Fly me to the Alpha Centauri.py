import sys
import math

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    k = 1
    while True:
        if k % 2 == 0:
            maxDist = (k / 2) ** 2 + (k / 2)
        else:
            maxDist = (math.ceil(k / 2)) ** 2
        if maxDist >= d:
            print(k)
            break
        k += 1
