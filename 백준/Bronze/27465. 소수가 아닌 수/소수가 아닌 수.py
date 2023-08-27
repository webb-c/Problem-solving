import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    # 2가 아닌 짝수는 모두 소수임을 활용
    N = int(input())
    if N == 1:
        print(4)
    else:
        print(2*N)

if __name__ == "__main__":
    main()
