from collections import deque

N = int(input())
queue = deque([ i+1 for i in range(N)])
while len(queue) > 2 :
    queue.popleft()
    n = queue.popleft()
    queue.append(n)
print(queue.pop())