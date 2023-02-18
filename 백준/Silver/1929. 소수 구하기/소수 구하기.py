import math
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
numList = [True for i in range(N+1)]
numList[0] = numList[1] = False

for i in range(2, int(math.sqrt(N)) + 1) :
    if numList[i] == True :
        j = 2
        while i*j <= N :
            numList[i*j] = False
            j += 1

for i in range(M, N+1) :
    if numList[i] : print(i)