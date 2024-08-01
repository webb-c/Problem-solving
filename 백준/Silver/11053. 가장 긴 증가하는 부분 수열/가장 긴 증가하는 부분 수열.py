import sys
from bisect import bisect_left

def get_longest_increasing_subsequence_length_via_binary_search(N, A):
    LIS = [A[0]]
    
    for i in range(1, N):
        entry = A[i]
        if entry > LIS[-1]: 
            LIS.append(entry)
        else:
            LIS[bisect_left(LIS, entry)] = entry
            
    return len(LIS)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    print(get_longest_increasing_subsequence_length_via_binary_search(N, A))
    

if __name__ == "__main__":
    solve()
    