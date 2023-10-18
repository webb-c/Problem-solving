import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    M, K = map(int, input().split())
    B = []
    for _ in range(M):
        B.append(list(map(int, input().split())))
    result = [[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for k in range(M):
                result[i][j] += A[i][k]*B[k][j]
    for i in range(N):
        for j in range(K):
            print(result[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
