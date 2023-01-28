inputStr = list(input())
dic = {}
for i in range(97, 123) : dic[chr(i)] = -1
for ch in inputStr :
    if dic[ch] == -1 : dic[ch] = inputStr.index(ch)
for count in dic.values() : print(count, end=" ")