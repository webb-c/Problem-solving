import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def main():
    D, H, W = map(int, input().split())
    # H**2 * x**2 + W**2 * x**2 = D**2
    # (H**2 + W**2) * x**2 = D**2
    x = (D ** 2 / (H**2 + W**2))**0.5
    Hx = math.trunc(H*x)
    Wx = math.trunc(W*x)
    print(Hx, Wx)

if __name__ == "__main__":
    main()
