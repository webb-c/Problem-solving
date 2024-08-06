import sys

def get_tile_number_of_cases(N):
    if N % 2 == 1:
        return 0
    DP = [1] * N
    DP[1] = 3
        
    for i in range(3, N, 2):
        DP[i] = DP[i-2]*3 + 2
        for k in range(4, i, 2):
            DP[i] += DP[i-k]*2
        
    return DP[N-1]


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    print(get_tile_number_of_cases(N))
    

if __name__ == "__main__":
    solve()
    