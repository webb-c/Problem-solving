emg = input()
b  = 0
for ch in emg[5:] :
    if ch == "_" : b += 1
print(len(emg)+2+b*5)