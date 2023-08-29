import sys

def input():
    return sys.stdin.readline().rstrip()

def is_prime(n):
    isPrime = True
    if n < 2:
        isPrime = True
    else:
        for p in range(2, n):
            if n % p == 0:
                isPrime = False
    return isPrime

def main():
    word = input()
    wordVal = 0
    for ch in word:
        if ch.isupper():
            wordVal += ord(ch)-ord("A")+27
        else:
            wordVal += ord(ch)-ord("a")+1
    if is_prime(wordVal):
        print("It is a prime word.")
    else:
        print("It is not a prime word.")

if __name__ == "__main__":
    main()
