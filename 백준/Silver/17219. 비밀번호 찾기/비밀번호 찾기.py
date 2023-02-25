import sys
input = sys.stdin.readline

domainDic = {}
N, M = map(int, input().split())
for _ in range(N):
    domain, pwd = input().split()
    domainDic[domain] = pwd
for _ in range(M) :
    print(domainDic[input().rstrip()])