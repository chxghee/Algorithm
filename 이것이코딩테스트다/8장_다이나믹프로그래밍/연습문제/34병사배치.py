# https://www.acmicpc.net/problem/18353

import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

# 열외도지 않는 사람 수
dp = [1] * (n) 

for i in range(1,n):
    for j in range(0,i):
        if data[j] > data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(n-max(dp))