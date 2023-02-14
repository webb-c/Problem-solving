import sys
input = sys.stdin.readline

def run(stack, cmd, n):
    if cmd == 'push': stack.append(n)
    elif cmd == 'pop':
        if not stack : print(-1)
        else :
            m = stack.pop()
            print(m)
    elif cmd == 'size': print(len(stack))
    elif cmd == 'empty':
        if stack : print(0)
        else : print(1)
    elif cmd == 'top':
        if not stack : print(-1)
        else : print(stack[-1])

N = int(input())
stack = []
for _ in range(N) :
    cmdList = list(input().split())
    if cmdList[0] == "push" : run(stack, cmdList[0], int(cmdList[1]))
    else: run(stack, cmdList[0], -1)