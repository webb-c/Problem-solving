import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(n):
    isPrime = [False, False] + [True] * (n - 1)
    primeList = []
    for i in range(2, n+1):
        if isPrime[i]:
            primeList.append(i)
            for m in range(2*i, n+1, i):
                isPrime[m] = False
    return primeList

def solve(n):
    global primeList
    count = 0
    for p in primeList:
        if n < p <= 2*n:
            count += 1
    return count

def main():
    global primeList
    primeList = eratosthenes_sieve(2*123456)
    while True:
        n = int(input())
        if n == 0:
            break
        print(solve(n))

if __name__ == "__main__":
    main()
