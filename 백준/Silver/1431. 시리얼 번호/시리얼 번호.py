import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def check_sum(serial_num):
    result = 0
    for n in serial_num:
        if n.isdigit(): result += int(n)
    return result


def solve():
    N = int(input())
    serial_num_list = [input() for i in range(N)]
    serial_num_list.sort(key = lambda x:(len(x), check_sum(x), x))
    for serial_num in serial_num_list:
        print(serial_num)

    
if __name__ == "__main__":
    solve()
