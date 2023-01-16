# [Silver 5] 수 이어가기 - 2635 🌟
# 가능한 경우를 모두 테스트함 (생각보다 시간 안 걸림)
# 반례는 음수일때만 break이므로 같을 때(차가 0일때)도 고려해줘야 한다.

first = int(input())
second = 1
maxcount = 0
List = []
while second <= first :
    numList = [first, second]
    tempList = []
    count = 0
    ppre = first
    pre = second
    n = ppre - pre
    while n >= 0 :
        tempList.append(n)
        count+=1
        ppre = pre
        pre = n
        n = ppre - pre
    if count > maxcount :
        maxcount = count
        List = numList + tempList
    second+=1

print(maxcount+2)
for number in List :
    print(number, end=' ')