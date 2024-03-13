import sys


def input():
    return sys.stdin.readline().rstrip()


def bubble_Sort(A):
    for j in range(7):
        sorted = True
        last = 7 - j
        for i in range(last):
            n1 = A[i][0]
            n2 = A[i+1][0]
            if ((n1[0] > n2[0]) or ((n1[0] == n2[0]) and (n1[1] > n2[1])) or ((n1[0] == n2[0]) and (n1[1] == n2[1]) and (n1[2] > n2[2]))):
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                sorted = False
        if sorted:
            break
    return A


def solve():
    A = []
    for _ in range(8):
        time_str, team = input().split()
        time_lst = list(map(int, time_str.split(':')))
        A.append([time_lst, team])

    sort_A = bubble_Sort(A)

    red, blue = 0, 0
    score = [10, 8, 6, 5, 4, 3, 2, 1, 0]
    for i, car in enumerate(sort_A):
        if car[1] == 'R':
            red += score[i]
        else:
            blue += score[i]
    if red > blue:
        print("Red")
    else:
        print("Blue")


if __name__ == "__main__":
    solve()
