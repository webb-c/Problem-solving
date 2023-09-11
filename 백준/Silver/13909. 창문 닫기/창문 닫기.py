import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(n):
    result = 0
    for i in range(1, int(n**0.5)+1):
        if i*i <= n:
            result += 1
    return result

def main():
    N = int(input())
    print(solve(N))


if __name__ == "__main__":
    main()
