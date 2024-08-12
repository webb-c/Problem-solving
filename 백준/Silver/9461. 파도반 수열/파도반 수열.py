import sys

def get_p_list(N):
    DP = [1] * N
        
    for i in range(3, N):
        DP[i] = DP[i-2] + DP[i-3]
    
    return DP


def input():
    return sys.stdin.readline().rstrip()


def solve():
    T = int(input())
    max_N = 0
    N_list = []
    for _ in range(T):
        N = int(input())
        max_N = max(max_N, N)
        N_list.append(N)
    
    p_list = get_p_list(max_N)
    
    for i in range(T):
        print(p_list[N_list[i]-1])
    

if __name__ == "__main__":
    solve()
    