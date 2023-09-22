import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def is_prime(n):
    isPrime = True
    for p in range(2, math.floor(math.sqrt(n))+1):
        if n % p == 0:
            isPrime = False
            break
    return isPrime

def solve(n):
    result = n
    if n <= 2:
        return 2
    if n % 2 == 0:
        result += 1
    while True:
        if is_prime(result):
            return result
        result += 2

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solve(n))

if __name__ == "__main__":
    main()
