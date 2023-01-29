N = int(input())
beeNum = path = 1
while N > beeNum :
    beeNum += path*6
    path += 1
print(path)