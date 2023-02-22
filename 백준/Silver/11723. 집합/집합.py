import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M) :
    # parse
    cmdline = input().split()
    cmd = cmdline[0]
    if len(cmdline) == 1:
        if cmd == 'all':
            S = set([i + 1 for i in range(20)])
        else:
            S = set()
    else :
        x = int(cmdline[1])
        if cmd == 'add' : S.add(x)
        elif cmd == 'remove' : S.discard(x)
        elif cmd == 'check' :
            if x in S : print(1)
            else : print(0)
        elif cmd == 'toggle' :
            if x in S : S.remove(x)
            else : S.add(x)