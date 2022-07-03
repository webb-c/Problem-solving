n = int(input())
numList = []
for i in range(n) :
  item = int(input())
  numList.append(item)

numList.sort()
for i in numList :
  print(i)