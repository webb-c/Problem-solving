import sys
input = sys.stdin.readline

N = int(input())
sizeList = []
orderList = []
for _ in range(N):
    x, y = map(int, input().split())
    sizeList.append((x, y))
for n in sizeList:
    count = 0
    for m in sizeList :
        if m[0] > n[0] and m[1] > n[1] : count+=1
    orderList.append(str(count+1))

print(' '.join(orderList))