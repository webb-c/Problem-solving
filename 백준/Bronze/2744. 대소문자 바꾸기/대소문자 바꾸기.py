import sys
input = sys.stdin.readline

string = input().strip()
reString = ""
for ch in string:
    if "Z" < ch:
        reString += ch.upper()
    else:
        reString += ch.lower()

print(reString)
