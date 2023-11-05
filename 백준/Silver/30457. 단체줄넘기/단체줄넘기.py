import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip()

def D():
    N = int(input())
    heightList = list(map(int, input().split()))
    heightCount = Counter(heightList)
    result = 0
    for count in heightCount:
        if heightCount[count] < 3:
            result += heightCount[count]
        else:
            result += 2
    print(result)

if __name__ == "__main__":
    D()
