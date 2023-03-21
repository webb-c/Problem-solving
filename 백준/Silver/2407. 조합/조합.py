import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dn, dm = 1, 1
for i in range(m, 0, -1) :
    dn *= n-i+1
    dm *= i
print(dn//dm)