import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def main():
    numList = []
    try:
        while True:
            line = input()
            if not line:
                break
            line = list(map(int, line.split()))
            numList += line
    except EOFError:
        pass

    gcd = 0
    for a, b in list(combinations(numList, 2)):
        temp = get_gcd(a, b)
        gcd = max(temp, gcd)

    print(gcd)


if __name__ == "__main__":
    main()
