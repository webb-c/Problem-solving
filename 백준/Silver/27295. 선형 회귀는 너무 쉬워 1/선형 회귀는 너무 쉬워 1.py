import sys

def input():
    return sys.stdin.readline().rstrip()

def get_gcd(a, b):
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r

def main():
    n, b = map(int, input().split())
    xSum, ySum = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        xSum += x
        ySum += y
    if xSum == 0:
        print("EZPZ")
    else:
        ceil = ySum - n*b
        floor = xSum
        reminder = ceil % floor
        if reminder == 0:
            print(ceil // floor)
        else:
            gcd = get_gcd(ceil, floor)
            print(str(ceil//gcd)+"/"+str(floor//gcd))

if __name__ == "__main__":
    main()
