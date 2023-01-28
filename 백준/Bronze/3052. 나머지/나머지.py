numList = []
for _ in range(10) :
    reminder = int(input())%42
    if reminder not in numList : numList.append(reminder)
print(len(numList))