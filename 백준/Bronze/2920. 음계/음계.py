seq = list(map(int, input().split()))
output = "mixed"
for i, n in enumerate(seq) :
    if i==0 :
        if n==1 : output = "ascending"
        elif n==8 : output = "descending"
        else : break
    elif ((output == "ascending") and (seq[i-1] != n-1)) or ((output == "descending") and (seq[i-1] != n+1)):
        output = "mixed"
        break
print(output)