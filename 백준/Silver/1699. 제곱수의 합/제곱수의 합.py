import sys

def get_square_sum(N):
    DP = [1000001] * (N+1)
    DP[0], DP[1] = 0, 1
        
    for i in range(2, N+1):
        if i**(0.5) % 1 == 0:
            DP[i] = 1
        else:
            for j in range(0, int((i//2)**0.5)+1):
                DP[i] = min(DP[i] , 1 + DP[i-(j*j)])
        
    return DP[-1]


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    print(get_square_sum(N))
    

if __name__ == "__main__":
    solve()
    