import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    for i in range(n):
        numList = list(map(int, input().split()))
        numList.sort()
        print("Scenario #"+str(i+1)+":")
        if numList[0]**2 + numList[1]**2 == numList[2]**2:
            print("yes")
        else:
            print("no")
        print()
        
if __name__ == "__main__":
    main()
