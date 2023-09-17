import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = list(map(int, list(input())))
    N.reverse()
    result = 0
    for idx in range(len(N)):
        if 4 < N[idx]:
            N[idx] = N[idx] - 1
        result += N[idx] * (9**idx)
    print(result)

if __name__ == "__main__":
    main()
