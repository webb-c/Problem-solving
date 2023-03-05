import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
answer = 0
caseList = [[0,0], [0,1], [1,0], [1,1]]
for n in range(N-1, -1, -1) :
    nr, nc = r//(2**n), c//(2**n)
    for idx, case in enumerate(caseList):
        if nr==case[0] and nc==case[1] :
            answer += idx*(2**(n))*(2**(n))
            break
    r, c = r%(2**n), c%(2**n)
print(answer)