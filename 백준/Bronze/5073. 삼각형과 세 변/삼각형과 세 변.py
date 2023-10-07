import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(numList):
    numList.sort()
    if numList[0]+numList[1] <= numList[2]:
        return "Invalid"
    if numList[0] == numList[1]:
        if numList[0] == numList[2]:
            return "Equilateral"
        else:
            return "Isosceles"
    elif numList[0] == numList[2]:
        return "Isosceles"
    elif numList[1] == numList[2]:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    while True:
        numList = list(map(int, input().split()))
        if numList[0] == 0:
            break
        print(solve(numList))

if __name__ == "__main__":
    main()
