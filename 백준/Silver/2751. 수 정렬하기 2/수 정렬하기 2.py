import sys
input = sys.stdin.readline
N = int(input())
numList = [0 for _ in range(2000001)]
for _ in range(N) :
    idx = int(input()) + 1000000
    numList[idx] += 1
for idx, n in enumerate(numList) :
    if n != 0 : print(idx-1000000)