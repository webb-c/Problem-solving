import sys


def get_max_cost(N, cost_list):
    DP = [0] * (N+1)
    DP[1] = cost_list[0]
    
    for i in range(2, N+1):
        max_cost = cost_list[i-1]
        for j in range(i//2 + 1):
            max_cost = max(max_cost, DP[j]+DP[i-j])
            
        DP[i] = max_cost
    
    return DP[-1]


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    cost_list = list(map(int, input().split()))
    print(get_max_cost(N, cost_list))
    

if __name__ == "__main__":
    solve()
    