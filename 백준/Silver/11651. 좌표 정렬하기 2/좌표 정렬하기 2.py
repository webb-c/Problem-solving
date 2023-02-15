import sys
input = sys.stdin.readline

N = int(input())
dotList = []
for _ in range(N):
    x, y = map(int, input().split())
    dotList.append([x, y])
dotList = sorted(dotList, key=lambda dot: dot[0])
dotList = sorted(dotList, key=lambda dot: dot[1])
for x, y in dotList:
    print(x, y)