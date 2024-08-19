import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(sorted(num_list)[K-1])

if __name__ == "__main__":
    solve()
    