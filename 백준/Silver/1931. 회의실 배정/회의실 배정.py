import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nList = [list(map(int, input().split())) for _ in range(N)]
nList.sort()
nList.sort(key=lambda n : n[1])
queue = deque(nList)
answer = 1
endT = queue.popleft()[1]
while queue :
    s, e = queue.popleft()
    if endT <= s :
        answer += 1
        endT = e
print(answer)