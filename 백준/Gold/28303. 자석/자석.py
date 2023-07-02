# UCPC 예선 백준
import sys

input = sys.stdin.readline

def I():
    def solve(N, K):
        minJSN = 999999999999999999
        minJNS = 999999999999999999
        maxEnergy = -999999999999999999
        Energy = [0] + energy
        reverseEnergy = [0] + list(reversed(energy))
        for i in range(2, N + 1):
            j = i - 1
            minJSN = min(minJSN, Energy[j] - K * j)
            minJNS = min(minJNS, reverseEnergy[j] - K * j)
            maxEnergy = max(
                maxEnergy, Energy[i] - K * i - minJSN, reverseEnergy[i] - K * i - minJNS
            )
        return maxEnergy

    N, K = map(int, input().split())
    energy = list(map(int, input().split()))
    print(solve(N, K))

I()