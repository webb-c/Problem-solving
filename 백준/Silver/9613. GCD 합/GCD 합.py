import sys
import itertools

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def main():
    T = int(input())
    for _ in range(T):
        nList = list(map(int, input().split()))[1:]
        gcdSum = 0
        for a, b in list(itertools.combinations(nList, 2)):
            gcdSum += get_gcd(a, b)
        print(gcdSum)

if __name__ == "__main__":
    main()
