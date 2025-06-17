# https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))


# 탐색 위치까지 가장 긴 수열의 길이 dp 저장

dp = [1] * n

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))