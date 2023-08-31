import sys

def input():
    return sys.stdin.readline().rstrip()

def find_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i == 1:
                continue
            divisors.add(n//i)
    return sorted(list(divisors))

def solve(n):
    divSum = sum(find_divisors(n))
    if divSum < n or n == 1:
        result = "Deficient"
    elif divSum == n:
        result = "Perfect"
    else:
        result = "Abundant"
    return result

def main():
    T = int(input())
    testList = list(map(int, input().split()))
    for n in testList:
        print(solve(n))

if __name__ == "__main__":
    main()
