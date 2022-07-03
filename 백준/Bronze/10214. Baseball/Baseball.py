case = int(input())
str = "Draw"
for _ in range(case):
  y_total = 0
  k_total = 0
  for __ in range(9):
    y, k = input().split()
    y = int(y)
    k = int(k)
    y_total += y
    k_total += k
  if y_total > k_total :
    str = "Yonsei"
  elif k_total > y_total :
    str = "Korea"
  else :
    str = "Draw"
  print(str)