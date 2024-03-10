import sys

def input():
    return sys.stdin.readline().rstrip()

def verify(n):
    # odd: 제곱수 ### 부동소수점 오류 잡기
    if n == (int(n**0.5)**2):
        return 1
    else:
        return 0


def solve():
    N = int(input())
    X = list(map(int, input().split()))
    for n in X:
        print(verify(n), end=" ")


if __name__ == "__main__":
    solve()

