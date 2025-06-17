# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
dp = [[INF] * (n+1) for _ in range(n+1)]

# init DP table 
for i in range(m):
    start, end, cost = map(int, input().split())
    dp[start][end] = min(dp[start][end], cost)

for i in range(n+1):
    dp[i][i] = 0

for node in range(1, n+1):
    for start  in range(1, n+1):
        for end  in range(1, n+1):
            if start != end:
                dp[start][end] = min(dp[start][node] + dp[node][end], dp[start][end])

for i in range(1, n+1):
    for j in range(1, n+1):
        d = dp[i][j]
        if d != INF:
            print(d, end=' ')
        else:
            print(0,end=' ')
    print()

