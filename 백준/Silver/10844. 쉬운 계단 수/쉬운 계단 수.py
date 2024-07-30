import sys

sys.setrecursionlimit(10**6)
MOD = 1000000000

def get_step(N):
    # DP 배열 대신 두 행만 유지 (메모리 개선)
    prev_dp = [0] * 10
    curr_dp = [0] * 10
    
    for i in range(1, 10):
        prev_dp[i] = 1
    
    for n in range(2, N + 1):
        curr_dp = [0] * 10  
        for i in range(10):
            if i > 0:
                curr_dp[i - 1] = (curr_dp[i - 1] + prev_dp[i]) % MOD
            if i < 9:
                curr_dp[i + 1] = (curr_dp[i + 1] + prev_dp[i]) % MOD
        prev_dp = curr_dp  
    
    return sum(prev_dp) % MOD


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    if N == 1:
        print(9)  # 길이가 1인 경우 계단 수는 1~9까지 9개
    else:
        print(get_step(N))
    
    
if __name__ == "__main__":
    solve()