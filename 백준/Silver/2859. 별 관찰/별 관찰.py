"""
두 별이 반짝이는 주기에 대한 시작값이 다르기 때문에 단순히 최소공배수만을 구해서는 안된다.
최대 상한까지 점점 하나의 변수를 늘려가면서 다른 변수가 정수값이 되도록하는 경우가 존재하는지를 찾으면 된다.
구현이 귀찮다.
"""

import sys

input = sys.stdin.readline

BOUND = 5000
MtoH = 60
MtoD = 1440

dayList = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
s1H, s1M = map(int, input().split(":"))
s2H, s2M = map(int, input().split(":"))
sP1H, sP1M = map(int, input().split(":"))
sP2H, sP2M = map(int, input().split(":"))

startTime1 = s1H * MtoH + s1M
startTime2 = s2H * MtoH + s2M
period1 = sP1H * MtoH + sP1M
period2 = sP2H * MtoH + sP2M

flag = False
for n in range(BOUND):
    m = startTime1 + period1 * n
    if m - startTime2 < 0 or (m - startTime2) % period2 != 0:
        continue
    print(dayList[(m // MtoD) % 7])
    MM = str(m % MtoH)
    HH = str(m // MtoH % 24)
    if len(HH) < 2:
        HH = "0" * (2 - len(HH)) + HH
    elif len(MM) < 2:
        MM = "0" * (2 - len(MM)) + MM
    print(HH + ":" + MM)
    flag = True
    break
if not flag:
    print("Never")
