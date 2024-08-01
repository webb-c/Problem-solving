import sys

def get_longest_bitonic_subsequence_length_via_dp(N, A):
    DP = [[1, 1] for _ in range(N)]
    answer = 1
    
    for i in range(1, N):
        entry = A[i]
        max_length_asc, max_length_desc = 0, 0
        for j in range(i):
            if A[j] < entry: 
                max_length_asc = max(max_length_asc, DP[j][0])
            elif A[j] > entry:
                max_length_desc = max(max_length_desc, DP[j][0], DP[j][1])
        
        DP[i][0], DP[i][1] = max_length_asc+1, max_length_desc+1
        answer = max(answer, max_length_asc+1, max_length_desc+1)
    
    return answer


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    print(get_longest_bitonic_subsequence_length_via_dp(N, A))
    


if __name__ == "__main__":
    solve()
    