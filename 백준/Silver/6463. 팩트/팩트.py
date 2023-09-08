import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(numList):
    resultList = [1]*len(numList)
    maxNum = max(numList)
    n = 0
    fact = 1
    for N in range(0, maxNum+1):
        if N != 0:
            fact *= n
        if N in numList:
            idx = numList.index(N)
            result = fact
            while True:
                remind = result % 10
                if remind:
                    break
                result //= 10
            resultList[idx] = str(result)[-1]
        n += 1
    return resultList

def main():
    numList = []
    while True:
        try:
            N = int(input())
            numList.append(N)
        except:
            break
    resultList = solve(numList)
    for i in range(len(numList)):
        print(f"{numList[i]:5} -> {resultList[i]}")

if __name__ == "__main__":
    main()
