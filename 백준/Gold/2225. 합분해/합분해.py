import sys


def get_num_of_cases(N, K):
    DP = [[1 for i in range(N)] for j in range(K)]

    for i in range(1, K):
        for j in range(N):
            DP[i][j] = (DP[i][j-1] + DP[i-1][j]) % 1000000000

    return DP[-1][-1]


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N, K = map(int, input().split())
    print(get_num_of_cases(N, K))
    

if __name__ == "__main__":
    solve()
    