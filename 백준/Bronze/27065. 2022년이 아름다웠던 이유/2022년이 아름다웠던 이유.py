import sys

def input():
    return sys.stdin.readline().rstrip()

def find_divisors(n):
    divisors = set()
    if n == 1:
        return [0]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i == 1:
                continue
            divisors.add(n//i)
    return sorted(list(divisors))

def solve(n):
    divisors = find_divisors(n)
    divSum = sum(divisors)
    if divSum > n:
        for div in divisors:
            div_divisors = find_divisors(div)
            div_divSum = sum(div_divisors)
            if div_divSum > div:
                return "BOJ 2022"
        return "Good Bye"
    else:
        return "BOJ 2022"

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solve(n))

if __name__ == "__main__":
    main()
