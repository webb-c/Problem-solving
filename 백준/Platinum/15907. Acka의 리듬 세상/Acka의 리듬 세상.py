import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(n):
    isPrime = [True] * (n+1)
    primeList = []
    for i in range(2, n+1):
        if isPrime[i]:
            primeList.append(i)
        for j in range(len(primeList)):
            if i * primeList[j] > n:
                break
            isPrime[i * primeList[j]] = False
            if i % primeList[j] == 0:
                break
    return primeList

def main():
    N = int(input())
    tapList = list(map(int, input().split()))
    primeList = eratosthenes_sieve(2000000)
    count = [0] * (2000002)
    result = 0

    for k in primeList:
        for i in range(N):
            count[tapList[i] % k] += 1
            result = max(result, count[tapList[i] % k])
        for i in range(N):
            count[tapList[i] % k] -= 1

    print(result)

if __name__ == "__main__":
    main()
