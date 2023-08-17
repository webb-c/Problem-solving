import sys

def input(): return sys.stdin.readline().rstrip()

def main():
    nameList = input().split("-")
    algoName = "".join(name[0] for name in nameList)
    print(algoName)

if __name__ == "__main__":
    main()
