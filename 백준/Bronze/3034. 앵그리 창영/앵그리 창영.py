import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, W, H = map(int, input().split())
    D = math.sqrt(W**2 + H**2)
    for _ in range(N):
        if int(input()) <= D:
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()
