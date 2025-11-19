# https://www.acmicpc.net/problem/1890
import sys

input = sys.stdin.readline


def check_range(now, jp):
    return 0 <= now + jp < n


n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

# 밟을 수 있는 경우를 계산한다.
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
            
        jump = game[i][j]

        if check_range(i, jump):
            dp[i + jump][j] += dp[i][j]

        if check_range(j, jump):
            dp[i][j + jump] += dp[i][j]

print(dp[n-1][n-1])