# [Silver 1] 달력 - 20207
# 작업 스케쥴링 류 문제...?

# 입력
N = int(input())
doList = []
for _ in range(N) :
    doList.append(list(map(int, input().split())))

# 정렬
sortDoList = sorted(doList, key=lambda d: d[1], reverse=True) # 종료 날짜가 느린 것부터 정렬 (=정렬 안정성을 이용, 긴 일정나열을 위해)
sortDoList = sorted(sortDoList, key=lambda d: d[0]) # 시작 날짜가 빠른 것부터 정렬

# 배정
coverList = [] # 면적 ...
oneList = []  # 시작 날짜, 종료 날짜
lastDay = 0
for do in sortDoList :
    lastDay = 0
    if len(oneList) == 0 : # 기계 초기화
        oneList.append([do[0], do[1]])
        lastDay = do[1]
    else :
        index = -1
        conflict = False
        for idx, one in enumerate(oneList) :
            if index == -1 :
                if do[0] <= one[1] :
                    conflict = True
                else :
                    conflict = False
                    index = idx
            if lastDay < one[1] :
                lastDay = one[1]
        # 충돌이 발생할 때
        if conflict :
            oneList.append([do[0], do[1]])
        else :
            oneList[index][1] = do[1]
        # 연속 일정 아닐때
        if lastDay+1 < do[0] :
            coverList.append((lastDay - oneList[0][0] + 1) * len(oneList))
            oneList = [[do[0], do[1]]]

        if lastDay < do[1] :
            lastDay = do[1]

# 마지막 일정처리
if len(oneList) != 0 :
    coverList.append((lastDay - oneList[0][0] + 1) * len(oneList))

coverSum = 0
for c in coverList : coverSum+=c
print(coverSum)