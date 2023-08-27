import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    if N <= 2:
        print(4)
    elif N % 2 != 0:
        print(N+1)
    else:
        print(N)

if __name__ == "__main__":
    main()
