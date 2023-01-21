# [Bronze 1] 반복

string = input()
chList = []
count = 1
pre = 'A'
for s in string:
    if s <= pre :
        count = count+1
    pre = s
print(count)