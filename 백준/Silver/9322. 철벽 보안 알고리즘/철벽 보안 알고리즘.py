import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(n, pubKey_1, pubKey_2, cipherText):
    positions = [pubKey_1.index(word) for word in pubKey_2]
    plainText = [cipherText[positions.index(i)] for i in range(n)]
    return plainText

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        pubKey_1 = input().split()
        pubKey_2 = input().split()
        cipherText = input().split()
        plainText = solve(n, pubKey_1, pubKey_2, cipherText)
        print(*plainText)

if __name__ == "__main__":
    main()
