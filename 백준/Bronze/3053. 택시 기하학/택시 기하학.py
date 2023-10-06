import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def main():
    R = int(input())
    uArea = math.pi*R*R
    tArea = 2*R*R
    print("{:.6f}".format(uArea))
    print("{:.6f}".format(tArea))

if __name__ == "__main__":
    main()
