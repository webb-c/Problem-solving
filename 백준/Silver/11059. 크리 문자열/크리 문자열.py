# [Silver] 크리 문자열 - 11059
S = input()
length = len(S)
table = []
for i in range(length) :
    table.append([])
    for j in range(length):
        if i==j : table[i].append(int(S[i]))
        else :
            table[i].append(0)

maxLength = 0
for L in range(1, length+length%2):
    for i in range(length):
        if i+L > length-1 : continue
        j = i+L
        partition = i+int((j-i)/2)
        if table[i][partition] == table[partition+1][j] and (L+1)%2==0:
            if maxLength < j-i+1 : maxLength = j-i+1
            table[i][j] = 2*table[i][partition]
        else :
            table[i][j] = table[i][partition] + table[partition+1][j]

print(maxLength)