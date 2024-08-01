import sys

def get_longest_increasing_subsequence_length_via_dp(N, A):
    DP = [1] * N
    
    for i in range(1, N):
        entry = A[i]
        length = 0
        for j in range(i):
            if A[j] < entry: length = max(length, DP[j])
        
        DP[i] = length + 1
    
    return max(DP)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    print(get_longest_increasing_subsequence_length_via_dp(N, A))
    

if __name__ == "__main__":
    solve()
    