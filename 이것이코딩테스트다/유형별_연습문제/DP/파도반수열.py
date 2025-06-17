# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline



def calc_result(n):
    dp = [1,1,1,2,2]+ [0]*(n)
    
    for i in range(5, n):
        dp[i] = dp[i-5] + dp[i-1]

    return dp[n-1]

t = int(input())

for i in range(t):
    n = int(input())
    print(calc_result(n))
