import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def solve(numList):
    abc = ["a", "b", "c"]
    idx = numList.index(-1)
    numList.pop(idx)
    if idx == 2:
        result = math.sqrt(numList[0]**2 + numList[1]**2)
    else:
        if numList[1]**2 - numList[0]**2 <= 0:
            print("Impossible.")
            return
        result = math.sqrt(numList[1]**2 - numList[0]**2)
    print("{} = {:.3f}".format(abc[idx], result))

def main():
    i = 0
    while True:
        i += 1
        numList = list(map(int, input().split()))
        if numList[0] == 0:
            break
        print(f"Triangle #{i}")
        solve(numList)
        print()
        
if __name__ == "__main__":
    main()
