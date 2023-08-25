import sys

def input():
    return sys.stdin.readline().rstrip()

def find_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(list(divisors))

def solve(n):
    primeList = find_divisors(n)
    primeList.pop()
    primeSum = sum(primeList)
    if primeSum == n:
        equation = ""
        for p in primeList:
            equation += str(p)
            if p != primeList[-1]:
                equation += " + "
        print(n, "=", equation)
    else:
        print(n, "is NOT perfect.")

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        solve(n)

if __name__ == "__main__":
    main()
