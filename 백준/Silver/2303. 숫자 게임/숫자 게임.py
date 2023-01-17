N = int(input())
winner = 0
maxNum = -1
for i in range(N):
    cardList = list(map(int,input().split()))
    score = []
    for number in cardList:
        for a in range(3):
            for b in range(a+1, 4):
                for c in range(b+1, 5):
                    score.append((cardList[a]+cardList[b]+cardList[c])%10)
        maxscore = max(score)
        if maxNum <= maxscore :
            winner = i+1
            maxNum = maxscore

print(winner)