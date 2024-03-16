import sys


def input():
    return sys.stdin.readline().rstrip()

def solve():
    N = int(input())
    num_lst = [int(input()) for _ in range(N)]
    num_lst.sort(reverse=True)
    for n in num_lst:
        print(n)

if __name__ == "__main__":
    solve()
