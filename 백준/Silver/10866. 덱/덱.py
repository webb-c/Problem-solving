import sys
from collections import deque
input = sys.stdin.readline

def run(deq, cmd, n):
    if cmd == 'push_front': deq.appendleft(n)
    elif cmd == 'push_back': deq.append(n)
    elif cmd == 'pop_front':
        if not deq : print(-1)
        else :
            m = deq.popleft()
            print(m)
    elif cmd == 'pop_back':
        if not deq : print(-1)
        else :
            m = deq.pop()
            print(m)
    elif cmd == 'size': print(len(deq))
    elif cmd == 'empty':
        if deq : print(0)
        else : print(1)
    elif cmd == 'front':
        if not deq : print(-1)
        else : print(deq[0])
    elif cmd == 'back':
        if not deq : print(-1)
        else : print(deq[-1])

N = int(input())
deq = deque([])
for _ in range(N) :
    cmdList = list(input().split())
    if cmdList[0] == "push_front" or cmdList[0] == "push_back" : run(deq, cmdList[0], int(cmdList[1]))
    else: run(deq, cmdList[0], -1)