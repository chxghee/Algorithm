# https://www.acmicpc.net/problem/15988
import sys
input = sys.stdin.readline


def result(m):
    global dp

    cur_len = len(dp)

    if cur_len > m:
        return dp[m]

    dp += [0] * (m - cur_len + 1)
    
    for i in range(cur_len, m+1):
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1_000_000_009
    
    return dp[m]



n = int(input())

dp = [0, 1, 2, 4]

for _ in range(n):
    m = int(input())
    print(result(m))