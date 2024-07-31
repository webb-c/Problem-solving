import sys

def get_max_wine(n, values):
    DP = [[0, 0, 0] for _ in range(n)] # DP[N][0]: N번쨰 와인을 안마심 / [N][1]: N번쨰 와신을 마심 / [N][2]: N-1번째 와인도 마심
    DP[0][0], DP[0][1] = 0, values[0]
    DP[1][0], DP[1][1], DP[1][2] = DP[0][1], values[1], DP[0][1] + values[1]
    
    for i in range(2, n):
        DP[i][0] = max(DP[i-1])
        DP[i][1] = max(DP[i-2]) + values[i]
        DP[i][2] = DP[i-1][1] + values[i]
        
    return max(DP[-1])


def input():
    return sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    values = [int(input()) for _ in range(n)]
    if n==1: print(values[0])
    elif n==2: print(values[0] + values[1])
    else:
        print(get_max_wine(n, values))


if __name__ == "__main__":
    solve()