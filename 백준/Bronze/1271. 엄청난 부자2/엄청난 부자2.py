import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    print(n // m)
    print(n % m)

if __name__ == "__main__":
    main()
