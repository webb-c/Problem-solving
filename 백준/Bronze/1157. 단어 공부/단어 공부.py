string = input().upper()
numList = {}
for ch in string :
    if ch not in numList :
        numList[ch] = 1
    else :
        numList[ch] += 1

valueList = list(numList.values())
valueList.sort(reverse=True)
if len(valueList) > 1 and valueList[0] == valueList[1] : print("?")
else :
    for k, v in numList.items() :
        if v == valueList[0] :
            print(k)
            break