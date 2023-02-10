import sys
input = sys.stdin.readline

N = int(input())
dotList = [0 for _ in range(N)]
for i in range(N) :
    x, y = map(int, input().split())
    dotList[i] = [x,y]
dotList=sorted(dotList)
for idx in range(N) :
    print(dotList[idx][0], dotList[idx][1])