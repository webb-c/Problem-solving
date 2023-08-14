import sys

def input(): return sys.stdin.readline().rstrip()

def main():
    money = 1000 - int(input())
    coins = [500, 100, 50, 10, 5, 1]
    count = 0
    while True:
        flag = False
        for coin in coins:
            if money >= coin:
                money -= coin
                count += 1
                flag = True
                break
        if not flag:
            break
    print(count)

if __name__ == "__main__":
    main()
