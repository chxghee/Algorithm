import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * 100

dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i-2] + data[i], dp[i-1])

print(dp[n-1])
