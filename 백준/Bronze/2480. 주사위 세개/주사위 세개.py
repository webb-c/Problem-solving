a, b, c = map(int, input().split())
maxNum = max([a, b, c])

if a == b == c :
    print(10000+a*1000)
elif a != b and a != c and b != c :
    print(maxNum*100)
else :
    if a == b :
        same = a
    elif a == c :
        same = a
    elif b == c :
        same = b
    print(1000+same*100)