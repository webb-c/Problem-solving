import sys
input = sys.stdin.readline

N, M = map(int, input().split())
notListen = set()
notSeen = set()
for _ in range(N) : notListen.add(input().rstrip())
for _ in range(M) : notSeen.add(input().rstrip())
notLS = sorted(list(notListen & notSeen))

print(len(notLS))
for name in notLS : print(name)