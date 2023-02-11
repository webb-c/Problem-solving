import sys
from collections import deque

input = sys.stdin.readline

answer = []
order = "<"
N, K = map(int, input().split())
queue = deque([ i for i in range(1, N+1) ])

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

for i in range(len(answer)-1):
    order += str(answer[i])+", "
order += str(answer[-1])+">"

print(order)