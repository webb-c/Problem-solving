import sys

MOD = 1000000


def get_num_of_decryption(cryptogram, length):
    DP = [0] * length
    if int(cryptogram[0]) != 0: 
        DP[0] = 1
    if 1 < length:
        if int(cryptogram[1]) != 0:
            DP[1] += DP[0]
        if int(cryptogram[0]) != 0 and int(cryptogram[0:2]) < 27:
            DP[1] += 1
    
    for i in range(2, len(cryptogram)):
        if int(cryptogram[i]) != 0:
            DP[i] += DP[i-1]
        if int(cryptogram[i-1]) != 0 and int(cryptogram[i-1:i+1]) < 27:
            DP[i] += DP[i-2]
        
        DP[i] %= MOD
            
    return DP[-1]


def input():
    return sys.stdin.readline().rstrip()


def solve():
    cryptogram = input()
    length = len(cryptogram)
    print(get_num_of_decryption(cryptogram, length))
    

if __name__ == "__main__":
    solve()
    