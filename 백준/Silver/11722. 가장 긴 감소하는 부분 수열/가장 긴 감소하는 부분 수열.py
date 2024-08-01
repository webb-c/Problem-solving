import sys

def bisect_left_desc(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def get_longest_decreasing_subsequence_length_via_dp(N, A):
    DP = [1] * N
    
    for i in range(1, N):
        entry = A[i]
        max_length = 0
        for j in range(i):
            if A[j] > entry: max_length = max(max_length, DP[j])
        
        DP[i] = max_length + 1
    
    return max(DP)


def get_longest_decreasing_subsequence_length_via_binary_search(N, A):
    LIS = [A[0]]
    
    for i in range(1, N):
        entry = A[i]
        if entry < LIS[-1]: 
            LIS.append(entry)
        else:
            LIS[bisect_left_desc(LIS, entry)] = entry
            
    return len(LIS)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    print(get_longest_decreasing_subsequence_length_via_binary_search(N, A))
    


if __name__ == "__main__":
    solve()
    