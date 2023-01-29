r = 31
M = 1234567891
int(input())
string = list(map(lambda x: ord(x)-96, list(input())))
hashVal = 0
for n, i in enumerate(string):
    hashVal += i*r**n
print(hashVal%M)