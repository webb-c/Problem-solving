import sys

def input():
    return sys.stdin.readline().rstrip()

def get_common_divisors(N, numList):
    divisorList = set()
    minNum = min(numList)
    for i in range(1, minNum+1):
        count = 0
        for n in numList:
            if n % i == 0:
                count += 1
            if count == N:
                divisorList.add(i)
    return sorted(list(divisorList))

def main():
    N = int(input())
    numList = list(map(int, input().split()))
    result = get_common_divisors(N, numList)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()
