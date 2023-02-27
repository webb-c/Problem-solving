import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
realNum = list(map(int, input().split()))
realNum.sort()
print(realNum[0]*realNum[-1])