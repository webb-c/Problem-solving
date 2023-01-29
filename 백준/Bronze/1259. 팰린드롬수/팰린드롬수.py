while True:
    num = input()
    if num == '0' : break
    elif num == ''.join(reversed(num)) : print("yes")
    else : print("no")