score = []
idxList = []
for i in range(8):
  item = int(input())
  score.append(item)

sum = 0
for i in range(5) :
  num = max(score)
  index = score.index(num)
  sum = sum + num
  score[index] = 0
  idxList.append(index+1)

idxList.sort()
print(sum)
print(idxList[0], idxList[1], idxList[2], idxList[3], idxList[4])