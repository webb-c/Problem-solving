import sys

def input():
    return sys.stdin.readline().rstrip()

def get_score(x, y):
    d = (x**2 + y**2)**0.5
    if d <= 3:
        return 100
    elif d <= 6:
        return 80
    elif d <= 9:
        return 60
    elif d <= 12:
        return 40
    elif d <= 15:
        return 20
    else:
        return 0

def solve(a, b):
    a_score, b_score = 0, 0
    for i in range(0, 5, 2):
        a_score += get_score(a[i], a[i+1])
        b_score += get_score(b[i], b[i+1])

    if a_score > b_score:
        print("SCORE: "+str(a_score)+" to "+str(b_score)+", PLAYER 1 WINS.")
    elif a_score < b_score:
        print("SCORE: "+str(a_score)+" to "+str(b_score)+", PLAYER 2 WINS.")
    else:
        print("SCORE: "+str(a_score)+" to "+str(b_score)+", TIE.")

def main():
    T = int(input())
    for _ in range(T):
        line = list(map(float, input().split()))
        a = line[:6]
        b = line[6:]
        solve(a, b)

if __name__ == "__main__":
    main()
