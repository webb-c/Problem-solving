T = int(input())
for _ in range(T) :
    result = input()
    score = temp = 0
    for i in result :
        if i == "O" :
            temp+=1
            score+=temp
        else : temp = 0
    print(score)