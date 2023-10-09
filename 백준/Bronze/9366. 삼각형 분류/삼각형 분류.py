import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    T = int(input())
    for _ in range(T):
        result = ""
        a, b, c = map(int, input().split())
        if a == b == c:
            result = "equilateral"
        elif a == b or b == c or a == c:
            result = "isosceles"
        else:
            result = "scalene"
        numList = [a, b, c]
        numList.sort()
        if numList[0]+numList[1] <= numList[2]:
            result = "invalid!"
        print("Case #{}: {}".format(_+1, result))

if __name__ == "__main__":
    main()
