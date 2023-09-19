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
    table = [input() for _ in range(N)]
    maxNum = -1
    for i in range(N):
        for j in range(M):
            for ii in range(-N, N):
                for jj in range(-M, M):
                    ni, nj = i, j
                    tempNum = ""
                    while 0 <= ni < N and 0 <= nj < M:
                        tempNum += table[ni][nj]
                        tempNum_int = int(tempNum)
                        if tempNum_int > maxNum and check(tempNum_int):
                            maxNum = tempNum_int
                        if ii == 0 and jj == 0:
                            break
                        ni, nj = ni+ii, nj+jj
    print(maxNum)

if __name__ == "__main__":
    main()
