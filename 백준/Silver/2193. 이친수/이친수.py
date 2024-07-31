import sys
sys.setrecursionlimit(10**6)

def get_hit_binary(N):
    prev_info = [0, 1] # init
    
    for n in range(2, N+1):
        curr_info = [0, 0]
        
        curr_info[0] = prev_info[0] + prev_info[1]
        curr_info[1] = prev_info[0]
            
        prev_info, curr_info = curr_info, prev_info 
    
    return sum(prev_info)


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