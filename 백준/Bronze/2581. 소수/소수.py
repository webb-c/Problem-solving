import sys

def input():
    return sys.stdin.readline().rstrip()

def is_prime(n):
    isPrime = True
    if n < 2:
        isPrime = False
    else:
        for p in range(2, n):
            if n % p == 0:
                isPrime = False
    return isPrime

def main():
    M = int(input())
    N = int(input())
    sumVal = 0
    minVal = float("inf")
    for n in range(M, N+1):
        if is_prime(n):
            sumVal += n
            minVal = min(minVal, n)
    if sumVal == 0:
        print("-1")
    else:
        print(sumVal)
        print(minVal)

if __name__ == "__main__":
    main()
