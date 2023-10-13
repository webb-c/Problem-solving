import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def main():
    L = int(input())
    print(math.sqrt(3)*L*L/4)

if __name__ == "__main__":
    main()
