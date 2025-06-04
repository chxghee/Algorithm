# https://www.acmicpc.net/problem/2775
import sys
import copy
input = sys.stdin.readline

def calc_resident(k, n):
    
    dp = [i for i in range(n+1)]

    for i in range(k):
        prev = copy.deepcopy(dp)
        for j in range(n+1):
            dp[j] = sum(prev[:j+1])
    
    return dp[n]

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    print(calc_resident(k,n))

    