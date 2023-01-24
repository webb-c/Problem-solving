# [Bronze 1] Meats On The Grill - 10219 🌟

n = int(input())
for _ in range(n) :
    # 입력
    h, w = map(int, input().split())
    for i in range(h) :
        line = input()
        print(''.join(reversed(line)))