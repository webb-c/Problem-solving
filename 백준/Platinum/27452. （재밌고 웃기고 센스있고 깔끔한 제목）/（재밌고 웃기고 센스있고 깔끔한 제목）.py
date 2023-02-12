import sys
input = sys.stdin.readline
def getChar(n, k):
    if k > lengthS[n-1] : return '0'
    elif k < 0 : return '('   # 줄인 값 이전
    elif k == lengthS[n-1] : return ')'
    elif k == 1 : return '('
    else :
        if k <= lengthS[n-3] + 1 : return getChar(n-2, k-1)
        else : return getChar(n-1, k-1-lengthS[n-3])

T = int(input())
TestList = []
lengthS = [2, 2]
limit = 85
maxN = 0
for _ in range(T):
    n, k = map(int, input().split())
    if n > maxN: maxN = n
    if n > limit:
        gap = n-limit
        n = n-gap//2*2
        k = k-gap//2
    TestList.append([n, k])
maxN = min(maxN, limit)
for i in range(2, maxN+1):
    lengthS.append(1 + lengthS[i-2] + lengthS[i-1] + 1)
for n, k in TestList :
    print(getChar(n, k))