import sys
input = sys.stdin.readline
numberList = [False for _ in range(30)]
for _ in range(28) :
    n = int(input())
    numberList[n-1] = True
for number, tf in enumerate(numberList) :
    if not tf :
        print(number+1)