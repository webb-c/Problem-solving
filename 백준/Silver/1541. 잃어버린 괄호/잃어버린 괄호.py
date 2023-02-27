import sys
input = sys.stdin.readline

Formular = input().rstrip().split("-")
newFormular = []
for n in Formular :
    if n.isdigit() :
        newFormular.append(int(n))
    else :
        subFormular = n.split("+")
        temp = 0
        for nn in subFormular :
            temp += int(nn)
        newFormular.append(temp)

result = newFormular[0]
for n in newFormular[1:] :
    result -= n
print(result)