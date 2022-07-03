strList1 = input().split()
strList2 = input().split()
Lotte = list(map(int, strList1))
LG = list(map(int, strList2))
winning = False
fire = False
Lose = False

my_score = 0
other_score = 0

for i in range(9):
  my_score = my_score + Lotte[i]
  if (my_score > other_score):
    winning  = True
  other_score = other_score + LG[i]
  if ((my_score<other_score) and winning):
    fire = True

if (my_score<other_score) :
  Lose = True

if (Lose and fire) :
  print("Yes")
else :
  print("No")