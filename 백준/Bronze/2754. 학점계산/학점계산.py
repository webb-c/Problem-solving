import sys
input = sys.stdin.readline


def calculate_gpa(g):
    gpa = 0.0
    if len(g) == 1:
        return gpa

    if g[0] == "A":
        gpa += 4.0
    elif g[0] == "B":
        gpa += 3.0
    elif g[0] == "C":
        gpa += 2.0
    elif g[0] == "D":
        gpa += 1.0

    if g[1] == "0":
        return gpa
    elif g[1] == "-":
        return gpa-0.3
    elif g[1] == "+":
        return gpa+0.3


g = list(input().split()[0])
print(calculate_gpa(g))
