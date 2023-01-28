ABC = str(int(input())*int(input())*int(input()))
countList = [0 for _ in range(10)]
for n in ABC : countList[int(n)] += 1
for c in countList : print(c)