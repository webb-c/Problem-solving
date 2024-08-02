import sys

def get_continuous_sum(n, num_list):
    DP = [0] * n
    DP[0] = num_list[0]
    
    for i in range(1, n):
        DP[i] = max(DP[i-1]+num_list[i], num_list[i])
        
    return max(DP)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    num_list = list(map(int, input().split()))
    
    print(get_continuous_sum(n, num_list))
    


if __name__ == "__main__":
    solve()
    