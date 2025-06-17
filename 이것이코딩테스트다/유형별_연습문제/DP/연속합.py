# https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# dp[i]: i번째까지의 수열 중, i를 반드시 포함하는 최대 연속합 -> 최종 답은 dp중 max
dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i], data[i])
    
print(max(dp))