import sys

def input():
    return sys.stdin.readline().rstrip()


def solve():
    day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yo_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    d = 0
    x, y = map(int, input().split())
    d += (sum(day_list[:x]) + y-1)
    print(yo_list[d % 7])


if __name__ == "__main__":
    solve()
