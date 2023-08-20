import sys

def input(): return sys.stdin.readline().rstrip()

def get_denominator(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        if count > 4:
            break
    return count

def get_RSA(a, b):
    count = 0
    for n in range(a, b+1):
        if get_denominator(n) == 4:
            count += 1
    return count

def main():
    a = int(input())
    b = int(input())
    n = get_RSA(a, b)
    print("The number of RSA numbers between " +
          str(a)+" and "+str(b)+" is "+str(n))

if __name__ == "__main__":
    main()
