import sys


def input():
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    num_list = [int(input()) for _ in range(N)]
    num_list.sort()
    
    for i in range(N):
        print(num_list[i])
    

if __name__ == "__main__":
    solve()
    