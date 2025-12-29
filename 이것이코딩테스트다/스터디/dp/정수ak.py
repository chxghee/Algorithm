# https://www.acmicpc.net/problem/25418
import sys

INF = 1000000

a, k = map(int, input().split())


dp = [INF] * (k+1)
dp[a] = 0
for i in range(a+1, k+1):

    if i % 2 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)
    else:
        dp[i] = dp[i-1] + 1

print(dp[k])