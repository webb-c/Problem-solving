import sys
sys.setrecursionlimit(10**6)

def get_hit_binary(N):
    prev_0, prev_1 = 0, 1
    
    for n in range(2, N+1):
        new_0 = prev_0 + prev_1
        new_1 = prev_0
        
        prev_0, prev_1 = new_0, new_1
    
    return prev_0 + prev_1


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(get_hit_binary(N))


if __name__ == "__main__":
    solve()