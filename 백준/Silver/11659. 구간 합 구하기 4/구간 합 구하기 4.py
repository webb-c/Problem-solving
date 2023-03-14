import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
sumList = [0]*(N+1)
for i in range(N) :
    sumList[i+1] = sumList[i]+numList[i]
for _ in range(M) :
    i, j = map(int, input().split())
    print(sumList[j]-sumList[i-1])