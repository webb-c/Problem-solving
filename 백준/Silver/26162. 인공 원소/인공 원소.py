import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(n):
    isPrime = [False, False] + [True] * (n - 1)  # 0과 1은 소수가 아님
    primeList = []
    for i in range(2, n+1):
        if isPrime[i]:
            primeList.append(i)
            for m in range(2*i, n+1, i):  # multiple
                isPrime[m] = False
    return primeList

def solve(a):
    global primeList
    for p in primeList:
        if p >= a:
            return "No"
        if (a - p) in primeList:
            return "Yes"
    return "No"

def main():
    global primeList
    primeList = eratosthenes_sieve(118)
    N = int(input())
    for _ in range(N):
        a = int(input())
        print(solve(a))

if __name__ == "__main__":
    main()
