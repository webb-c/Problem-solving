import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(n):
    isPrime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = False
    return isPrime

def solve(n):
    isPrime = eratosthenes_sieve(n)
    for i in range(math.ceil(n/2), 1, -1):
        if isPrime[i] and isPrime[n-i]:
            print(min(n-i, i), max(n-i, i))
            break

def main():
    global primeList
    T = int(input())
    for _ in range(T):
        n = int(input())
        solve(n)

if __name__ == "__main__":
    main()
