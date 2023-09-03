import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    binary = list(map(int, list(input())))
    K = int(input())
    if sum(binary[N-K:]) != 0:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
