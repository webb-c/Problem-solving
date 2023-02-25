import sys
input = sys.stdin.readline

N = int(input())  #500,000
M = int(input())
notButton = input().split()

count = abs(100 - N)
for num in range(1000001):
    num = str(num)
    for i, ni in enumerate(num) :
        if ni in notButton : break
        elif i == len(num)-1 : count = min(count, len(num) + abs(int(num) - N))
print(count)