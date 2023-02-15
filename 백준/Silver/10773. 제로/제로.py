import sys
from collections import deque
input = sys.stdin.readline

numList = deque([])
K = int(input())
for _ in range(K) :
    n = int(input())
    if n == 0 : numList.pop()
    else :
        numList.append(n)
print(sum(numList))