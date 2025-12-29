# https://www.acmicpc.net/problem/10844
import sys
input = sys.stdin.readline

n = int(input())


# 마지막 자리를 추가 할 건데,
# 그럼 현재 구하는 길이가 n 이라면 n-1 의 경우의 수를 더해야 함 
# 마지막 수를 기준으로 -1 +1의 테이블을 구성

dp = [[0] * 10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):

        if j - 1>=0:
            dp[i][j] += dp[i-1][j-1]
        if j + 1 < 10:
            dp[i][j] += dp[i-1][j+1]
        
        dp[i][j] %= 1_000_000_000

print(sum(dp[n]) % 1_000_000_000)


