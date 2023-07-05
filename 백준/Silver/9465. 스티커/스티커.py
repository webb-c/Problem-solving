"""
단순한 DP 문제.
아이디어 : 동일한 열에 있는 스티커는 하나만 선택해야한다. 이웃한 열에서는 위-아래 형식으로 이어져야한다. 단, 이전의 열을 선택하지 않고
더 큰 값을 갖는 다른 방향의 스티커를 선택할 수도 있기 때문에 2가지 case 모두 고려하여 선택해줘야한다.
일반화 : totalValue[up][i] = max(totalValue[down][i-1] + totalValue[down][i-2]) + value[up][i] 이다.
"""

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    value = []
    value.append(list(map(int, input().split())))  # up
    value.append(list(map(int, input().split())))  # down

    maxValue = 0
    totalValue = [[0 for _ in range(n)], [0 for _ in range(n)]]
    for i in range(n):
        if i == 0:
            totalValue[0][i] = value[0][i]
            totalValue[1][i] = value[1][i]
        elif i == 1:
            totalValue[0][i] = totalValue[1][i - 1] + value[0][i]
            totalValue[1][i] = totalValue[0][i - 1] + value[1][i]
        else:
            totalValue[0][i] = (
                max(totalValue[1][i - 1], totalValue[1][i - 2]) + value[0][i]
            )
            totalValue[1][i] = (
                max(totalValue[0][i - 1], totalValue[0][i - 2]) + value[1][i]
            )
        maxValue = max(maxValue, totalValue[0][i], totalValue[1][i])
    print(maxValue)
