import sys
sys.setrecursionlimit(10**6)

MOD = 10007

def get_asc(N):
    prev_dp = [0] * 10
    curr_dp = [0] * 10
    
    for i in range(10):
        prev_dp[i] = 1
    
    for n in range(2, N+1):
        for i in range(10):
            curr_dp[i] = 0 
        
        for i in range(10): # 0, 1, ..., 9
            for j in range(i, 10): # i, ..., 9
                curr_dp[j] = (curr_dp[j] + prev_dp[i]) % MOD
            
        prev_dp, curr_dp = curr_dp, prev_dp 
    
    return sum(prev_dp) % MOD


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    if N == 1:
        print(10)
    else:
        print(get_asc(N))


if __name__ == "__main__":
    solve()