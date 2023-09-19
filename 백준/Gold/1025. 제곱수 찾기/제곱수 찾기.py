import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def check(n):
    if int(math.sqrt(n)) ** 2 == n:
        return True
    return False

def main():
    N, M = map(int, input().split())
    table = []
    cantList = [2, 3, 7, 8]
    flag = True
    for _ in range(N):
        numList = list(map(int, list(input())))
        if flag:
            for n in numList:
                if n not in cantList:
                    flag = False
                    break
        table.append(numList)
    if flag:
        print(-1)
        return

    maxNum = -1
    for i in range(N):
        for j in range(M):
            for ii in range(-N, N):
                for jj in range(-M, M):
                    ni, nj = i, j
                    tempNum = 0
                    while 0 <= ni < N and 0 <= nj < M:
                        tempNum = tempNum*10 + table[ni][nj]
                        if tempNum > maxNum and check(tempNum):
                            maxNum = tempNum
                        if ii == 0 and jj == 0:
                            break
                        ni, nj = ni+ii, nj+jj
    print(maxNum)

if __name__ == "__main__":
    main()
