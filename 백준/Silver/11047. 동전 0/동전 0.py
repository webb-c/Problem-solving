import sys
input = sys.stdin.readline

N, K = map(int, input().split())
vList = [int(input()) for _ in range(N)]
count = 0
for v in reversed(vList) :
    count += K//v
    K = K%v
    if K == 0 : break
print(count)
