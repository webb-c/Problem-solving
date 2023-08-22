import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxVal = float('-inf')

    for perm in permutations(A):
        value = sum(abs(perm[i] - perm[i+1]) for i in range(N-1))
        maxVal = max(maxVal, value)

    print(maxVal)


if __name__ == "__main__":
    main()
