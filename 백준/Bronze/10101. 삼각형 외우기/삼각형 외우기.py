import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    if a1 == a2 or a2 == a3 or a1 == a3:
        if a1 == a2 == a3:
            if a1 == 60:
                print("Equilateral")
            else:
                print("Error")
        else:
            if a1 + a2 + a3 == 180:
                print("Isosceles")
            else:
                print("Error")
    else:
        if a1 + a2 + a3 == 180:
            print("Scalene")
        else:
            print("Error")


if __name__ == "__main__":
    main()
