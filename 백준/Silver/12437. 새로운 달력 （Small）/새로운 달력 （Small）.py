import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def solve(totalMonth, dayPerMonth, dayPerWeek):
    basic = math.ceil(dayPerMonth/dayPerWeek)*totalMonth
    additional = 0
    remind = dayPerMonth % dayPerWeek
    space = dayPerWeek - remind
    for m in range(totalMonth-1):
        if space != 0 and remind > space:
            additional += 1
            space = dayPerWeek - (remind - space)
        elif space == 0:
            space = dayPerWeek - remind
        else:
            space = space - remind
    row = basic + additional
    return row

def main():
    T = int(input())
    for i in range(T):
        totalMonth, dayPerMonth, dayPerWeek = map(int, input().split())
        row = solve(totalMonth, dayPerMonth, dayPerWeek)
        print("Case #"+str(i+1)+": "+str(row))

if __name__ == "__main__":
    main()
