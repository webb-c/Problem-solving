import sys

def input():
    return sys.stdin.readline().rstrip()

def eratosthenes_sieve(Min, Max):
    isSquareNN = [1] * (Max-Min + 1)
    for i in range(2, int(Max**0.5)+1):
        square = i*i
        start = ((Min-1)//square + 1)*square
        for j in range(start, Max+1, square):
            if isSquareNN[j-Min] == 1:
                isSquareNN[j-Min] = 0
    return sum(isSquareNN)

def main():
    Min, Max = map(int, input().split())
    result = eratosthenes_sieve(Min, Max)
    print(result)

if __name__ == "__main__":
    main()
