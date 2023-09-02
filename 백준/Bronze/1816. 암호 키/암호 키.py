import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(num):
    result = "YES"
    i = 2
    while i <= 1000000:
        if num % i == 0:
            result = "NO"
            break
        i += 1
    return result

def main():
    T = int(input())
    for _ in range(T):
        num = int(input())
        print(solve(num))

if __name__ == "__main__":
    main()
