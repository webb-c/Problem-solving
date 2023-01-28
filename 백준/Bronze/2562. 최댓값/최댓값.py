maxNum = maxIdx = 0
for i in range(9):
    num = int(input())
    if maxNum < num :
        maxNum = num
        maxIdx = i+1
print(maxNum)
print(maxIdx)