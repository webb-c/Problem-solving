import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    E, S, M = map(int, input().split())
    yearParam = [1, 1, 1]
    result = 1
    while True:
        if yearParam[0] == E and yearParam[1] == S and yearParam[2] == M:
            print(result)
            break
        if yearParam[0] >= 15:
            yearParam[0] = yearParam[0] % 15
        if yearParam[1] >= 28:
            yearParam[1] = yearParam[1] % 28
        if yearParam[2] >= 19:
            yearParam[2] = yearParam[2] % 19
        for i in range(3):
            yearParam[i] += 1
        result += 1

if __name__ == "__main__":
    main()
