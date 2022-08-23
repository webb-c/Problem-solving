numList = list(map(int, input().split()))
needList = [1, 1, 2, 2, 2, 8]
resultList = []

for a, b in zip(numList, needList):
    resultList.append(b-a)

for i in resultList :
    print(i, end=" ")