# UCPC 예선 백준
import sys
import heapq


# start N ->
def A():
    totalSum = 0
    for _ in range(10):
        n = int(input())
        if n == 3:
            n = -1
        totalSum += n
    remind = totalSum % 4
    if remind == 0:
        result = "N"
    elif remind == 1:
        result = "E"
    elif remind == 2:
        result = "S"
    elif remind == 3:
        result = "W"
    print(result)


A()