import sys
from collections import deque
input = sys.stdin.readline

def run(queue, cmd, n):
    if cmd == 'push': queue.append(n)
    elif cmd == 'pop':
        if not queue : print(-1)
        else :
            m = queue.popleft()
            print(m)
    elif cmd == 'size': print(len(queue))
    elif cmd == 'empty':
        if queue : print(0)
        else : print(1)
    elif cmd == 'front':
        if not queue : print(-1)
        else : print(queue[0])
    elif cmd == 'back':
        if not queue : print(-1)
        else : print(queue[-1])

N = int(input())
queue = deque([])
for _ in range(N) :
    cmdList = list(input().split())
    if cmdList[0] == "push" : run(queue, cmdList[0], int(cmdList[1]))
    else: run(queue, cmdList[0], -1)