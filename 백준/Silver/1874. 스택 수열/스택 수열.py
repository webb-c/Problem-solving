import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N) : array.append(int(input()))
# 43/6/87/5/21
order = []
stack = deque([])
idx = 0
for n in range(1, N+1) :
    stack.append(n)
    order.append('+')
    while True :
        if stack and array[idx] == stack[-1] :
            stack.pop()
            idx += 1
            order.append('-')
        else : break

if stack : print('NO')
else :
    for op in order :
        print(op)