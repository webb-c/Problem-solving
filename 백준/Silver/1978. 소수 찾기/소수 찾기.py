N = int(input())
numList = list(map(int, input().split()))
count = 0
for i in range(2, max(numList)) :
    for idx, n in enumerate(numList) :
        if n == 1 : numList.pop(idx)
        elif n > i :
            remain = n % i
            if remain == 0 : numList.pop(idx)
        else : continue

print(len(numList))