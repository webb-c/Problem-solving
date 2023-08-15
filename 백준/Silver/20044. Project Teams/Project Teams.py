import sys

def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    valueList = sorted(map(int, input().split()))
    left, right = 0, 2*n-1
    minValue = valueList[left] + valueList[right]
    for i in range(1, n):
        minValue = min(minValue, valueList[left+i] + valueList[right-i])
    print(minValue)

if __name__ == "__main__":
    main()
