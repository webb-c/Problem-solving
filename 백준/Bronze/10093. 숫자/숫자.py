import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    nums = list(map(int, input().split()))
    A = min(nums)
    B = max(nums)
    if A == B:
        print(0)
    else:
        print(B-A-1)
    for i in range(A+1, B):
        print(i, end=" ")

if __name__ == "__main__":
    solve()
