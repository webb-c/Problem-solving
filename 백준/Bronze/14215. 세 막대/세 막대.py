import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    numList = list(map(int, input().split()))
    numList.sort()
    if numList[0]+numList[1] <= numList[2]:
        print(numList[0]+numList[1]+numList[0]+numList[1]-1)
    else:
        print(sum(numList))

if __name__ == "__main__":
    main()
